# Author = Valerii Vorobiov
# Date = 02 December, 2021


class Position:
    def __init__(self):
        self.horisontal = 0
        self.depth = 0

    def forward(self, n):
        self.horisontal += n

    def up(self, n):
        self.depth -= n

    def down(self, n):
        self.depth += n

    def format(self):
        return self.depth * self.horisontal

    def update(self, command):
        command, n = split_command(command)
        commands = dict(forward=self.forward, up=self.up, down=self.down)
        commands[command](n)


class AimPosition(Position):
    def __init__(self):
        self.aim = 0
        super().__init__()

    def forward(self, n):
        self.horisontal += n
        self.depth += (self.aim * n)

    def up(self, n):
        self.aim -= n

    def down(self, n):
        self.aim += n


def split_command(command):
    direction, step = command.split(' ')
    return direction, int(step)


def main(position, _input):
    for move in _input.split('\n'):
        position.update(move)
    return position.format()


def part_one(_input):
    return main(Position(), _input)


def part_two(_input):
    return main(AimPosition(), _input)


def read_input():
    with open((__file__.rstrip("main.py") + "input.txt"), 'r') as input_file:
        return input_file.read()


_input = read_input()

print("Part One : " + str(part_one(_input)))

print("Part Two : " + str(part_two(_input)))
