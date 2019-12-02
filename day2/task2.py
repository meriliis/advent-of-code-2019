from typing import List, Tuple
import os
from pathlib import Path

from task1 import process_opcode, run_intcode_program, restore_program


def find_inputs_for_output(program: List[int], desired_output: int, noun_range: Tuple[int, int], verb_range: Tuple[int, int]) -> Tuple[int, int]:
    for noun in range(noun_range[0], noun_range[1] + 1):
        for verb in range(verb_range[0], verb_range[1] + 1):
            restored_program = restore_program(program, {1: noun, 2: verb})
            final_program = run_intcode_program(restored_program)
            output = final_program[0]

            if output == desired_output:
                return (noun, verb)


if __name__ == '__main__':
    with open(os.path.join(Path(__file__).parent, 'initial_program.txt')) as f:
        initial_program = [int(x) for x in f.readline().split(',')]

    desired_output = 19690720
    noun, verb = find_inputs_for_output(initial_program, desired_output, noun_range=(0, 99), verb_range=(0, 99))
    
    print(100 * noun + verb)

    


    