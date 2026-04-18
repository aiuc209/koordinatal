import pytest
import math

def distance_to_axis(point):
    return min(abs(point[0]), abs(point[1]))

def test_distance_to_axis():
    assert distance_to_axis((3, 4)) == 3
    assert distance_to_axis((0, 5)) == 0
    assert distance_to_axis((-2, 0)) == 0
    assert distance_to_axis((0, 0)) == 0
    assert distance_to_axis((-1, -1)) == 1

def test_distance_to_axis_list():
    points = [(1, 2), (3, 4), (5, 6)]
    distances = [distance_to_axis(point) for point in points]
    assert distances == [1, 3, 5]

def test_distance_to_axis_empty_list():
    points = []
    distances = [distance_to_axis(point) for point in points]
    assert distances == []
