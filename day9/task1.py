from typing import List
import os
from pathlib import Path
from itertools import permutations

import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))


def get_param_value(program: List[int], i: int, param_mode: str, relative_base: int) -> int:
    if param_mode == '0':
        param_i = program[i]
        param_value = program[param_i]
    elif param_mode == '1':
        param_value = program[i]
    elif param_mode == '2':
        param_i = program[i] + relative_base
        param_value = program[param_i]
    else:
        raise ValueError(f'Invalid param_mode: {param_mode}')

    return param_value


def get_output_index(program: List[int], i: int, param_mode: str, relative_base: int) -> int:
    if param_mode == '0':
        output_i = program[i]
    elif param_mode == '1':
        output_i = i
    elif param_mode == '2':
        output_i = program[i] + relative_base
    else:
        raise ValueError(f'Invalid param_mode: {param_mode}')

    return output_i


def update_value(program: List[int], output_i: int, new_value: int):
    max_i = len(program) - 1

    if output_i > max_i:
        program += [0] * (output_i - max_i)

    program[output_i] = new_value
    
    return program

def run_intcode_program(program: List[int], program_inputs: List[int], instruction_i: int) -> List[int]:
    final_program = program.copy()

    program_input_i = 0
    relative_base = 0

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
            input1 = get_param_value(final_program, param1_i, param1_mode, relative_base)
            input2 = get_param_value(final_program, param2_i, param2_mode, relative_base)

            if opcode == '01':
                output = input1 + input2
            else:
                output = input1 * input2

            output_i = get_output_index(final_program, param3_i, param3_mode, relative_base)

            final_program = update_value(final_program, output_i, output)
            instruction_i += 4

        elif opcode == '03':
            output_i = get_output_index(final_program, param1_i, param1_mode, relative_base)
            program_input = program_inputs[program_input_i]

            final_program = update_value(final_program, output_i, program_input)
            instruction_i += 2
            program_input_i += 1

        elif opcode == '04':
            output_i = get_output_index(final_program, param1_i, param1_mode, relative_base)
            output = final_program[output_i]
            instruction_i += 2

            return (final_program, output, instruction_i)
            
        elif opcode in ['05', '06', '07', '08']:
            param1 = get_param_value(final_program, param1_i, param1_mode, relative_base)
            param2 = get_param_value(final_program, param2_i, param2_mode, relative_base)
            param3 = get_output_index(final_program, param3_i, param3_mode, relative_base)

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
                    final_program = update_value(final_program, param3, 1)
                else:
                    final_program = update_value(final_program, param3, 0)

                instruction_i += 4

            elif opcode == '08':
                if param1 == param2:
                    final_program = update_value(final_program, param3, 1)
                else:
                    final_program = update_value(final_program, param3, 0)

                instruction_i += 4
        elif opcode == '09':
            param1 = get_param_value(final_program, param1_i, param1_mode, relative_base)
            relative_base += param1
            instruction_i += 2

        else:
            raise ValueError(f'Invalid opcode {opcode} at instruction {instruction_i}')

    
if __name__ == '__main__':
    with open(os.path.join(Path(__file__).parent, 'boost_program.txt')) as f:
        program = [int(x) for x in f.readline().split(',')]
      
    program_inputs = [1]
    final_program, output, _ = run_intcode_program(
        program,
        program_inputs, 
        0
    )

    print(output)