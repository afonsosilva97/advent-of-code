import copy
from itertools import product

MAX_ADJACENT_PAPER_ROLLS = 4
RELATIVE_ADJACENT_POSITIONS = list(product([-1, 0, 1], repeat=2))


def get_paper_roll_grid(input_lines):
    paper_rolls_lines = input_lines.splitlines()
    paper_roll_grid = []

    for line in paper_rolls_lines:
        paper_roll_row = []
        for char in line:
            if char == "@":
                paper_roll_row.append(True)
            else:
                paper_roll_row.append(False)

        paper_roll_grid.append(paper_roll_row)

    return paper_roll_grid


def get_answer_part_1(paper_roll_grid):
    count_accessible_paper_rolls = 0

    for row_idx, row in enumerate(paper_roll_grid):
        for paper_roll_idx, paper_roll in enumerate(row):

            if not paper_roll:
                continue

            count_adjacent_paper_rolls = 0

            for relative_position in RELATIVE_ADJACENT_POSITIONS:
                if relative_position == (0, 0):
                    continue

                adjacent_y = row_idx + relative_position[0]
                adjacent_x = paper_roll_idx + relative_position[1]

                if (
                    adjacent_y < 0
                    or adjacent_x < 0
                    or adjacent_y >= len(paper_roll_grid)
                    or adjacent_x >= len(row)
                ):
                    continue

                if paper_roll_grid[adjacent_y][adjacent_x]:
                    count_adjacent_paper_rolls += 1

            if count_adjacent_paper_rolls < MAX_ADJACENT_PAPER_ROLLS:
                count_accessible_paper_rolls += 1

    return count_accessible_paper_rolls


def get_answer_part_2(paper_roll_grid):
    total_accessible_paper_rolls = 0
    updated_paper_roll_grid = copy.deepcopy(paper_roll_grid)
    can_still_remove_paper_rolls = True

    while can_still_remove_paper_rolls:
        can_still_remove_paper_rolls = False
        paper_roll_grid = copy.deepcopy(updated_paper_roll_grid)

        for paper_roll_y, row in enumerate(paper_roll_grid):
            for paper_roll_x, paper_roll in enumerate(row):

                if not paper_roll:
                    continue

                count_adjacent_paper_rolls = 0

                for relative_position in RELATIVE_ADJACENT_POSITIONS:
                    if relative_position == (0, 0):
                        continue

                    adjacent_y = paper_roll_y + relative_position[0]
                    adjacent_x = paper_roll_x + relative_position[1]

                    if (
                        adjacent_y < 0
                        or adjacent_x < 0
                        or adjacent_y >= len(paper_roll_grid)
                        or adjacent_x >= len(row)
                    ):
                        continue

                    if paper_roll_grid[adjacent_y][adjacent_x]:
                        count_adjacent_paper_rolls += 1

                if count_adjacent_paper_rolls < MAX_ADJACENT_PAPER_ROLLS:
                    total_accessible_paper_rolls += 1
                    updated_paper_roll_grid[paper_roll_y][paper_roll_x] = False
                    can_still_remove_paper_rolls = True

    return total_accessible_paper_rolls


def run(input_lines, test_name):
    print(f"\n{test_name}")

    paper_roll_grid = get_paper_roll_grid(input_lines)

    answer_part_1 = get_answer_part_1(paper_roll_grid)
    print(f"answer_part_1: {answer_part_1}")

    answer_part_2 = get_answer_part_2(paper_roll_grid)
    print(f"answer_part_2: {answer_part_2}")
