from copy import deepcopy

def get_line_positions_of_char(line, char):
    char_positions = []

    for idx in range(len(line)):
        if line[idx] == char:
            char_positions.append(idx)

    return set(char_positions)

def get_answer_part_1(input_lines):
    input_lines = input_lines.splitlines()
    tachyon_positions = get_line_positions_of_char(input_lines[0], "S")
    num_splits = 0

    for line in input_lines[1:]:
        splitter_positions = get_line_positions_of_char(line, "^")
        tachyon_positions_temp = deepcopy(tachyon_positions)

        for splitter_position in splitter_positions:
            if splitter_position in tachyon_positions:
                num_splits += 1
                tachyon_positions_temp.remove(splitter_position)
                tachyon_positions_temp.add(splitter_position - 1)
                tachyon_positions_temp.add(splitter_position + 1)

        tachyon_positions = set(tachyon_positions_temp)

    return num_splits

def get_answer_part_2():
    raise NotImplementedError


def run(input_lines, test_name):
    print(f"\n{test_name}")

    answer_part_1 = get_answer_part_1(input_lines)
    print(f"answer_part_1: {answer_part_1}")

    # answer_part_2 = get_answer_part_2()
    # print(f"answer_part_2: {answer_part_2}")
