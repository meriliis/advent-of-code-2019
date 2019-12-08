from day7.task1 import run_intcode_program, run_amplifiers, find_max_output_signal

    
class TestRunIntcodeProgram:
    def test_correctly_runs_program1(self):
        program_inputs = [3, 0]
        initial_program = [3, 5, 3, 3, 99, 0]
        expected_final_program = [3, 5, 3, 0, 99, 3]
        expected_output = None
        expected_instruction_i = 4

        final_program, output, instruction_i = run_intcode_program(initial_program, program_inputs, 0)

        assert final_program == expected_final_program
        assert output == expected_output
        assert instruction_i == expected_instruction_i

        if expected_final_program != initial_program:
            assert initial_program != final_program


class TestRunAmplifiers:
    def test_returns_correct_output(self):
        program = [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]
        input_signal = 0
        phase_setting_sequence = '43210'
        expected_output = 43210

        output = run_amplifiers(program, input_signal, phase_setting_sequence)

        assert output == expected_output


class TestFindMaxOuputSignal:
    def test_returns_correct_output(self):
        program = [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]
        input_signal = 0
        possible_phase_settings = '01234'
        expected_output = 43210

        output = find_max_output_signal(program, input_signal, possible_phase_settings)

        assert output == expected_output