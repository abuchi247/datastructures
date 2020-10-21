# Find all points within a certain distance of another point

# distance = sqrt((x2-x2)^2 + (y2-y1)^2))
from math import sqrt


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, other_point):
        """
        Calculates the distance between two points
        :param other_point:
        :return: return the distance
        """
        distance = sqrt(pow((other_point.x - self.x), 2) + pow((other_point.y - self.y), 2))
        return distance

    def is_within_distance(self, other_point, desired_distance):
        """
        Checks if the two points are within a certain distance
        :param other_point:
        :param desired_distance:
        :return: True or false on whether the points are within a given distance
        """
        # shortcut if a point exceeds any of the axis
        if abs(self.x - other_point.x) > desired_distance or abs(self.y - other_point.y) > distance:
            return False
        return self.get_distance(other_point) <= desired_distance


def getPointsWithinDistance(points_list, central_point, distance):
    """

    :param points_list:
    :param central_point:
    :param distance:
    :return:
    """
    points_within_distance = []

    for point in points_list:
        if point.is_within_distance(central_point, distance):
            points_within_distance.append(point)

    print(f"Points with {distance} of point x = {central_point.x}, y = {central_point.y}")

    for point in points_within_distance:
        print(f"Point: x = {point.x}, y = {point.y}")



if __name__ == "__main__":
    central_point = Point(0, 0)
    distance = 10
    points = [Point(3, 4), Point(12, 13), (Point(2, 5))]

    getPointsWithinDistance(points_list=points, central_point=central_point, distance=distance)

