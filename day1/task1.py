from typing import List
import os
from pathlib import Path


def get_module_fuel_requirement(module_mass: int) -> int:
    fuel_requirement = module_mass // 3 - 2

    return fuel_requirement

def get_total_fuel_requirement(module_masses: List[int]) -> int:
    total_fuel_requirement = sum(map(get_module_fuel_requirement, module_masses))

    return total_fuel_requirement


if __name__ == "__main__":
    module_masses = []
    with open(os.path.join(Path(__file__).parent, 'module_masses.txt')) as f:
        for mass in f.readlines():
            module_masses.append(int(mass))

    print(get_total_fuel_requirement(module_masses))