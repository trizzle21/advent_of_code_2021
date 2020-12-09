"""
--- Part Two ---
The final step in breaking the XMAS encryption relies on the invalid number you just found: you must find a contiguous
set of at least two numbers in your list which sum to the invalid number from step 1.

Again consider the above example:

35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
In this list, adding up all of the numbers from 15 through 40 produces the invalid number from step 1, 127. (Of course,
the contiguous set of numbers in your actual list might be much longer.)

To find the encryption weakness, add together the smallest and largest number in this contiguous range; in this
example, these are 15 and 47, producing 62.

What is the encryption weakness in your XMAS-encrypted list of numbers?
"""
import logging

logging.basicConfig(level=logging.DEBUG)
LOG = logging.getLogger()

input_file = 'day_9_input.txt'
INVALID_NUMBER = 32321523 if input_file != 'test_input.txt' else 127


def _find_contiguous_sum_range(lines):
    idx = 0
    while idx < len(lines):
        second_idx = idx + 1
        while second_idx < len(lines):
            total = sum(lines[idx:second_idx])
            if total > INVALID_NUMBER:
                break
            elif total == INVALID_NUMBER:
                return idx, second_idx
            else:
                second_idx += 1
        idx += 1
    raise Exception('No solution found')


def run() -> int:
    with open('day_9_input.txt', 'r') as f:
        lines = [int(value) for value in f.readlines()]
    min_idx, max_idx = _find_contiguous_sum_range(lines)
    new_range = lines[min_idx: max_idx]
    return min(new_range) + max(new_range)


if __name__ == '__main__':
    result = run()
    print(f'result: {result}')
