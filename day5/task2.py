from typing import Optional, List
import os
from pathlib import Path

from task1 import get_param_value, get_output_index


def run_intcode_program(program: List[int], program_input: int) -> List[int]:
    final_program = program.copy()

    instruction_i = 0

    while True:
        instruction = str(final_program[instruction_i]).rjust(5, '0')
        opcode = instruction[-2:]
        param_modes = instruction[:-2][::-1]

        if opcode == '99':
            return final_program

        param1_i = instruction_i + 1
        param2_i = instruction_i + 2
        param3_i = instruction_i + 3

        param1_mode = param_modes[0]
        param2_mode = param_modes[1]
        param3_mode = param_modes[2]

        print(opcode, (param1_mode, param2_mode, param3_mode))

        if opcode in ['01', '02']:
            input1 = get_param_value(final_program, param1_i, param1_mode)
            input2 = get_param_value(final_program, param2_i, param2_mode)

            if opcode == '01':
                output = input1 + input2
            else:
                output = input1 * input2

            output_i = get_output_index(final_program, param3_i, param3_mode)

            print(f'Changed value {final_program[output_i]} at {output_i} to {output}')

            final_program[output_i] = output
            instruction_i += 4

        elif opcode == '03':
            output_i = get_output_index(final_program, param1_i, param1_mode)

            print(f'Changed value {final_program[output_i]} at {output_i} to {program_input}')

            final_program[output_i] = program_input
            instruction_i += 2

        elif opcode == '04':
            output_i = get_output_index(final_program, param1_i, param1_mode)
            output = final_program[output_i]

            return output
            
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

    
if __name__ == '__main__':
    with open(os.path.join(Path(__file__).parent, 'diagnostic_program.txt')) as f:
        program = [int(x) for x in f.readline().split(',')]
        
    id_of_the_system = 5
    program_output = run_intcode_program(program, id_of_the_system)

    print(program_output)