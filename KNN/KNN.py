import math


# 根据数学上直角坐标系上两点间距离
def ComputeEuclideanDistance(x1, y1, x2, y2):
    d = math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2))
    return d


d_ag = ComputeEuclideanDistance(0, 0, 3, 4)

print(d_ag)
