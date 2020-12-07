"""
--- Day 7: Handy Haversacks ---
You land at the regional airport in time for your next flight. In fact, it looks like you'll even have time to grab some
food: all flights are currently delayed due to issues in luggage processing.

Due to recent aviation regulations, many rules (your puzzle input) are being enforced about bags and their contents;
 bags must be color-coded and must contain specific quantities of other color-coded bags. Apparently, nobody responsible
 for these regulations considered how long they would take to enforce!

For example, consider the following rules:

light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
These rules specify the required contents for 9 bag types. In this example, every faded blue bag is empty, every vibrant
plum bag contains 11 bags (5 faded blue and 6 dotted black), and so on.

You have a shiny gold bag. If you wanted to carry it in at least one other bag, how many different bag colors would be
valid for the outermost bag? (In other words: how many colors can, eventually, contain at least one shiny gold bag?)

In the above rules, the following options would be available to you:

A bright white bag, which can hold your shiny gold bag directly.
A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
A dark orange bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold
bag.
A light red bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
So, in this example, the number of bag colors that can eventually contain at least one shiny gold bag is 4.

How many bag colors can eventually contain at least one shiny gold bag? (The list of rules is quite long; make sure you
get all of it.)
"""
from typing import Dict, List
import logging
import re

logging.basicConfig(level=logging.DEBUG)
LOG = logging.getLogger()

my_bag = 'shiny gold'
check_bag = rf'\d {my_bag}'

can_contain_bag = set()
_cannot_contain_gold = []


def _generate_rules(rules: str):
    bag_contain_rules = {}
    for rule in rules:
        tokens = rule.split(' ')
        bag_color = f'{tokens[0]} {tokens[1]}'
        contains_regex = r'\d (\w+ \w+) bag'
        bag_contain_rules[bag_color] = re.findall(contains_regex, rule)
    return bag_contain_rules


def _check_if_can_contain_my_bag(bag: str, rules: List[str], bag_rules: Dict[str, List[str]]) -> bool:
    children: List = rules
    while len(children) != 0:
        if my_bag in children:
            return True
        child = children.pop()
        child_rules = bag_rules[child]

        if child in _cannot_contain_gold:
            continue
        if child in can_contain_bag:
            return True
        elif len(child_rules) == 0:
            continue
        elif my_bag in child_rules:
            return True
        else:
            children += child_rules
    return False


def run() -> int:
    # with open('test_input.txt', 'r') as f:
    with open('day_7_input.txt', 'r') as f:
        rules = [str(value).strip('\n') for value in f.readlines()]
    print(len(rules))
    bag_rules = _generate_rules(rules)
    for bag, rule in bag_rules.items():
        if _check_if_can_contain_my_bag(bag, rule, bag_rules):
            can_contain_bag.add(bag)
        else:
            _cannot_contain_gold.append(bag)

    print(len(_cannot_contain_gold))
    return len(can_contain_bag)


if __name__ == '__main__':
    bags_that_can_contain_gold_bag = run()
    print(f'result: {bags_that_can_contain_gold_bag}')
