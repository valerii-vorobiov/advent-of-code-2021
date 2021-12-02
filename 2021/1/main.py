
# Author = Valerii Vorobiov
# Date = 01 December, 2021

def part_one(_input):
    measurements = [int(m) for m in _input.split()]
    return count_increasing(measurements)


def part_two(_input):
    measurements = [int(m) for m in _input.split()]
    return count_increasing(sliding_window_sum(measurements, 3))


def count_increasing(measurements):
    return sum(measurements[i - 1] < measurements[i] for i in range(1, len(measurements)))


def sliding_window_sum(measurements, window_size):
    return [sum(measurements[i:i + window_size]) for i in range(len(measurements) - window_size + 1)]


def read_input():
    with open((__file__.rstrip("main.py") + "input.txt"), 'r') as input_file:
        return input_file.read()


_input = read_input()    

print("Part One : " + str(part_one(_input)))

print("Part Two : " + str(part_two(_input)))
