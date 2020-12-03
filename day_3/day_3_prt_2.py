"""
Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.

Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left
corner and traverse the map all the way to the bottom:

Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce
the answer 336.

What do you get if you multiply together the number of trees encountered on each of the listed slopes?

"""
from collections import namedtuple
from functools import reduce  # Required in Python 3
import operator
import logging

logging.basicConfig(level=logging.DEBUG)
Position = namedtuple('Position', ['vertical', 'horizontal'])


def _check_tree_count(inputs: str, vertical_dist: int, horizontal_dist: int) -> int:
    hill_height = len(inputs) - 1
    hill_width = len(inputs[0])
    position = Position(
        vertical=vertical_dist,
        horizontal=horizontal_dist
    )
    trees: int = 0
    while position.vertical <= hill_height:
        row = inputs[position.vertical]

        if position.horizontal >= hill_width:
            horizontal = position.horizontal % hill_width
        else:
            horizontal = position.horizontal

        if row[horizontal] == '#':
            trees += 1

        position = Position(
            vertical=position.vertical + vertical_dist,
            horizontal=position.horizontal + horizontal_dist
        )

    return trees


def run() -> int:
    with open('day_3_input.txt', 'r') as f:
        inputs = [str(value).strip('\n') for value in f.readlines()]

    traversal_patterns = [
        (1, 1),
        (1, 3),
        (1, 5),
        (1, 7),
        (2, 1)
    ]
    counts = [_check_tree_count(inputs, pattern[0], pattern[1]) for pattern in traversal_patterns]
    print(counts)
    return reduce(operator.mul, counts, 1)


if __name__ == '__main__':
    tree_count = run()
    print(f'result: {tree_count}')
