"""

"""
import logging

logging.basicConfig(level=logging.DEBUG)
LOG = logging.getLogger()


def run() -> int:
    with open('test_input.txt.txt', 'r') as f:
        lines = [str(value).strip('\n') for value in f.readlines()]
    return len(lines)


if __name__ == '__main__':
    result = run()
    print(f'result: {result}')
