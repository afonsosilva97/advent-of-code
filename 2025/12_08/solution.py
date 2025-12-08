from functools import reduce
from operator import mul
import itertools

NUM_LARGEST_CIRCUITS = 3


def get_all_junction_boxes_as_circuits(input_lines):
    junction_boxes = [line.split(",") for line in input_lines.splitlines()]
    return [[[int(coordinate) for coordinate in box]] for box in junction_boxes]


def calculate_spacial_distance(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2) ** 0.5


def get_box_circuit_idx(junction_box, circuits):
    for circuit_idx, circuit in enumerate(circuits):
        if junction_box in circuit:
            return circuit_idx

    raise Exception("Box not found in circuits!")


def get_answer_part_1(circuits, num_connections):
    junction_boxes = list(itertools.chain.from_iterable(circuits))
    num_junction_boxes = len(junction_boxes)

    connections_made = []

    while num_connections > 0:
        min_distance = None
        closest_connection_boxes_idx = None

        for box1_idx in range(num_junction_boxes):
            box1 = junction_boxes[box1_idx]
            for box2_idx in range(box1_idx + 1, num_junction_boxes):
                if (
                    box1_idx == box2_idx
                    or (box1_idx, box2_idx) in connections_made
                    or (box2_idx, box1_idx) in connections_made
                ):
                    continue

                box2 = junction_boxes[box2_idx]
                distance = calculate_spacial_distance(box1, box2)

                if min_distance is None or distance < min_distance:
                    min_distance = distance
                    closest_connection_boxes_idx = (box1_idx, box2_idx)

        connections_made.append(closest_connection_boxes_idx)

        box_1_idx = closest_connection_boxes_idx[0]
        box_2_idx = closest_connection_boxes_idx[1]
        box_1_circuit_idx = get_box_circuit_idx(junction_boxes[box_1_idx], circuits)
        box_2_circuit_idx = get_box_circuit_idx(junction_boxes[box_2_idx], circuits)
        num_connections -= 1

        if box_1_circuit_idx == box_2_circuit_idx:
            continue

        circuits[box_1_circuit_idx].extend(circuits[box_2_circuit_idx])
        circuits.pop(box_2_circuit_idx)

    largest_circuits = sorted(circuits, key=lambda x: len(x), reverse=True)[
        :NUM_LARGEST_CIRCUITS
    ]

    return reduce(mul, [len(circuit) for circuit in largest_circuits])


def get_answer_part_2():
    raise NotImplementedError


def run(input_lines, test_name, num_connections):
    print(f"\n{test_name}")

    circuits = get_all_junction_boxes_as_circuits(input_lines)

    answer_part_1 = get_answer_part_1(circuits, num_connections)
    print(f"answer_part_1: {answer_part_1}")

    # answer_part_2 = get_answer_part_2()
    # print(f"answer_part_2: {answer_part_2}")
