from day3.task1 import get_line_coordinates, get_wire_coordinates, get_crossing_coordinates, calculate_manhattan_distance, get_crossing_closest_to_start


class TestGetLineCoordinates:
    def test_gets_correct_coordinates(self):
        start = (0, 0)
        direction = 'R'
        steps = 3
        expected_coordinates = [(0, 0), (1, 0), (2, 0), (3, 0)]

        coordinates = get_line_coordinates(start, direction, steps)

        assert coordinates == expected_coordinates


class TestGetWireCoordinates:
    def test_gets_correct_coordinates(self):
        start = (0, 0)
        wire_path = ['R3', 'U2']
        expected_coordinates = [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2)]
        
        coordinates = get_wire_coordinates(start, wire_path)

        assert coordinates == expected_coordinates


class TestGetCrossingCoordinates:
    def test_gets_correct_coordinates(self):
        start = (0, 0)
        wire1_path = ['R8', 'U5', 'L5', 'D3']
        wire2_path = ['U7', 'R6', 'D4', 'L4']
        expected_coordinates = {(0, 0), (3, 3), (6, 5)}

        coordinates = get_crossing_coordinates(start, wire1_path, wire2_path)

        assert coordinates == expected_coordinates


class TestCalculateManhattanDistance:
    def test_gets_correct_distance(self):
        p1 = (0, 0)
        p2 = (3, 3)
        expected_distance = 6

        distance = calculate_manhattan_distance(p1, p2)

        assert distance == expected_distance


class TestGetsCrossingClosestToStart:
    def test_gets_correct_crossing(self):
        start = (0, 0)
        crossing_coordinates = [(3, 3), (6, 5)]
        expected_crossing, expected_distance = (3, 3), 6

        crossing, distance = get_crossing_closest_to_start(start, crossing_coordinates)

        assert crossing == expected_crossing
        assert distance == expected_distance