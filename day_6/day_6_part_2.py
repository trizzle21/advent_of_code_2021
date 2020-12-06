"""
--- Part Two ---
As you finish the last group's customs declaration, you notice that you misread one word in the instructions:

You don't need to identify the questions to which anyone answered "yes"; you need to identify the questions to
which everyone answered "yes"!

Using the same example as above:

abc

a
b
c

ab
ac

a
a
a
a

b
This list represents answers from five groups:

In the first group, everyone (all 1 person) answered "yes" to 3 questions: a, b, and c.
In the second group, there is no question to which everyone answered "yes".
In the third group, everyone answered yes to only 1 question, a. Since some people did not answer "yes" to b or c, they
don't count.
In the fourth group, everyone answered yes to only 1 question, a.
In the fifth group, everyone (all 1 person) answered "yes" to 1 question, b.
In this example, the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6.

For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?
"""
import logging

logging.basicConfig(level=logging.DEBUG)
LOG = logging.getLogger()


def run() -> int:
    with open('day_6_input.txt', 'r') as f:
        lines = [str(value).strip('\n') for value in f.readlines()]

    idx = 0
    common_yes_answers = 0

    common_answers = set()
    start_line = True
    while idx <= len(lines):
        if idx == len(lines) or lines[idx] == '':
            group_common_yes_answer = len(common_answers)
            common_yes_answers += group_common_yes_answer
            common_answers = set()
            start_line = True
        else:
            if start_line:
                for char in lines[idx]:
                    common_answers.add(char)
                start_line = False
            else:
                answers = set()
                for char in lines[idx]:
                    answers.add(char)
                common_answers = common_answers.intersection(answers)

        idx += 1
    return common_yes_answers


if __name__ == '__main__':
    result = run()
    print(f'result: {result}')
