from libs import cubic_spline_planner
import matplotlib.pyplot as plt
import numpy as np

from shapely.geometry import LineString
import geopandas as gpd
import utm
import pymap3d


def interpolate_points(geom, distance):  # Input gpd linestring
    if geom.geom_type == 'LineString':
        num_vert = int(round(geom.length / distance))
        if num_vert == 0:
            num_vert = 1
        return LineString(
            [geom.interpolate(float(n) / num_vert, normalized=True)
             for n in range(num_vert + 1)])

def get_coord():
    shpfile = gpd.read_file('./weekdays/path.shp')  # read shp
    shpfile = shpfile.to_crs('epsg:32652')
    shpfile = interpolate_points(shpfile.geometry[0], 5)
    path = shpfile.coords

    X, Y = [], []
    for x, y in path:
        out = utm.to_latlon(x, y, 52, 'N')
        out = pymap3d.geodetic2enu(out[0], out[1], 0, 37.5833501770936, 126.88227370105241, 0)
        X.append(out[0])
        Y.append(out[1])
    return X, Y
    return path

def save(path):
    import pickle
    with open('weekdays.pkl', 'wb') as f:
        pickle.dump(path, f)

def generate():
    x, y = get_coord()

    sp = cubic_spline_planner.Spline(x, y)
    csp = cubic_spline_planner.Spline2D(x, y)

    s = np.arange(0, csp.s[-1], 1)

    rx, ry, ryaw, rk = [], [], [], []
    for i_s in s:
        ix, iy = csp.calc_position(i_s)
        rx.append(ix)
        ry.append(iy)
        ryaw.append(csp.calc_yaw(i_s))
        rk.append(csp.calc_curvature(i_s))

    save([(rx[i], ry[i]) for i in range(len(rx))])

if __name__ == '__main__':
    generate()
