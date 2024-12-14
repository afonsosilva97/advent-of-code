def convert_input_lines_to_value_list(input_lines):
    lines = input_lines.splitlines()
    reports = []

    for line in lines:
        reports.append(list(map(int, line.split())))

    return reports


def is_level_safe(previous_level, current_level, is_order_ascending):
    return not (
        previous_level == current_level
        or (is_order_ascending and current_level < previous_level)
        or (not is_order_ascending and current_level > previous_level)
        or abs(previous_level - current_level) > 3
    )


def is_report_safe(report):
    is_order_ascending = report[1] > report[0]

    for i in range(1, len(report)):
        current_level = report[i]
        previous_level = report[i - 1]

        if not is_level_safe(previous_level, current_level, is_order_ascending):
            return False

    return True


def make_temp_report(report):
    temp_report = []

    for level in report:
        temp_report.append(level)

    return temp_report


def run_part_one(reports):
    result = len(reports)

    for report in reports:
        if not is_report_safe(report):
            result -= 1

    return result


def run_part_two(reports):
    result = len(reports)

    for report in reports:
        if is_report_safe(report):
            continue

        is_temp_report_safe = False

        for i in range(len(report)):
            temp_report = make_temp_report(report)
            del temp_report[i]
            if is_report_safe(temp_report):
                is_temp_report_safe = True
                break

        if not is_temp_report_safe:
            result -= 1

    return result


def run(input_lines, test_name):
    print(f"{test_name}")

    reports = convert_input_lines_to_value_list(input_lines)

    result_part_one = run_part_one(reports)
    print(f"result_part_one: {result_part_one}")

    result_part_two = run_part_two(reports)
    print(f"result_part_two: {result_part_two}\n")
