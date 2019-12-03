import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from day3.task2 import calculate_steps_to_coordinate, get_crossing_with_least_amount_of_total_steps


class TestCalculateStepsToCoordinate:
    def test_calculates_correct_steps(self):
        coordinate = (3, 0)
        wire_coordinates = [(0, 0), (1, 0), (2, 0), (3, 0)]
        expected_steps = 3

        steps = calculate_steps_to_coordinate(coordinate, wire_coordinates)
        
        assert steps == expected_steps


class TestGetCrossingWithLeastAmountOfTotalSteps:
    def test_gets_correct_crossing(self):
        start = (0, 0)
        wire1_path = ['R8', 'U5', 'L5', 'D3']
        wire2_path = ['U7', 'R6', 'D4', 'L4']
        expected_crossing = (6, 5)
        expected_distance = 30

        crossing, distance = get_crossing_with_least_amount_of_total_steps(start, wire1_path, wire2_path)

        assert crossing == expected_crossing
        assert distance == expected_distance