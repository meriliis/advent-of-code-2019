from typing import List
import os
from pathlib import Path

from task1 import convert_orbit_map_to_dict, get_all_orbits


def get_path_to_root(orbit_dict: dict, from_node: str) -> List[str]:
    current_path = [from_node]

    while True:
        from_node = orbit_dict.get(from_node, None)

        if not from_node:
            break
            
        current_path.append(from_node)

    return current_path


def find_shortest_path(orbit_dict: dict, from_node: str, to_node: str) -> List[str]:
    path1 = get_path_to_root(orbit_dict, from_node)
    path2 = get_path_to_root(orbit_dict, to_node)

    current_path = []

    for node in path1:
        current_path.append(node)
        if node in path2:
            common_node_i = path2.index(node)
            break

    current_path += path2[:common_node_i][::-1]

    return current_path


if __name__ == '__main__':
    with open(os.path.join(Path(__file__).parent, 'orbit_map.txt')) as f:
        orbit_map = [x.strip() for x in f.readlines()]

    orbit_dict = convert_orbit_map_to_dict(orbit_map)

    shortest_path = find_shortest_path(orbit_dict, orbit_dict['YOU'], orbit_dict['SAN'])

    print(len(shortest_path) - 1)
