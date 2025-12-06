def get_math_problems(input_lines):
    input_lines = input_lines.splitlines()

    return [[value for value in line.split()] for line in input_lines]


def get_answer_part_1(math_problems):
    num_rows = len(math_problems)
    num_cols = len(math_problems[0])
    total = 0

    for col_idx in range(num_cols):
        operator = math_problems[-1][col_idx]
        subtotal = int(math_problems[0][col_idx])
        for row_idx in range(1, num_rows - 1):
            if operator == "+":
                subtotal += int(math_problems[row_idx][col_idx])
            elif operator == "*":
                subtotal *= int(math_problems[row_idx][col_idx])
            else:
                raise Exception(f"Unknown operator {operator}")

        total += subtotal

    return total


def get_answer_part_2(input_lines):
    input_lines = input_lines.splitlines()
    num_rows = len(input_lines)
    num_cols_per_row = [len(row) for row in input_lines]
    max_num_cols = max(num_cols_per_row)
    num_operations = len(input_lines[-1].split())

    total = 0
    col_idx = max_num_cols - 1
    operation_idx = num_operations - 1
    operation_values = []

    while operation_idx >= 0:
        col_value = ""
        operator = ""

        for row_idx in range(num_rows):
            if len(input_lines[row_idx]) <= col_idx:
                continue

            char = input_lines[row_idx][col_idx]

            if char.isspace():
                continue

            if row_idx == num_rows - 1:
                operator = char
                break

            col_value += char

        if col_value:
            operation_values.append(int(col_value))

        if operator:
            operation_idx -= 1
            subtotal = operation_values[0]
            for value in operation_values[1:]:
                if operator == "+":
                    subtotal += value
                elif operator == "*":
                    subtotal *= value
                else:
                    raise Exception(f"Unknown operator {operator}")

            total += subtotal

            operation_values = []

        col_idx -= 1

    return total


def run(input_lines, test_name):
    print(f"\n{test_name}")

    math_problems = get_math_problems(input_lines)

    answer_part_1 = get_answer_part_1(math_problems)
    print(f"answer_part_1: {answer_part_1}")

    answer_part_2 = get_answer_part_2(input_lines)
    print(f"answer_part_2: {answer_part_2}")
