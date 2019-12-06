from day6.task1 import convert_orbit_map_to_dict, get_all_orbits, count_all_orbits


class TestConvertOrbitMapToDict:
    def test_converts_orbit_map_to_dict(self):
        orbit_map = [
            'B)C',
            'C)D',
            'D)E'
        ]
        expected_result = {'C': 'B', 'D': 'C', 'E': 'D'}

        result = convert_orbit_map_to_dict(orbit_map)

        assert result == expected_result


class TestGetAllOrbits:
    def test_gets_all_orbits(self):
        orbit_map = [
            'B)C',
            'C)D',
            'D)E'
        ]
        expected_orbits = {
            'C': {'B'}, 
            'D': {'C', 'B'}, 
            'E': {'D', 'C', 'B'}
        }

        orbits = get_all_orbits(orbit_map)

        assert orbits == expected_orbits


class TestCountAllOrbits:
    def test_correctly_counts_all_orbits(self):
        orbit_dict = {
            'C': {'B'}, 
            'D': {'C', 'B'}, 
            'E': {'D', 'C', 'B'}
        }

        expected_orbits_count = 6

        orbits_count = count_all_orbits(orbit_dict)

        assert orbits_count == expected_orbits_count
