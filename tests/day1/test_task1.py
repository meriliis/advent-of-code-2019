from day1.task1 import get_module_fuel_requirement, get_total_fuel_requirement


class TestGetModuleFuelRequirement:
    def test_gets_correct_fuel_requirement(self):
        module_mass = 13
        expected_fuel_requirement = 2

        fuel_requirement = get_module_fuel_requirement(module_mass)

        assert fuel_requirement == expected_fuel_requirement

class TestGetTotalFuelRequirement:
    def test_gets_correct_total_fuel_requirement(self):
        module_masses = [12, 14, 1969, 100756] 
        expected_fuel_requirement = 34241

        fuel_requirement = get_total_fuel_requirement(module_masses)

        assert fuel_requirement == expected_fuel_requirement

        