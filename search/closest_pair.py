import numpy as np


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def brute_force_closest_pair(arr: list) -> float:
    """
    Find distance between two closest points in list of points
    :param arr:list of point
    :return:distance between closest pair
    """
    d = np.inf
    n = len(arr)
    for i in range(n-1):
        for j in range(i+1, n):
            dis = (arr[i].x - arr[j].x)*(arr[i].x - arr[j].x) + (arr[i].y - arr[j].y)*(arr[i].y - arr[j].y)
            d = dis if dis < d else d
    return d


if __name__ == "__main__":
    list_points = [Point(1, 2), Point(4, 5), Point(6, 9), Point(2, 4), Point(11, 6)]
    min_distance = brute_force_closest_pair(list_points)
    print(np.sqrt(min_distance))
