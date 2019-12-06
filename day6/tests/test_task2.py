import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from day6.task1 import convert_orbit_map_to_dict
from day6.task2 import get_path_to_root, find_shortest_path


class TestGetPathToRoot:
    def test_gets_correct_path(self):
        orbit_dict = {'C': 'B', 'D': 'C', 'E': 'D'}
        from_node = 'E'
        expected_path = ['E', 'D', 'C', 'B']

        path = get_path_to_root(orbit_dict, from_node)

        assert path == expected_path


class TestFindShortestPath:
    def test_finds_correct_path(self):
        orbit_map = [
            'COM)B',
            'B)C',
            'C)D',
            'D)E',
            'E)F',
            'B)G',
            'G)H',
            'D)I',
            'E)J',
            'J)K',
            'K)L',
            'K)YOU',
            'I)SAN',
        ]

        expected_path = ['YOU', 'K', 'J', 'E', 'D', 'I', 'SAN']

        path = find_shortest_path(convert_orbit_map_to_dict(orbit_map), 'YOU', 'SAN')

        assert path == expected_path