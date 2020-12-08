"""
After some careful analysis, you believe that exactly one instruction is corrupted.

Somewhere in the program, either a jmp is supposed to be a nop, or a nop is supposed to be a jmp. (No acc instructions
were harmed in the corruption of this boot code.)

The program is supposed to terminate by attempting to execute an instruction immediately after the last instruction in
the file. By changing exactly one jmp or nop, you can repair the boot code and make it terminate correctly.

For example, consider the same program from above:

nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
If you change the first instruction from nop +0 to jmp +0, it would create a single-instruction infinite loop, never
leaving that instruction. If you change almost any of the jmp instructions, the program will still eventually find
another jmp instruction and loop forever.

However, if you change the second-to-last instruction (from jmp -4 to nop -4), the program terminates! The instructions
are visited in this order:

nop +0  | 1
acc +1  | 2
jmp +4  | 3
acc +3  |
jmp -3  |
acc -99 |
acc +1  | 4
nop -4  | 5
acc +6  | 6
After the last instruction (acc +6), the program terminates by attempting to run the instruction below the last
instruction in the file. With this change, after the program terminates, the accumulator contains the value 8
(acc +1, acc +1, acc +6).

Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp). What is the
value of the accumulator after the program terminates?
"""
import logging
from typing import List
import copy

logging.basicConfig(level=logging.DEBUG)
LOG = logging.getLogger()

"""
nop +0
acc +1
jmp +4
"""


def operate(value):
    if value[0] == '+':
        return int(value[1:])
    else:
        return -int(value[1:])


def _will_end_next(test_idx, operations):
    return test_idx == len(operations) - 1


def _is_not_infinite_loop(operations, operations_seen, idx, accumulator):
    while idx not in operations_seen:
        operations_seen.add(idx)

        if idx == len(operations):
            return accumulator
        # print(idx)
        operation, value = operations[idx].split(' ')
        if operation == 'nop':
            idx += 1
        elif operation == 'acc':
            accumulator += operate(value)
            idx += 1
        elif operation == 'jmp':
            idx += operate(value)

    return None


def run_code(operations: List[str]):
    operations_seen = set()
    accumulator = 0
    idx = 0
    while idx != len(operations):
        operation, value = operations[idx].split(' ')
        if operation == 'nop':
            test_idx = idx + operate(value)
            is_not_loop_accumulator = _is_not_infinite_loop(operations, copy.copy(operations_seen), test_idx, copy.copy(accumulator))
            if is_not_loop_accumulator is not None:
                return is_not_loop_accumulator
            else:
                idx += 1
        elif operation == 'acc':
            accumulator += operate(value)
            idx += 1
        elif operation == 'jmp':
            test_idx = idx + 1
            is_not_loop_accumulator = _is_not_infinite_loop(operations, copy.copy(operations_seen), test_idx, copy.copy(accumulator))
            if is_not_loop_accumulator is not None:
                return is_not_loop_accumulator
            else:
                idx += operate(value)
        operations_seen.add(idx)

    return accumulator


def run() -> int:
    with open('day_8_input.txt', 'r') as f:
        lines = [str(value).strip('\n') for value in f.readlines()]

    accumulated_during_first_run = run_code(lines)
    return accumulated_during_first_run


if __name__ == '__main__':
    result = run()
    print(f'result: {result}')
