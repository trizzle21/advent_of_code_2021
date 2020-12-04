"""
--- Day 4: Passport Processing ---
You arrive at the airport only to realize that you grabbed your North Pole Credentials instead of your passport.
While these documents are extremely similar, North Pole Credentials aren't issued by a country and therefore aren't
actually valid documentation for travel in most of the world.

It seems like you're not the only one having problems, though; a very long line has formed for the automatic passport
scanners, and the delay could upset your travel itinerary.

Due to some questionable network security, you realize you might be able to solve both of these problems at the
same time.

The automatic passport scanners are slow because they're having trouble detecting which passports have all required
fields. The expected fields are as follows:

byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
Passport data is validated in batch files (your puzzle input). Each passport is represented as a sequence of key:value
pairs separated by spaces or newlines. Passports are separated by blank lines.

Here is an example batch file containing four passports:

ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
The first passport is valid - all eight fields are present. The second passport is invalid - it is missing hgt
(the Height field).

The third passport is interesting; the only missing field is cid, so it looks like data from North Pole Credentials,
not a passport at all! Surely, nobody would mind if you made the system temporarily ignore missing cid fields.
Treat this "passport" as valid.

The fourth passport is missing two fields, cid and byr. Missing cid is fine, but missing any other field is not,
so this passport is invalid.

According to the above rules, your improved system would report 2 valid passports.

Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file,
how many passports are valid?
"""
from typing import List, Set
import logging

logging.basicConfig(level=logging.DEBUG)

VALID_PASSPORTS = [
    set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']),
    set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']),
]


def build_passport(passport_values: List[str]) -> List[str]:
    keys = []
    for line in passport_values:
        for pairs in line.split(' '):
            pair = pairs.split(':')
            keys.append(pair[0])
    return set(keys)


def validate_passport(passport_keys: Set[str]) -> bool:
    return passport_keys in VALID_PASSPORTS


def run() -> int:
    with open('day_4_input.txt', 'r') as f:
        inputs = [str(value).strip('\n') for value in f.readlines()]
    idx = 0
    valid_passport_count = 0
    passport_values = []
    while idx < len(inputs):
        if idx == len(inputs) - 1:
            passport_keys = build_passport([inputs[idx]])
            if validate_passport(passport_keys):
                valid_passport_count += 1
        elif inputs[idx] != '':
            passport_values.append(inputs[idx])
        else:
            passport_keys = build_passport(passport_values)
            if validate_passport(passport_keys):
                valid_passport_count += 1
            passport_values = []
        idx += 1
    return valid_passport_count


if __name__ == '__main__':
    valid_passports = run()
    print(f'result: {valid_passports}')
