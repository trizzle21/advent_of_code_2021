"""
While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan
Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job
at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second
character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!)
Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant
for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
How many passwords are valid according to the new interpretation of the policies?

"""
import logging

logging.basicConfig(level=logging.DEBUG)


def _check_valid_input(lower_range: int, upper_range: int, value: str, password: str):
    lower_pos: bool = password[lower_range] == value
    upper_bos: bool = password[upper_range] == value
    # (True, False) or (False, True)
    # FALSE and FALSE is True
    if lower_pos and upper_bos:
        return False
    elif not (lower_pos or upper_bos):
        return False
    else:
        return True


def _extract(expression: str):
    tokenized_expression = expression.split(' ')
    return {
        'lower_range': int(tokenized_expression[0].split('-')[0]) - 1,
        'upper_range': int(tokenized_expression[0].split('-')[1]) - 1,
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
    logging.info(f'result: {values}')
