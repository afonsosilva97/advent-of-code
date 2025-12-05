from operator import indexOf


def get_ingredients(input_lines):
    input_lines = input_lines.splitlines()
    blank_line_idx = indexOf(input_lines, "")

    fresh_ingredients_ranges = [
        [int(ingredient_id) for ingredient_id in line.split("-")]
        for line in input_lines[:blank_line_idx]
    ]

    available_ingredients = [int(line) for line in input_lines[blank_line_idx + 1 :]]

    return fresh_ingredients_ranges, available_ingredients


def get_answer_part_1(fresh_ingredients_ranges, available_ingredients):
    num_available_ingredients = 0

    for available_ingredient in available_ingredients:
        for fresh_ingredients_range in fresh_ingredients_ranges:
            min_id = fresh_ingredients_range[0]
            max_id = fresh_ingredients_range[1]

            if min_id <= available_ingredient <= max_id:
                num_available_ingredients += 1
                break

    return num_available_ingredients

def get_answer_part_2(fresh_ingredients_ranges):
    sorted_ranges = sorted(fresh_ingredients_ranges, key=lambda x: x[0])
    merged_ranges = [sorted_ranges[0]]

    for current_range in sorted_ranges[1:]:
        last_range = merged_ranges[-1]
        min_current_range = current_range[0]
        max_last_range = last_range[1]

        if min_current_range <= max_last_range:
            min_last_range = last_range[0]
            max_current_range = current_range[1]
            merged_ranges[-1] = [min_last_range, max(max_current_range, max_last_range)]
        else:
            merged_ranges.append(current_range)


    return sum(end - start + 1 for start, end in merged_ranges)



def run(input_lines, test_name):
    print(f"\n{test_name}")

    fresh_ingredients_ranges, available_ingredients = get_ingredients(input_lines)

    answer_part_1 = get_answer_part_1(fresh_ingredients_ranges, available_ingredients)
    print(f"answer_part_1: {answer_part_1}")

    answer_part_2 = get_answer_part_2(fresh_ingredients_ranges)
    print(f"answer_part_2: {answer_part_2}")
