import pytest
from main import avoid_blizzards, update_blizzards, decide_movement, update_your_position, is_valid_move, \
    calculate_distance, print_valley_state

valley_map = [
    "#E######",
    "#>>.<^<#",
    "#.<..<<#",
    "#>v.><>#",
    "#<^v^^>#",
    "######.#"
]


def test_avoid_blizzards():
    result = avoid_blizzards(valley_map)
    assert isinstance(result, int)
    assert result >= 0  # Ensure the result is a non-negative integer

def test_decide_movement():
    test_valley = [
        list("#.E######"),
        list("#>>.<^<#"),
        list("#.<..<<#"),
        list("#>v.><>#"),
        list("#<^v^^>#"),
        list("######.#")
    ]
    current_pos = (1, 3)
    goal_pos = (2, 5)
    result = decide_movement(test_valley, current_pos, goal_pos)
    assert result in [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]


def test_update_your_position():
    current_pos = (1, 3)
    move_direction = (0, 1)
    result = update_your_position(move_direction, current_pos)
    assert result == (1, 4)


def test_is_valid_move():
    test_valley = [
        list("#.E######"),
        list("#>>.<^<#"),
        list("#.<..<<#"),
        list("#>v.><>#"),
        list("#<^v^^>#"),
        list("######.#")
    ]
    assert is_valid_move(test_valley, (1, 3))  # Valid move
    assert not is_valid_move(test_valley, (1, 0))  # Wall, not a valid move
    assert not is_valid_move(test_valley, (6, 3))  # Out of bounds, not a valid move


def test_print_valley_state(capsys):
    valley = [
        list("#.E######"),
        list("#>>.<^<#"),
        list("#.<..<<#"),
        list("#>v.><>#"),
        list("#<^v^^>#"),
        list(list("######.#"))
    ]
    current_pos = (1, 3)
    print_valley_state(valley, current_pos)
    captured = capsys.readouterr()
    assert 'E' in captured.out  # Check if 'E' is printed


def test_calculate_distance():
    pos1 = (1, 3)
    pos2 = (4, 5)
    result = calculate_distance(pos1, pos2)
    assert result == 5  # Expected distance


if __name__ == "__main__":
    pytest.main()
