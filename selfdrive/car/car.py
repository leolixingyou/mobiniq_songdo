#!/usr/bin/python

import sys
import signal
import time
import rospy
from std_msgs.msg import String

from selfdrive.message.messaging import *
from selfdrive.car.simulator_transceiver import SimulatorTransceiver
from selfdrive.car.niro_transceiver import NiroTransceiver


def signal_handler(sig, frame):
    sys.exit(0)


class Transceiver:
    def __init__(self):
        self.state = 'None'
        sub_state = rospy.Subscriber('/state', String, self.state_cb)

    def transceiver(self):
        can = None
        while True:
            if self.state == 'WAITING':
                can = self.init()
            elif self.state == 'START':
                can.run()
            elif self.state == 'INITIALIZE':
                can = self.init()
            elif self.state == 'FINISH':
                return 1
            time.sleep(0.1)

    def init(self):
        car = rospy.get_param('car_name', 'None')
        CP = getattr(sys.modules[__name__], car).CP
        if car == "SIMULATOR":
            can = SimulatorTransceiver(CP)
        else:
            can = NiroTransceiver

        return can

    def state_cb(self, msg):
        if self.state != str(msg.data):
            if str(msg.data) == 'START':
                print("[{}] Start".format(self.__class__.__name__))
            elif str(msg.data) == 'INITIALZE':
                print("[{}] Initialize".format(self.__class__.__name__))
        self.state = str(msg.data)


def main():
    signal.signal(signal.SIGINT, signal_handler)
    rospy.init_node('Car', anonymous=False)
    t = Transceiver()
    print("[{}] Created".format(t.__class__.__name__))

    try:
        if t.transceiver() == 1:
            print("[Car Process] Over")
            time.sleep(3)
            sys.exit(0)

    except Exception as e:
        print("[{} Error]".format(t.__class__.__name__), e)
    except KeyboardInterrupt:
        print("[{}] Force Quit".format(t.__class__.__name__))
        sys.exit(0)


if __name__ == "__main__":
    main()