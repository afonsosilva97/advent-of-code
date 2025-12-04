import os
from solution import run


def test(test_name):
    filepath = f"{os.path.dirname(os.path.realpath(__file__))}/{test_name}_input.txt"
    input_lines = open(filepath).read()

    run(input_lines, test_name)


if __name__ == "__main__":
    test("basic_test")
    test("full_test")
