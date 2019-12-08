import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from day7.task2 import run_looped_amplifiers


class TestRunAmplifiers:
    def test_returns_correct_output(self):
        amplifiers_states = [[3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26, 27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99, 0, 0, 5]] * 5
        input_signal = 0
        phase_setting_sequence = '98765'
        expected_output = 139629729

        output = run_looped_amplifiers(amplifiers_states, input_signal, phase_setting_sequence)

        assert output == expected_output