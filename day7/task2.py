from typing import Tuple, List, Optional
import os
from pathlib import Path
from itertools import permutations

from task1 import run_intcode_program


def run_looped_amplifiers(amplifiers_states: Tuple[List[List[int]], int], input_signal: int, phase_setting_sequence: str, last_output: Optional[int] = None) -> int:
    new_states = []
    for (amplifier_state, instruction_i), phase_setting in zip(amplifiers_states, phase_setting_sequence):
        inputs = [int(phase_setting), input_signal] if last_output == None else [input_signal]
        new_amplifier_state, output_signal, new_instruction_i = run_intcode_program(amplifier_state, inputs, instruction_i)

        if output_signal is None:
            return last_output

        new_states.append((new_amplifier_state, new_instruction_i))
        input_signal = output_signal
        
    return run_looped_amplifiers(new_states, input_signal, phase_setting_sequence, input_signal)
    

def find_max_output_signal(program: List[int], input_signal: int, possible_phase_settings: str) -> int:
    n_amplifiers = len(possible_phase_settings)
    phase_setting_sequences = permutations(possible_phase_settings, n_amplifiers)

    phase_setting_sequence = next(phase_setting_sequences)
    amplifiers_states = [(program, 0)] * n_amplifiers
    max_output_signal = run_looped_amplifiers(amplifiers_states, input_signal, phase_setting_sequence)
    
    phase_setting_sequence = next(phase_setting_sequences, None)
    while phase_setting_sequence is not None:
        output_signal = run_looped_amplifiers(amplifiers_states, input_signal, phase_setting_sequence)
        max_output_signal = max(output_signal, max_output_signal)
        phase_setting_sequence = next(phase_setting_sequences, None)
        
    return max_output_signal
    
if __name__ == '__main__':
    with open(os.path.join(Path(__file__).parent, 'amplifier_controller_software.txt')) as f:
        program = [int(x) for x in f.readline().split(',')]
        
    input_signal = 0
    possible_phase_settings = '56789'
    max_output_signal = find_max_output_signal(program, input_signal, possible_phase_settings)

    print(max_output_signal)