def convert_input_lines_to_value_list(input_lines):
    lines = input_lines.splitlines()

    rotations = []

    for line in lines:
        direction, num_rotations = line[0], int(line[1:])
        rotations.append(-num_rotations if direction == "L" else num_rotations)

    return rotations


def get_answer_part_1(rotations):
    dial_pointer = 50
    number_times_dial_zero = 0

    for rotation in rotations:
        dial_pointer = (dial_pointer + rotation) % 100

        if dial_pointer == 0:
            number_times_dial_zero += 1

    return number_times_dial_zero


def get_answer_part_2(rotations):
    # I'm sure there are significantly better ways to solve this, but I'm
    # going with the naive approach due to time restrictions
    rotations_chopped = []

    for rotation in rotations:
        sign = (rotation > 0) - (rotation < 0)
        while abs(rotation) >= 1:
            rotations_chopped.append(sign)
            rotation -= sign

    return get_answer_part_1(rotations_chopped)


def run(input_lines, test_name):
    print(f"\n{test_name}")

    rotations = convert_input_lines_to_value_list(input_lines)

    answer_part_1 = get_answer_part_1(rotations)
    print(f"answer_part_1: {answer_part_1}")

    answer_part_2 = get_answer_part_2(rotations)
    print(f"answer_part_2: {answer_part_2}")
