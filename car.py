import pandas
import matplotlib.pyplot as plt
import math
import numpy as np

ground_truth = pandas.read_csv("ground_truth.csv")
x = pandas.read_csv("x.csv")
y = pandas.read_csv("y.csv")
xEst = []
yEst = []


def centroid(vertexes):
    _x_list = [vertex[0] for vertex in vertexes]
    _y_list = [vertex[1] for vertex in vertexes]
    _len = len(vertexes)
    _x = sum(_x_list) / _len
    _y = sum(_y_list) / _len
    return [_x, _y]


def draw_elipse(Px, Py, Qx, Qy, Rx, Ry, Sx, Sy):
    minor = math.dist([Px, Py], [Qx, Qy])
    major = math.dist([Rx, Ry], [Sx, Sy])
    polygon_data = [[Px, Py], [Qx, Qy], [Rx, Ry], [Sx, Sy]]
    [u, v] = centroid(polygon_data)
    xEst.append(u)
    yEst.append(v)
    a = major / 2  # radius on the x-axis
    b = minor / 2  # radius on the y-axis

    t = np.linspace(0, 2 * np.pi, 100)
    plt.plot(u + a * np.cos(t), v + b * np.sin(t), '--r')


for i in range(0, len(x["x"])):
    plt.cla()
    plt.plot(ground_truth["position_x"][0:i * 5], ground_truth["position_y"][0:i * 5], 'k-')
    plt.plot(x["x"][0:i], y["y"][0:i], '.g')
    if i > 4:
        draw_elipse(x["x"][i - 3], y["y"][i - 3], x["x"][i - 2], y["y"][i - 2], x["x"][i - 1], y["y"][i - 1], x["x"][i],
                    y["y"][i])
    plt.plot(xEst, yEst, '-r')
    plt.axis("equal")
    plt.pause(0.00001)

plt.show()
data = {
    'xEst': xEst,
    'yEst': yEst}

poseEst = pandas.DataFrame(data)
poseEst.to_csv('poseEst.csv')
