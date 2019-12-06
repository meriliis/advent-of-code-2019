import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from day5.task2 import run_intcode_program


class TestRunIntcodeProgram:
    def test_correctly_runs_program1(self):
        program_input = 1
        initial_program = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
        expected_output = 0

        output = run_intcode_program(initial_program, program_input)

        assert output == expected_output

    def test_correctly_runs_program2(self):
        program_input = 1
        initial_program = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
        expected_output = 1

        output = run_intcode_program(initial_program, program_input)

        assert output == expected_output

    def test_correctly_runs_program3(self):
        program_input = 1
        initial_program = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
        expected_output = 0

        [3, 3, 1108, -1, 8, 3, 4, 3, 99]
        [3, 3, 1108, 1, 8, 3, 4, 3, 99]
        [3, 3, 1108, 0, 8, 3, 4, 3, 99]

        output = run_intcode_program(initial_program, program_input)

        assert output == expected_output

    def test_correctly_runs_program4(self):
        program_input = 1
        initial_program = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
        expected_output = 1

        output = run_intcode_program(initial_program, program_input)

        assert output == expected_output

    def test_correctly_runs_program5(self):
        program_input = 1
        initial_program = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
        expected_output = 1

        output = run_intcode_program(initial_program, program_input)

        assert output == expected_output

    def test_correctly_runs_program6(self):
        program_input = 1
        initial_program = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
        expected_output = 1

        output = run_intcode_program(initial_program, program_input)

        assert output == expected_output

    def test_correctly_runs_program7(self):
        program_input = 1
        initial_program = [
            3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31, 
            1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104, 
            999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99
        ]
        expected_output = 999

        output = run_intcode_program(initial_program, program_input)

        assert output == expected_output

#[0,  1,    2,  3, 4,  5,    6,  7,  8,   9, 10, 11, 12,   13, 14, 14,   16, 17, 18, 19, 20, 21,   22, 23,  24, 25, 26, 27,   28, 29, 30,  31,  32,   33, 34, 35,   36]
#[3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107,  8, 21, 20, 1006, 20, 31, 1106,  0, 36, 98,  0,  0, 1002, 21, 125, 20,  4, 20, 1105,  1, 46, 104, 999, 1105,  1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]
#[3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107,  8, 21, 20, 1006, 20, 31, 1106,  0, 36, 98,  1,  8, 1002, 21, 125, 20,  4, 20, 1105,  1, 46, 104, 999, 1105,  1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]