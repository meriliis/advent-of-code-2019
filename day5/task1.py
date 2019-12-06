from typing import Optional, List
import os
from pathlib import Path


def get_param_value(program: List[int], i: int, param_mode: str) -> int:
    if param_mode == '0':
        param_i = program[i]
        param_value = program[param_i]
    elif param_mode == '1':
        param_value = program[i]
    else:
        raise ValueError(f'Invalid param_mode: {param_mode}')

    return param_value

def get_output_index(program: List[int], i: int, param_mode: str) -> int:
    if param_mode == '0':
        output_i = program[i]
    elif param_mode == '1':
        output_i = i
    else:
        raise ValueError(f'Invalid param_mode: {param_mode}')

    return output_i


def run_intcode_program(program: List[int], program_input: int) -> List[int]:
    final_program = program.copy()

    instruction_i = 0

    while True:
        instruction = str(final_program[instruction_i]).rjust(5, '0')
        opcode = instruction[-2:]

        if opcode == '99':
            return final_program

        if opcode in ['01', '02']:
            param1_i = instruction_i + 1
            param2_i = instruction_i + 2

            param1_mode = instruction[-3]
            param2_mode = instruction[-4]

            input1 = get_param_value(final_program, param1_i, param1_mode)
            input2 = get_param_value(final_program, param2_i, param2_mode)

            if opcode == '01':
                output = input1 + input2
            else:
                output = input1 * input2

            output_mode = instruction[-5]
            output_i = get_output_index(final_program, instruction_i + 3, output_mode)

            print(f'Changed value {final_program[output_i]} at {output_i} to {output}')

            final_program[output_i] = output
            instruction_i += 4

        elif opcode == '03':
            output_i = get_output_index(final_program, instruction_i + 1, '0')

            print(f'Changed value {final_program[output_i]} at {output_i} to {program_input}')

            final_program[output_i] = program_input
            instruction_i += 2

        elif opcode == '04':
            output_i = get_output_index(final_program, instruction_i + 1, '0')
            output = final_program[output_i]

            print(output)
            
            instruction_i += 2

        else:
            raise ValueError(f'Invalid opcode {opcode} at instruction {instruction_i}')

    
if __name__ == '__main__':
    with open(os.path.join(Path(__file__).parent, 'diagnostic_program.txt')) as f:
        program = [int(x) for x in f.readline().split(',')]

    id_of_the_system = 1
    final_program = run_intcode_program(program, id_of_the_system)