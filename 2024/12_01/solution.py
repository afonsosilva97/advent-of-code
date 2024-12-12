def __convert_input_to_ordered_value_list(input_lines):
    lines = input_lines.splitlines()

    array_1 = []
    array_2 = []

    for line in lines:
        num_1, num_2 = map(int, line.split())
        array_1.append(num_1)
        array_2.append(num_2)

    return array_1, array_2


def __run_part_one(array_1, array_2):
    result = 0
    array_1.sort()
    array_2.sort()

    for i in range(len(array_1)):
        result = result + abs(array_1[i] - array_2[i])

    return result


def __run_part_two(array_1, array_2):
    result = 0

    for x in array_1:
        count = 0

        for y in array_2:
            if y == x:
                count += 1

        result += x * count

    return result


def run(input_lines, test_name):
    print(f"{test_name}")

    array_1, array_2 = __convert_input_to_ordered_value_list(input_lines)

    result_part_one = __run_part_one(array_1, array_2)
    print(f"result_part_one: {result_part_one}")

    result_part_two = __run_part_two(array_1, array_2)
    print(f"result_part_two: {result_part_two}\n")
