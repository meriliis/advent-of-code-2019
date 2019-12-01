from day1.task2 import get_module_fuel_requirement, get_total_fuel_requirement


class TestGetModuleFuelRequirement:
    def test_gets_correct_fuel_requirement(self):
        module_mass = 1969
        expected_fuel_requirement = 966

        fuel_requirement = get_module_fuel_requirement(module_mass)

        assert fuel_requirement == expected_fuel_requirement

class TestGetTotalFuelRequirement:
    def test_gets_correct_total_fuel_requirement(self):
        module_masses = [14, 1969, 100756] 
        expected_fuel_requirement = 51314

        fuel_requirement = get_total_fuel_requirement(module_masses)

        assert fuel_requirement == expected_fuel_requirement

        