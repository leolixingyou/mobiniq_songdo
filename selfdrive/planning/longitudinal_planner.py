import rospy
import math
import time

from std_msgs.msg import Float32
from geometry_msgs.msg import PoseArray, Pose

from selfdrive.planning.libs.planner_utils import *
from selfdrive.visualize.rviz_utils import *

from collections import deque

import csv
import datetime
import os

KPH_TO_MPS = 1 / 3.6
MPS_TO_KPH = 3.6
HZ = 10

current_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
file_name = f'acc_test_data_{current_time}.csv'
directory = "data"
def write_to_csv(data):
    if not os.path.exists(directory):
        os.makedirs(directory)

    file_path = os.path.join(directory, file_name)
    is_new_file = not os.path.exists(file_path)

    with open(file_path, mode='a') as csvfile:
        writer = csv.writer(csvfile)
        if is_new_file:
            header = ['timestamp', 'near_obj_id', 'v_lead(km/h)','desired_follow_d(m)', 'front_car_d(-10)(m)', 'error', 'acc(m/s^2)','target_v','cur_v']
            writer.writerow(header)

        current_timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data.insert(0, current_timestamp)
        writer.writerow(data)

class LongitudinalPlanner:
    def __init__(self, CP):
        self.lidar_obstacle = None
        self.traffic_light_obstacle = None
        self.can_go_check_tick = -1
        self.lane_information = None
        self.goal_object = None
        self.M_TO_IDX = 1/CP.mapParam.precision
        self.IDX_TO_M = CP.mapParam.precision

        self.ref_v = CP.maxEnableSpeed
        self.min_v = CP.minEnableSpeed
        self.target_v = 0
        self.st_param = CP.stParam._asdict()
        self.sl_param = CP.slParam._asdict()

        self.last_error = 0
        self.last_s = None
        self.follow_error = 0
        self.integral = 0
        self.rel_v = 0
        self.prev_rel_v = None
        self.consecutive_outliers = 0
        self.outlier_threshold = 3  # 연속 이상치 허용 횟수
        self.distance_queue = deque(maxlen=5)

        self.closest_tracked = None
        self.closest_untracked = None

        rospy.Subscriber('/mobinha/perception/lidar_obstacle', PoseArray, self.lidar_obstacle_cb)
        rospy.Subscriber('/mobinha/perception/traffic_light_obstacle',PoseArray, self.traffic_light_obstacle_cb)
        rospy.Subscriber('/mobinha/planning/lane_information',Pose, self.lane_information_cb)
        rospy.Subscriber('/mobinha/planning/goal_information', Pose, self.goal_object_cb)
        self.pub_target_v = rospy.Publisher('/mobinha/planning/target_v', Float32, queue_size=1, latch=True)
        self.pub_traffic_light_marker = rospy.Publisher('/mobinha/planner/traffic_light_marker', Marker, queue_size=1)
        self.pub_accerror = rospy.Publisher('/mobinha/control/accerror', Float32, queue_size=1)

    def lidar_obstacle_cb(self, msg):
        self.lidar_obstacle = [(pose.position.x, pose.position.y, pose.position.z, pose.orientation.w, pose.orientation.z)for pose in msg.poses]

    def traffic_light_obstacle_cb(self, msg):
        self.traffic_light_obstacle = [(pose.position.x, pose.position.y, pose.position.z)for pose in msg.poses]

    def lane_information_cb(self, msg):
        # [0] id, [1] forward_direction, [2] cross_walk distance [3] forward_curvature
        self.lane_information = [msg.position.x,msg.position.y, msg.position.z, msg.orientation.x]

    def goal_object_cb(self, msg):
        self.goal_object = (msg.position.x, msg.position.y, msg.position.z)

    def sigmoid_logit_function(self, s):
        if s <=0:
            out = 0
        elif s >= 1:
            out = 1
        else:
            out = ((1+((s*(1-self.sl_param["mu"]))/(self.sl_param["mu"]*(1-s)))**-self.sl_param["v"])**-1).real
        return out

    def get_safe_obs_distance_s(self, v_ego, desired_ttc=3, comfort_decel=3, offset=5): # cur v = v ego (m/s), 2 sec, 2.5 decel (m/s^2)
        return ((v_ego ** 2) / (2 * comfort_decel) + desired_ttc * v_ego + offset)
        # return desired_ttc * v_ego + offset
    
    def desired_follow_distance_s(self, v_ego):
        return max(5, self.get_safe_obs_distance_s(v_ego))
    
    def get_stoped_equivalence_factor(self, v_lead, comfort_decel=3):
        if v_lead <= 5 * KPH_TO_MPS:
            v_lead = 0
        # elif 10 * KPH_TO_MPS < v_lead <= 20 * KPH_TO_MPS:
        #     v_lead = 12 * KPH_TO_MPS
        # elif 20 * KPH_TO_MPS < v_lead <= 30 * KPH_TO_MPS:
        #     v_lead = 22 * KPH_TO_MPS
        # elif 30 * KPH_TO_MPS < v_lead <= 40 * KPH_TO_MPS:
        #     v_lead = 32 * KPH_TO_MPS
        # elif 40 * KPH_TO_MPS < v_lead <= 45 * KPH_TO_MPS:
        #     v_lead = 42 * KPH_TO_MPS
        else:
            v_lead = v_lead
        return ((v_lead**2) / (2*comfort_decel))

    def get_safe_obs_distance(self, v_ego, desired_ttc=4, comfort_decel=3, offset=5): # cur v = v ego (m/s), 2 sec, 2.5 decel (m/s^2)
        return ((v_ego ** 2) / (2 * comfort_decel) + desired_ttc * v_ego + offset)
        # return desired_ttc * v_ego + offset
    
    def desired_follow_distance(self, v_ego, v_lead=0):
        return max(5, self.get_safe_obs_distance(v_ego) - self.get_stoped_equivalence_factor(v_lead)) 

    def get_dynamic_gain(self, error, ttc, kp=0.2/HZ, ki=0.0/HZ, kd=0.08/HZ):
        # if -1 < error < 1:
        #     error = 0
        # elif error < -1:
        #     error = error + 1
        # elif error > 1:
        #     error = error - 1
        self.integral += error*(1/HZ)
        self.integral = max(-6, min(self.integral, 6))
        derivative = (error - self.last_error)/(1/HZ) #  frame calculate.
        self.last_error = error
        # print(ttc)
        if error < 0:
            return max(0/HZ, min(2.5/HZ, -(kp*error + ki*self.integral + kd*derivative)))
        elif 0 < ttc < -3:
            print("collision warning!!", "decel: ", min(0/HZ, max(-7/HZ, -(kp*error + ki*self.integral + kd*derivative))))
            return min(0/HZ, max(-7/HZ, -(kp*error + ki*self.integral + kd*derivative)))
        else:
            print("decel: ", min(0/HZ, max(-3.5/HZ, -(kp*error + ki*self.integral + kd*derivative))))
            return min(0/HZ, max(-3.5/HZ, -(kp*error + ki*self.integral + kd*derivative)))
        # TODO: error part 0~-7 0~-3
        
    def get_static_gain(self, error, ttc, gain=0.1/HZ):
        if error < 0:
            return 2.5 / HZ
        elif 0 < ttc < 3:
            print("collision warning!!", "decel: ", max(0/HZ, min(7/HZ, error*gain))*10)
            return max(0/HZ, min(7/HZ, error*gain))
        else:
            print("decel: ", max(0/HZ, min(4/HZ, error*gain))*10)
            return max(0/HZ, min(4/HZ, error*gain))
        
    def dynamic_consider_range(self, max_v, base_range=50):  # input max_v unit (m/s)
        return (base_range + (0.267*(max_v)**1.902))*self.M_TO_IDX 

    def get_params(self, max_v, distance):# input distance unit (idx) # TODO: distance unit (m)
        consider_distance = self.dynamic_consider_range(self.ref_v*KPH_TO_MPS) # consider_distance unit (idx) 
        if 0 < distance < consider_distance:
            norm_s = distance/consider_distance
        elif distance >= consider_distance:
            norm_s = 1
        else:
            norm_s = 0
        min_s = distance*self.IDX_TO_M
        pi = self.sigmoid_logit_function(norm_s)# if 0<norm_s<1 else 1
        target_v = max_v * pi
        return target_v, min_s
    
    def static_velocity_plan(self, cur_v, max_v, static_d):
        target_v, min_s = self.get_params(max_v, static_d) # input static d unit (idx), output min_s unit (m)
        follow_distance = self.desired_follow_distance_s(cur_v) #output follow_distance unit (m)
        ttc = min_s / cur_v if cur_v != 0 else min_s
        self.follow_error = follow_distance-min_s # negative is acceleration. but if min_s is nearby 0, we need deceleration.
        gain = self.get_static_gain(self.follow_error, ttc)
        if self.follow_error < 0: # MINUS is ACCEL
            target_v = min(max_v, self.target_v + gain)
        else: # PLUS is DECEL
            target_v = max(0, self.target_v - gain)
        # target_v = max(self.target_v - gain, min(target_v, self.target_v + gain))
        # print(min_s, follow_distance,self.follow_error, gain)
        # write_to_csv([1,0,round(follow_distance,1),round(min_s,1),round(self.follow_error,3),round(gain*HZ,2),round(target_v,2),round(cur_v,2)])
        return target_v

    def dynamic_velocity_plan(self, cur_v, max_v, dynamic_d):
        target_v, min_s = self.get_params(max_v, dynamic_d) # input static d unit (idx), output min_s unit (m)
        follow_distance = self.desired_follow_distance(cur_v, self.rel_v + cur_v) #output follow_distance unit (m)
        ttc = min_s / self.rel_v if self.rel_v != 0 else min_s# minus value is collision case
        self.follow_error = follow_distance-min_s
        gain = self.get_dynamic_gain(self.follow_error, ttc)
        if self.follow_error < 0: # MINUS is ACCEL
            target_v = min(max_v, self.target_v + gain)
        else: # PLUS is DECEL
            target_v = max(0, self.target_v + gain)
        # v_lead = self.rel_v + cur_v
        # if v_lead <= 10 * KPH_TO_MPS:
        #     v_lead = 0
        # elif 10 * KPH_TO_MPS < v_lead <= 40 * KPH_TO_MPS:
        #     v_lead = 30 * KPH_TO_MPS
        # else:
        #     v_lead = v_lead     
        # print("lead v:", round((v_lead)*MPS_TO_KPH,1) ,"flw d:", round(follow_distance), "obs d:", round(min_s), "err(0):",round(self.follow_error,2), "gain:",round(gain,3))
        # write_to_csv([0,round((v_lead) * MPS_TO_KPH, 1),round(follow_distance,1),round(min_s,1),round(self.follow_error,3),round(gain*HZ,2),round(target_v,2),round(cur_v,2)])

        return target_v

    def traffic_light_to_obstacle(self, traffic_light, forward_direction):
        # TODO: consideration filtering
        stop_list = [[6, 8, 10, 11, 12, 13], [4, 6, 8, 9, 10, 11, 13], [
            6, 8, 10, 11, 12, 13], [6, 8, 10, 11, 12, 13], [6, 8, 10, 11, 12, 13], [4, 6, 8, 9, 10, 11, 13]]
        if traffic_light in stop_list[forward_direction]:
            self.can_go_check_tick = -1
            return False
        else:
            if self.can_go_check_tick < 4:
                self.can_go_check_tick += 1
                return False
            else:
                return True

    def check_dynamic_objects(self, cur_v, local_s):
        offset = 8.5*self.M_TO_IDX
        dynamic_d = 80*self.M_TO_IDX 
        self.rel_v = 0
        if self.lidar_obstacle is not None:
            for lobs in self.lidar_obstacle:
                if lobs[2] >= -1.5 and lobs[2] <= 1.5:  # object in my lane
                    if lobs[4] >= 1: # tracking
                        dynamic_d = lobs[1]-offset-local_s
                        self.rel_v = lobs[3]
                        print("track car:",dynamic_d*self.IDX_TO_M,"m")
                        return dynamic_d
                    else: # only cluster is track_id = 0
                        dynamic_d = lobs[1]-offset-local_s
                        self.rel_v = 0 # TODO: track and cluster box color modify
                        print("cluster car:",dynamic_d*self.IDX_TO_M,"m")
                        return dynamic_d
            
        return dynamic_d
    
    def check_static_object(self, local_path, local_s):
        local_len = len(local_path)
        goal_offset = 1.5*self.M_TO_IDX
        tl_offset = 7*self.M_TO_IDX
        static_d1, static_d2 = 80*self.M_TO_IDX, 80*self.M_TO_IDX
        # [1] = Goal Object
        if self.goal_object is not None:
            left = (self.goal_object[1]-self.goal_object[2]) * self.M_TO_IDX
            if left <= local_len:
                if left-goal_offset < 80*self.M_TO_IDX:
                    static_d1 = left-goal_offset

        # [2] = Traffic Light
        if self.traffic_light_obstacle is not None:
            can_go = False
            if len(self.traffic_light_obstacle) > 0:
                tlobs = self.traffic_light_obstacle[0]
                if self.traffic_light_to_obstacle(int(tlobs[1]), int(self.lane_information[1])):
                    can_go = True
            if not can_go:
                if self.lane_information[2] < math.inf:
                    if self.lane_information[2]-tl_offset-local_s < 80*self.M_TO_IDX:
                        static_d2 = self.lane_information[2]-tl_offset-local_s
                    if static_d2 < -13*self.M_TO_IDX: # passed traffic light is not considered
                        static_d2 = 80*self.M_TO_IDX
                print("stop line: ", static_d2*self.IDX_TO_M,"m")
        return min(static_d1, static_d2)

    def run(self, sm, pp=0, local_path=None):
        CS = sm.CS
        lgp = 0
        self.pub_target_v.publish(Float32(self.target_v))
        self.pub_accerror.publish(Float32(self.follow_error))
        if local_path != None and self.lane_information != None:
            local_idx = calc_idx(local_path, (CS.position.x, CS.position.y))
            if CS.cruiseState == 1:
                local_curv_v = calculate_v_by_curvature(self.lane_information, self.ref_v, self.min_v, CS.vEgo)
                #local_curv_v = max_v_by_curvature(self.lane_information[3], self.ref_v, self.min_v, CS.vEgo)
                #local_curv_v= self.ref_v*KPH_TO_MPS
                static_d = self.check_static_object(local_path, local_idx) # output unit: idx
                dynamic_d = self.check_dynamic_objects(CS.vEgo, local_idx) # output unit: idx
                target_v_static = self.static_velocity_plan(CS.vEgo, local_curv_v, static_d)
                target_v_dynamic = self.dynamic_velocity_plan(CS.vEgo, local_curv_v, dynamic_d)
                self.target_v = min(target_v_static, target_v_dynamic)
            else:
                self.target_v = CS.vEgo

            if pp == 2:
                self.target_v = 0.0
                if CS.vEgo <= 0.01:
                    lgp = 2
            else:
                lgp = 1

        return lgp
