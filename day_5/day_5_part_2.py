"""
It's a completely full flight, so your seat should be the only missing boarding pass in your list. However,
there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft,
so they'll be missing from your list as well.

Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.
"""
import logging
from typing import Set, Tuple, List

from day_5.day_5_part_1 import find_seat, calculate_seat_id

logging.basicConfig(level=logging.DEBUG)

seats_seen = set()


def find_seen_seats(boarding_passes: str) -> Set[Tuple[int, int]]:
    seen_seats = set()
    for boarding_pass in boarding_passes:
        seat = find_seat(boarding_pass)
        seen_seats.add(seat)
    return seen_seats


def find_valid_seat(missing_seats: Set[Tuple[int, int]], found_seat_ids: List[int]) -> int:
    for seat_id in [calculate_seat_id(seat[0], seat[1]) for seat in missing_seats]:
        if seat_id + 1 in found_seat_ids and seat_id - 1 in found_seat_ids:
            return seat_id
        else:
            continue


def run() -> int:
    with open('day_5_input.txt', 'r') as f:
        boarding_passes = [str(value).strip('\n') for value in f.readlines()]

    total_seats = generate_all_seats()
    found_seats = find_seen_seats(boarding_passes)
    found_seat_ids = [calculate_seat_id(seat[0], seat[1]) for seat in found_seats]

    missing_seats = total_seats.difference(found_seats)
    return find_valid_seat(missing_seats, found_seat_ids)


def generate_all_seats():
    all_seats = set()
    for column in range(8):
        all_seats = all_seats.union({(row, column) for row in range(128)})
    return all_seats


if __name__ == '__main__':
    missing_seat = run()
    print(f'result: {missing_seat}')
