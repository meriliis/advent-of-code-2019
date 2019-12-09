import os
from pathlib import Path

import sys
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from day9.task1 import run_intcode_program


if __name__ == '__main__':
    with open(os.path.join(Path(__file__).parent, 'boost_program.txt')) as f:
        program = [int(x) for x in f.readline().split(',')]
      
    program_inputs = [2]
    final_program, output, _ = run_intcode_program(
        program,
        program_inputs, 
        0
    )

    print(output)