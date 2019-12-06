from typing import List, Tuple
import os
from pathlib import Path


def convert_orbit_map_to_dict(orbit_map: List[str]) -> dict:
    orbit_map_dict = {}

    for orbit in orbit_map:
        orbitee, orbiter = tuple(orbit.split(')'))
        orbit_map_dict[orbiter] = orbitee

    return orbit_map_dict


def get_all_orbits(orbit_map: dict) -> int:
    all_orbits = {}
    
    orbit_dict = convert_orbit_map_to_dict(orbit_map)

    for orbiter, orbitee in orbit_dict.items():
        all_orbits[orbiter] = {orbitee}

        while True:
            orbitee = orbit_dict.get(orbitee, None)

            if not orbitee:
                break
        
            all_orbits[orbiter].add(orbitee)

    return all_orbits

def count_all_orbits(orbit_dict: dict) -> int:
    return sum(map(len, orbit_dict.values()))

    
if __name__ == '__main__':
    with open(os.path.join(Path(__file__).parent, 'orbit_map.txt')) as f:
        orbit_map = [x.strip() for x in f.readlines()]

    all_orbits = get_all_orbits(orbit_map)
    all_orbits_count = count_all_orbits(all_orbits)

    print(all_orbits_count)

