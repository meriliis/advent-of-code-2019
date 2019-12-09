from day9.task1 import run_intcode_program


class TestRunIntcodeProgram:
    def test_returns_correct_output1(self):
        program = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
        program_inputs = []
        instruction_i = 0
        expected_final_program = program

        final_program, _, _ = run_intcode_program(program, program_inputs, instruction_i)

        assert final_program == expected_final_program


    def test_returns_correct_output2(self):
        program = [1102, 34915192, 34915192, 7, 4, 7, 99, 0]
        program_inputs = []
        instruction_i = 0
        expected_output_length = 16

        _, output, _ = run_intcode_program(program, program_inputs, instruction_i)

        assert len(str(output)) == expected_output_length

    def test_returns_correct_output3(self):
        program = [104, 1125899906842624, 99]
        program_inputs = []
        instruction_i = 0
        expected_output = 1125899906842624

        _, output, _ = run_intcode_program(program, program_inputs, instruction_i)

        assert output == expected_output

