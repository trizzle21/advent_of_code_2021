"""
--- Day 2: Password Philosophy ---
Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers;
we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the
Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted
database) and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. The password policy indicates the lowest and highest
number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password
 must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b,
but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the
limits of their respective policies.

How many passwords are valid according to their policies?
"""
from collections import Counter
import logging

logging.basicConfig(level=logging.DEBUG)


def _check_valid_input(lower_range: int, upper_range: int, value: str, password: str):
    counter = Counter(password)

    return lower_range <= counter.get(value, 0) <= upper_range


def _extract(expression: str):
    tokenized_expression = expression.split(' ')
    return {
        'lower_range': int(tokenized_expression[0].split('-')[0]),
        'upper_range': int(tokenized_expression[0].split('-')[1]),
        'value': tokenized_expression[1][0],
        'password': tokenized_expression[2]
    }


def run() -> int:
    with open('day_2_input.txt', 'r') as f:
        inputs = [str(value).strip('\n') for value in f.readlines()]

    count = 0
    for expression in inputs:
        tokens = _extract(expression)
        if _check_valid_input(**tokens):
            count += 1
    return count


if __name__ == '__main__':
    values = run()
    logging.debug(values)