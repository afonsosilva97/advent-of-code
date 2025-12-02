def get_valid_id_ranges(input_lines):
    lines = input_lines.splitlines()

    if len(lines) != 1:
        raise Exception(f"Invalid input ({len(lines)} lines)")

    return [[int(x) for x in item.strip().split("-")] for item in lines[0].split(",")]


def get_answer_part_1(id_ranges):
    sum_invalid_ids = 0

    for id_range in id_ranges:
        for id_value in range(id_range[0], id_range[1] + 1):
            id_str = str(id_value)
            id_len = len(id_str)

            if id_len % 2 != 0:
                continue

            position = id_len // 2
            first_half, second_half = id_str[:position], id_str[position:]

            if first_half == second_half:
                sum_invalid_ids += id_value

    return sum_invalid_ids


def get_answer_part_2(id_ranges):
    sum_invalid_ids = 0
    invalid_ids = []

    for id_range in id_ranges:
        for id_value in range(id_range[0], id_range[1] + 1):
            value_str = str(id_value)
            value_len = len(value_str)

            for pattern_split_num in range(1, value_len + 1):
                if value_len % pattern_split_num != 0:
                    continue

                for i in range(1, pattern_split_num):
                    pattern_split_size = value_len // pattern_split_num
                    position_1 = (i - 1) * pattern_split_size
                    position_2 = i * pattern_split_size
                    position_3 = (i + 1) * pattern_split_size
                    first_half, second_half = (
                        value_str[position_1:position_2],
                        value_str[position_2:position_3],
                    )

                    if first_half != second_half:
                        break

                    if i == pattern_split_num - 1:
                        sum_invalid_ids += id_value
                        invalid_ids.append(id_value)

    return sum(list(dict.fromkeys(invalid_ids)))


def run(input_lines, test_name):
    print(f"\n{test_name}")

    valid_id_ranges = get_valid_id_ranges(input_lines)

    answer_part_1 = get_answer_part_1(valid_id_ranges)
    print(f"answer_part_1: {answer_part_1}")

    answer_part_2 = get_answer_part_2(valid_id_ranges)
    print(f"answer_part_2: {answer_part_2}")
