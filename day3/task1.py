from typing import List, Tuple, Set
import os
from pathlib import Path


def get_line_coordinates(start: Tuple[int, int], direction: str, steps: int) -> List[Tuple[int, int]]:
    coordinates = [start]

    for _ in range(steps):
        last_x, last_y = coordinates[-1]

        if direction == 'L':
            new_x, new_y = (last_x - 1, last_y)
        elif direction == 'R':
            new_x, new_y = (last_x + 1, last_y)
        elif direction == 'U':
            new_x, new_y = (last_x, last_y + 1)
        elif direction == 'D':
            new_x, new_y = (last_x, last_y - 1)
        else:
            raise ValueError('Invalid direction {direction}')

        coordinates.append((new_x, new_y))

    return coordinates


def get_wire_coordinates(start: Tuple[int, int], wire_path: List[str]) -> List[Tuple[int, int]]:
    coordinates = [start]

    for line in wire_path:
        start = coordinates[-1]
        direction = line[0]
        steps = int(line[1:])

        line_coordinates = get_line_coordinates(start, direction, steps)

        coordinates += line_coordinates[1:]

    return coordinates


def get_crossing_coordinates(start: Tuple[int, int], wire1_path: List[str], wire2_path: List[str]) -> Set[Tuple[int, int]]:
    wire1_coordinates = get_wire_coordinates(start, wire1_path)
    wire2_coordinates = get_wire_coordinates(start, wire2_path)

    crossing_coordinates = set.intersection(set(wire1_coordinates), set(wire2_coordinates))

    return crossing_coordinates


def calculate_manhattan_distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
    manhattan_distance = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    return manhattan_distance

def get_crossing_closest_to_start(start: Tuple[int, int], crossing_coordinates: List[Tuple[int, int]]) -> Tuple[Tuple[int, int], int]:
    closest_crossing = crossing_coordinates[0]
    closest_distance = calculate_manhattan_distance(start, closest_crossing)
    
    for crossing in crossing_coordinates[1:]:
        distance = calculate_manhattan_distance(start, crossing)

        if distance < closest_distance:
            closest_crossing = crossing
            closest_distance = distance

    return closest_crossing, closest_distance

if __name__ == '__main__':
    with open(os.path.join(Path(__file__).parent, 'wire_paths.txt')) as f:
        wire1_path = f.readline().split(',')
        wire2_path = f.readline().split(',')

    start = (0, 0)
    crossing_coordinates = get_crossing_coordinates(start, wire1_path, wire2_path) - {start}
    closest_crossing, distance = get_crossing_closest_to_start(start, list(crossing_coordinates))

    print(distance)


    