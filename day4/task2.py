from typing import Tuple, List
from itertools import combinations_with_replacement
import re


def find_valid_passwords(n_digits: int, valid_range: Tuple[int, int], n_adjacent_same: int) -> List[int]:
    range_min, range_max = str(valid_range[0]), str(valid_range[1])

    # Find all combinations as strings (using regex later to find ones with same adjacent digits)
    all_combinations = map(''.join, combinations_with_replacement('0123456789', n_digits))

    valid_passwords = (
        int(c) for c in all_combinations
        if not c.startswith('0') and  # remove numbers starting with 0
        (c >= range_min and c <= range_max) and  # keep numbers within range
        [m for m in list(re.finditer(f'([\\d])\\1{{{n_adjacent_same - 1},}}', c)) if len(m.group(0)) == n_adjacent_same]  # keep numbers with exactly least n_adjacent_same adjacent digits with same value
    )

    return valid_passwords


if __name__ == '__main__':
    valid_passwords = find_valid_passwords(n_digits=6, valid_range=(134564, 585159), n_adjacent_same=2)

    print(len(list(valid_passwords)))
