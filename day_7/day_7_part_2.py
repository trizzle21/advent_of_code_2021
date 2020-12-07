"""
It's getting pretty expensive to fly these days - not because of ticket prices, but because of the ridiculous number
of bags you need to buy!

Consider again your shiny gold bag and the rules from the above example:

faded blue bags contain 0 other bags.
dotted black bags contain 0 other bags.
vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 dotted black bags.
dark olive bags contain 7 other bags: 3 faded blue bags and 4 dotted black bags.
So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags within it) plus 2 vibrant plum bags (and the
11 bags within each of those): 1 + 1*7 + 2 + 2*11 = 32 bags!

Of course, the actual rules have a small chance of going several levels deeper than this example; be sure to count all
of the bags, even if the nesting becomes topologically impractical!

Here's another example:

shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
In this example, a single shiny gold bag must contain 126 other bags.

How many individual bags are required inside your single shiny gold bag?
"""
import logging
import re
from typing import Dict, List

logging.basicConfig(level=logging.DEBUG)
LOG = logging.getLogger()

my_bag = 'shiny gold'
re_bag_with_count = r'(\d+) (\w+ \w+)'


def _generate_rules(rules: str):
    bag_contain_rules = {}
    for rule in rules:
        tokens = rule.split(' ')
        bag_color = f'{tokens[0]} {tokens[1]}'
        contains_regex = r'(\d \w+ \w+) bag'
        bag_contain_rules[bag_color] = re.findall(contains_regex, rule)
    return bag_contain_rules


def multiply_rules(rules: List[str], amount: int) -> List[str]:
    # 3 dark green, 2 -> 6 dark green
    corrected_rules = []
    for rule in rules:
        delimited = rule.split(' ')
        delimited[0] = str(int(delimited[0]) * amount)
        corrected_rules.append(' '.join(delimited))
    return corrected_rules


def _calculate_children_count(bag_rules: Dict[str, List[str]]) -> int:
    children = bag_rules[my_bag]
    total = 0
    while len(children) != 0:
        child = children.pop()
        if len(child) == 0:
            continue
        match = re.match(re_bag_with_count, child)
        if not match:
            continue

        groups = match.groups()

        total += int(groups[0])
        bag = groups[1]
        children += multiply_rules(bag_rules[bag], int(groups[0]))
    return total


def run() -> int:
    with open('day_7_input.txt', 'r') as f:
        lines = [str(value).strip('\n') for value in f.readlines()]
    bag_rules = _generate_rules(lines)
    return _calculate_children_count(bag_rules)


if __name__ == '__main__':
    total_bags = run()
    print(f'result: {total_bags}')
