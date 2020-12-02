"""
The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over
from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?

"""
from typing import Tuple
import logging

logging.basicConfig(level=logging.DEBUG)




def check_values(other_inputs, target_value):
    for idx, other_value in enumerate(other_inputs):
        # other_values = other_inputs[0:idx] + other_inputs[idx + 1:len(other_inputs)]
        missing_value = target_value - other_value
        if missing_value in other_inputs:
            logging.info(f'{missing_value}, {other_value}')
            return other_value, missing_value


def iterate_(inputs):
    for idx, value in enumerate(inputs):
        other_values = inputs[0:idx] + inputs[idx+1:len(inputs)]
        target_value = 2020 - value
        result = check_values(other_values,  target_value)
        if result:
            logging.info(f'{value}, {result[0]}, {result[1]} = {value + result[0] + result[1]}')
            return value * result[0] * result[1]


def run():
    with open('day_1_input.txt', 'r') as f:
        inputs = [int(value) for value in f.readlines()]
    return iterate_(inputs)


if __name__ == '__main__':
    values: Tuple[int, int] = run()
    logging.debug(values)
