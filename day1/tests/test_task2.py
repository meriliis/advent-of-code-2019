import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from day1.task2 import get_module_fuel_requirement


class TestGetModuleFuelRequirement:
    def test_gets_correct_fuel_requirement(self):
        module_mass = 1969
        expected_fuel_requirement = 966

        fuel_requirement = get_module_fuel_requirement(module_mass)

        assert fuel_requirement == expected_fuel_requirement