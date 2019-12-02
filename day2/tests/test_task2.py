import pytest

import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from day2.task2 import find_inputs_for_output


class TestFindInputsForOutput:
    def test_finds_correct_inputs(self):
        initial_program = [1, 0, 0, 0, 99]
        desired_output = 4
        expected_inputs = (2, 2)

        inputs = find_inputs_for_output(initial_program, desired_output, noun_range=(0, 3), verb_range=(0, 3))

        assert inputs == expected_inputs