from typing import List
import os
from pathlib import Path


def process_opcode(opcode: int, input1: int, input2: int) -> int:
    if opcode == 1:
        output = input1 + input2
    elif opcode == 2:
        output = input1 * input2
    else:
        raise ValueError(f'Invalid opcode {opcode}')

    return output


def run_intcode_program(program: List[int]) -> List[int]:
    final_program = program.copy()

    opcode_i = 0

    while True:
        opcode = final_program[opcode_i]

        if opcode == 99:
            return final_program
        
        input1_i = final_program[opcode_i + 1]
        input2_i = final_program[opcode_i + 2]
        output_i = final_program[opcode_i + 3]

        input1 = final_program[input1_i]
        input2 = final_program[input2_i]
        output = process_opcode(opcode, input1, input2)

        final_program[output_i] = output

        opcode_i += 4


def restore_program(program: List[int], replacements: dict) -> List[int]:
    restored_program = program.copy()

    for i, replacement in replacements.items():
        restored_program[i] = replacement

    return restored_program


if __name__ == '__main__':
    with open(os.path.join(Path(__file__).parent, 'initial_program.txt')) as f:
        initial_program = [int(x) for x in f.readline().split(',')]

    restored_program = restore_program(initial_program, {1: 12, 2: 2})
    final_program = run_intcode_program(restored_program)

    print(final_program[0])