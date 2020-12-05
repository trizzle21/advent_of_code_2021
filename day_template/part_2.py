"""

"""
import logging

logging.basicConfig(level=logging.DEBUG)
LOG = logging.getLogger()


def run() -> int:
    with open('input.txt', 'r') as f:
        lines = [str(value).strip('\n') for value in f.readlines()]
    return len(lines)


if __name__ == '__main__':
    missing_seat = run()
    print(f'result: {missing_seat}')
