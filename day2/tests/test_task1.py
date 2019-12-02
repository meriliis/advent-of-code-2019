import pytest

from day2.task1 import process_opcode, run_intcode_program, restore_program


class TestProcessOpcode:
    def test_correctly_processes_opcode_1(self):
        opcode = 1
        input1 = 2
        input2 = 3
        expected_output = 5

        output = process_opcode(opcode, input1, input2)

        assert output == expected_output

    def test_correctly_processes_opcode_2(self):
        opcode = 2
        input1 = 2
        input2 = 3
        expected_output = 6

        output = process_opcode(opcode, input1, input2)

        assert output == expected_output

    def test_raises_valueerror_with_opcode_99(self):
        opcode = 99
        input1 = 2
        input2 = 3

        with pytest.raises(ValueError):
            process_opcode(opcode, input1, input2)


class TestRunIntcodeProgram:
    def test_correctly_runs_program(self):
        initial_program = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        expected_final_program = [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]

        final_program = run_intcode_program(initial_program)

        assert final_program == expected_final_program

        if expected_final_program != initial_program:
            assert initial_program != final_program


class TestRestoreProgram:
    def test_correctly_restores_program(self):
        initial_program = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        replacements = {1: 12, 2: 2}
        expected_final_program = [1, 12, 2, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        
        final_program = restore_program(initial_program, replacements)

        assert final_program == expected_final_program
        
        if expected_final_program != initial_program:
            assert initial_program != final_program