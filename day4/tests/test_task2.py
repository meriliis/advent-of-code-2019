from day4.task2 import find_valid_passwords


class TestFindValidPasswords:
    def test_finds_all_valid_passwords(self):
        n_digits = 3
        valid_range = (100, 300)
        n_adjacent_same = 2
        expected_valid_passwords = [
            112, 113, 114, 115, 116, 117, 118, 119, 
            122, 133, 144, 155, 166, 177, 188, 199, 
            223, 224, 225, 226, 227, 228, 229,
            233, 244, 255, 266, 277, 288, 299
        ]

        valid_passwords = find_valid_passwords(n_digits, valid_range, n_adjacent_same)

        assert list(valid_passwords) == expected_valid_passwords