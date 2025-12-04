def get_battery_banks(input_lines):
    battery_banks = input_lines.splitlines()

    return [[int(joltage) for joltage in bank] for bank in battery_banks]


def get_answer_part_1(battery_banks):
    total_joltage = 0

    for bank in battery_banks:
        max_joltage = max(bank)
        max_joltage_idx = bank.index(max_joltage)

        if max_joltage_idx == len(bank) - 1:
            second_max_joltage = max_joltage
            max_joltage = max(bank[:-1])
        else:
            second_max_joltage = max(bank[max_joltage_idx + 1 :])

        total_joltage += (max_joltage * 10) + second_max_joltage

    return total_joltage


def get_answer_part_2(battery_banks):
    total_joltage = 0
    num_batteries = 12

    for bank in battery_banks:
        bank_size = len(bank)
        can_skip = bank_size - num_batteries
        position = 0

        for i in range(num_batteries):
            end = min(position + can_skip + 1, bank_size)
            bank_subset = bank[position:end]
            relative_max_joltage = max(bank_subset)
            relative_max_joltage_idx = bank_subset.index(relative_max_joltage)

            total_joltage += relative_max_joltage * (10 ** (num_batteries - i - 1))
            can_skip -= relative_max_joltage_idx
            position = position + relative_max_joltage_idx + 1

    return total_joltage


def run(input_lines, test_name):
    print(f"\n{test_name}")

    battery_banks = get_battery_banks(input_lines)

    answer_part_1 = get_answer_part_1(battery_banks)
    print(f"answer_part_1: {answer_part_1}")

    answer_part_2 = get_answer_part_2(battery_banks)
    print(f"answer_part_2: {answer_part_2}")
