from day_7.day_7_part_2 import _calculate_children_count, _generate_rules


def test_calculate_test_input_returns_correct():
    # assert
    with open('../test_input.txt', 'r') as f:
        lines = [str(value).strip('\n') for value in f.readlines()]
    bag_rules = _generate_rules(lines)
    # act
    count = _calculate_children_count(bag_rules)

    # assert
    assert count == 32


def test_calculate_test_input_part_2_returns_correct():
    # assert
    with open('../test_input_part_2.txt', 'r') as f:
        lines = [str(value).strip('\n') for value in f.readlines()]
    bag_rules = _generate_rules(lines)
    # act
    count = _calculate_children_count(bag_rules)

    # assert
    assert count == 126
