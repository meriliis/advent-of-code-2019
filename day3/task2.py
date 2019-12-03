from typing import List, Tuple, Set
import os
from pathlib import Path

from task1 import get_wire_coordinates, get_crossing_coordinates


def calculate_steps_to_coordinate(coordinate: Tuple[int, int], wire_coordinates: List[Tuple[int, int]]) -> int:
    return wire_coordinates.index(coordinate)


def calculate_total_steps_to_coordinate(coordinate: Tuple[int, int], wire1_coordinates: List[Tuple[int, int]], wire2_coordinates: List[Tuple[int, int]]) -> int:
    return calculate_steps_to_coordinate(coordinate, wire1_coordinates) + calculate_steps_to_coordinate(coordinate, wire2_coordinates)


def get_crossing_with_least_amount_of_total_steps(start: Tuple[int, int], wire1_path: List[str], wire2_path: List[str]) -> Tuple[Tuple[int, int], int]:
    wire1_coordinates = get_wire_coordinates(start, wire1_path)
    wire2_coordinates = get_wire_coordinates(start, wire2_path)
    crossing_coordinates = list(get_crossing_coordinates(start, wire1_path, wire2_path) - {start})

    closest_crossing = crossing_coordinates[0]
    closest_distance = calculate_total_steps_to_coordinate(closest_crossing, wire1_coordinates, wire2_coordinates)
    
    for crossing in crossing_coordinates[1:]:
        distance = calculate_total_steps_to_coordinate(crossing, wire1_coordinates, wire2_coordinates)

        if distance < closest_distance:
            closest_crossing = crossing
            closest_distance = distance

    return closest_crossing, closest_distance

if __name__ == '__main__':
    with open(os.path.join(Path(__file__).parent, 'wire_paths.txt')) as f:
        wire1_path = f.readline().split(',')
        wire2_path = f.readline().split(',')

    start = (0, 0)
    closest_crossing, closest_distance = get_crossing_with_least_amount_of_total_steps(start, wire1_path, wire2_path)

    print(closest_distance)


    