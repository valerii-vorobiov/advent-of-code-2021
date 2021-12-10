
# Author = Valerii Vorobiov
# Date = 10 December, 2021
from statistics import median


def part_one(_input):
    score = {
        ')': 3,
        '}': 1197,
        ']': 57,
        '>': 25137
    }
    res = []
    for line in _input.split('\n'):
        stack, error = main(line)
        if error:
            res.append(error)
    return sum(score[i] for i in res)


def part_two(_input):
    res = []
    for line in _input.split('\n'):
        stack, error = main(line)
        if stack and (not error):
            res.append(count_score_2(stack))
    return median(res)


def main(line):
    open_close = {
        '(': ')',
        '{': '}',
        '[': ']',
        '<': '>'
    }
    stack = []
    error = None
    for char in line:
        if char in open_close:
            stack.append(char)
        elif char == open_close[stack[-1]]:
            stack.pop(-1)
        else:
            error = char
            break
    return stack, error


def count_score_2(stack):
    score_map = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4
    }
    score = 0
    for i in reversed(stack):
        score *= 5
        score += score_map[i]
    return score


def read_input():
    with open((__file__.rstrip("main.py") + "input.txt"), 'r') as input_file:
        return input_file.read()


_input = read_input()    

print("Part One : " + str(part_one(_input)))

print("Part Two : " + str(part_two(_input)))

