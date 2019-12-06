from day5.task1 import get_param_value, run_intcode_program


class TestGetInputValue:
    def test_gets_correct_param_value_with_position_mode(self):
        program = [1, 2, 3, 4]
        i = 1
        param_mode = '0'
        expected_param_value = 3

        param_value = get_param_value(program, i, param_mode)

        assert param_value == expected_param_value

    def test_gets_correct_param_value_with_immediate_mode(self):
        program = [1, 2, 3, 4]
        i = 1
        param_mode = '1'
        expected_param_value = 2

        param_value = get_param_value(program, i, param_mode)

        assert param_value == expected_param_value

    
class TestRunIntcodeProgram:
    def test_correctly_runs_program1(self):
        program_input = 0
        initial_program = [1101, 100, -1, 4, 0]
        expected_final_program = [1101, 100, -1, 4, 99]

        final_program = run_intcode_program(initial_program, program_input)

        assert final_program == expected_final_program

        if expected_final_program != initial_program:
            assert initial_program != final_program

    def test_correctly_runs_program2(self):
        program_input = 0
        initial_program = [1002, 4, 3, 4, 33]
        expected_final_program = [1002, 4, 3, 4, 99]

        final_program = run_intcode_program(initial_program, program_input)

        assert final_program == expected_final_program

        if expected_final_program != initial_program:
            assert initial_program != final_program