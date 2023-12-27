def avoid_blizzards(valley):
    rows = len(valley)
    cols = len(valley[0])
    start_pos = None
    goal_pos = None

    # Find the positions of 'E' and the goal
    for i in range(rows):
        for j in range(cols):
            if valley[i][j] == 'E':
                start_pos = (i, j)
            elif valley[i][j] == '.':
                goal_pos = (i, j)

    # Check if 'E' and goal were found
    if 'start_pos' not in locals() or 'goal_pos' not in locals():
        raise ValueError("Starting position 'E' or goal position '.' not found in the valley map.")

    current_pos = start_pos
    minutes_taken = 0

    valley = [list(row) for row in valley]

    while True:
        update_blizzards(valley)

        if current_pos == goal_pos:
            break

        print_valley_state(valley, current_pos)

        move_direction = decide_movement(valley, current_pos, goal_pos)
        current_pos = update_your_position(move_direction, current_pos)

        minutes_taken += 1

    return minutes_taken


def update_blizzards(valley):
    for i in range(len(valley)):
        for j in range(len(valley[0])):
            if valley[i][j] in ('^', 'v', '<', '>'):
                if valley[i][j] == '^':
                    valley[i][j] = '.'
                    if i > 0:
                        valley[i - 1][j] = '^'
                elif valley[i][j] == 'v':
                    valley[i][j] = '.'
                    if i < len(valley) - 1:
                        valley[i + 1][j] = 'v'
                elif valley[i][j] == '<':
                    valley[i][j] = '.'
                    if j > 0:
                        valley[i][j - 1] = '<'
                elif valley[i][j] == '>':
                    valley[i][j] = '.'
                    if j < len(valley[0]) - 1:
                        valley[i][j + 1] = '>'


def print_valley_state(valley, current_pos):
    for i, row in enumerate(valley):
        for j, cell in enumerate(row):
            if (i, j) == current_pos:
                print('E', end='')
            else:
                print(cell, end='')
        print()
    print()


def decide_movement(valley, current_pos, goal_pos):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]  # Right, Left, Down, Up, Wait
    distances = []

    for direction in directions:
        new_pos = (current_pos[0] + direction[0], current_pos[1] + direction[1])
        if is_valid_move(valley, new_pos):
            distances.append((direction, calculate_distance(new_pos, goal_pos)))

    if distances:
        best_direction = min(distances, key=lambda x: x[1])[0]
        return best_direction
    else:
        return 0, 0


def update_your_position(move_direction, current_pos):
    return current_pos[0] + move_direction[0], current_pos[1] + move_direction[1]


def is_valid_move(valley, new_pos):
    # Check if the new position is valid (not a wall or out of bounds)
    i, j = new_pos
    return 0 <= i < len(valley) and 0 <= j < len(valley[0]) and valley[i][j] != '#'


def calculate_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


valley_map = [
    "#E######",
    "#>>.<^<#",
    "#.<..<<#",
    "#>v.><>#",
    "#<^v^^>#",
    "######.#"
]

try:
    result = avoid_blizzards(valley_map)
    print("Fewest number of minutes:", result)
except ValueError as e:
    print(e)