# Author = Valerii Vorobiov
# Date = 04 December, 2021
import re
from collections import defaultdict


class Board:
    def __init__(self, line):
        self.board_size = 5
        self.line = line
        self.match = set()
        self.horisontal_match = defaultdict(set)
        self.vertical_match = defaultdict(set)
        self._skip = False

    def check(self, value):
        if self._skip:
            return
        if value in self.line:
            self.match.add(value)
            self.horisontal_match[self.line.index(value) // self.board_size].add(
                self.line.index(value) % self.board_size)
            self.vertical_match[self.line.index(value) % self.board_size].add(self.line.index(value) // self.board_size)
            if (max(len(i) for i in self.horisontal_match.values()) == self.board_size
                    or max(len(i) for i in self.vertical_match.values()) == self.board_size):
                return int(value) * self.unmarked_sum()

    def skip(self):
        self._skip = True

    def unmarked_sum(self):
        return sum(int(i) for i in set(self.line) - self.match)


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def create_boards(_input):
    boards = [Board(re.findall(r'\d+', board))
              for board in _input.split('\n\n')[1:]]
    return boards


def part_one(_input):
    steps = _input.split()[0].split(',')
    boards = create_boards(_input)
    for step in steps:
        for board in boards:
            score = board.check(step)
            if score:
                return score


def part_two(_input):
    steps = _input.split()[0].split(',')
    boards = create_boards(_input)
    skip_wins = len(boards)
    for step in steps:
        for board in boards:
            score = board.check(step)
            if score:
                board.skip()
                skip_wins -= 1
                if not skip_wins:
                    return score


def read_input():
    with open((__file__.rstrip("main.py") + "input.txt"), 'r') as input_file:
        return input_file.read()


_input = read_input()

print("Part One : " + str(part_one(_input)))

print("Part Two : " + str(part_two(_input)))
