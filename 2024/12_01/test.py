import os
from solution import run


def basic_test():
    input_lines = """ 3   4
                4   3
                2   5
                1   3
                3   9
                3   3"""

    run(input_lines, basic_test.__name__)


def full_test():
    filepath = f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"
    input_lines = open(filepath).read()

    run(input_lines, full_test.__name__)


if __name__ == "__main__":
    basic_test()
    full_test()
