from typing import List
import os
from pathlib import Path
from itertools import permutations

import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from day5.task1 import get_param_value, get_output_index


def run_intcode_program(program: List[int], program_inputs: List[int], instruction_i: int) -> List[int]:
    final_program = program.copy()

    program_input_i = 0

    while True:
        instruction = str(final_program[instruction_i]).rjust(5, '0')
        opcode = instruction[-2:]
        param_modes = instruction[:-2][::-1]

        if opcode == '99':
            return (final_program, None, instruction_i)

        param1_i = instruction_i + 1
        param2_i = instruction_i + 2
        param3_i = instruction_i + 3

        param1_mode = param_modes[0]
        param2_mode = param_modes[1]
        param3_mode = param_modes[2]

        if opcode in ['01', '02']:
            input1 = get_param_value(final_program, param1_i, param1_mode)
            input2 = get_param_value(final_program, param2_i, param2_mode)

            if opcode == '01':
                output = input1 + input2
            else:
                output = input1 * input2

            output_i = get_output_index(final_program, param3_i, param3_mode)

            final_program[output_i] = output
            instruction_i += 4

        elif opcode == '03':
            output_i = get_output_index(final_program, param1_i, param1_mode)
            program_input = program_inputs[program_input_i]

            final_program[output_i] = program_input
            instruction_i += 2
            program_input_i += 1

        elif opcode == '04':
            output_i = get_output_index(final_program, param1_i, param1_mode)
            output = final_program[output_i]
            instruction_i += 2

            return (final_program, output, instruction_i)
            
        elif opcode in ['05', '06', '07', '08']:
            param1 = get_param_value(final_program, param1_i, param1_mode)
            param2 = get_param_value(final_program, param2_i, param2_mode)
            param3 = get_output_index(final_program, param3_i, param3_mode)

            if opcode == '05':
                if param1 != 0:
                    instruction_i = param2
                else:
                    instruction_i += 3

            elif opcode == '06':
                if param1 == 0:
                    instruction_i = param2
                else:
                    instruction_i += 3

            elif opcode == '07':
                if param1 < param2:
                    final_program[param3] = 1
                else:
                    final_program[param3] = 0

                instruction_i += 4

            elif opcode == '08':
                if param1 == param2:
                    final_program[param3] = 1
                else:
                    final_program[param3] = 0

                instruction_i += 4

        else:
            raise ValueError(f'Invalid opcode {opcode} at instruction {instruction_i}')

    
def run_amplifiers(program: List[int], input_signal: int, phase_setting_sequence: str) -> int:
    for phase_setting in phase_setting_sequence:
        _, output_signal = run_intcode_program(program, [int(phase_setting), input_signal], 0)
        input_signal = output_signal
    
    return output_signal


def find_max_output_signal(program: List[int], input_signal: int, possible_phase_settings: str) -> int:
    phase_setting_sequences = permutations(possible_phase_settings, len(possible_phase_settings))
    max_output_signal = run_amplifiers(program, input_signal, next(phase_setting_sequences))

    next_sequence = next(phase_setting_sequences, None)
    while next_sequence:
        output_signal = run_amplifiers(program, input_signal, next_sequence)
        max_output_signal = max(output_signal, max_output_signal)
        next_sequence = next(phase_setting_sequences, None)
        
    return max_output_signal
    
if __name__ == '__main__':
    with open(os.path.join(Path(__file__).parent, 'amplifier_controller_software.txt')) as f:
        program = [int(x) for x in f.readline().split(',')]
        
    input_signal = 0
    possible_phase_settings = '01234'
    max_output_signal = find_max_output_signal(program, input_signal, possible_phase_settings)

    print(max_output_signal)