from typing import List
import os
from pathlib import Path

from task1 import get_total_fuel_requirement


def get_module_fuel_requirement(module_mass: int) -> int:
    fuel_requirement = module_mass // 3 - 2

    if fuel_requirement <= 0:
        return 0
    else:
        return fuel_requirement + get_module_fuel_requirement(fuel_requirement)

if __name__ == "__main__":
    module_masses = []
    with open(os.path.join(Path(__file__).parent, 'module_masses.txt')) as f:
        for mass in f.readlines():
            module_masses.append(int(mass))

    print(get_total_fuel_requirement(module_masses))