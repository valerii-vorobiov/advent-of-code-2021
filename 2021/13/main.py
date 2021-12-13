# Author = Valerii Vorobiov
# Date = 13 December, 2021

def part_one(_input):
    points = get_points(_input)
    folds = get_folds(_input)
    return len(fold(folds[0], points))


def part_two(_input):
    points = get_points(_input)
    folds = get_folds(_input)
    for f in folds:
        points = fold(f, points)
    width = max(points, key=lambda x: x[0])[0]
    height = max(points, key=lambda x: x[1])[1]
    for y in range(height + 1):
        print(''.join(['#' if tuple([x, y]) in points else ' ' for x in range(width + 1)]))


def get_points(_input):
    return set(tuple(int(i) for i in p.split(',')) for p in _input.split('\n\n')[0].split('\n'))


def get_folds(_input):
    return [p.replace('fold along ', '').split('=') for p in _input.split('\n\n')[1].split('\n')]


def fold(instruction, points):
    if instruction[0] == 'x':
        return fold_x(int(instruction[1]), points)
    return fold_y(int(instruction[1]), points)


def fold_x(lenth, points):
    points_to_change = set(point for point in points if point[0] > lenth)
    points = points - points_to_change
    changed_points = set(tuple([abs(x - (2 * lenth)), y]) for x, y in points_to_change)
    points = points.union(changed_points)
    return points


def fold_y(lenth, points):
    points_to_change = set(point for point in points if point[1] > lenth)
    points = points - points_to_change
    changed_points = set(tuple([x, abs(y - (2 * lenth))]) for x, y in points_to_change)
    points = points.union(changed_points)
    return points


def read_input():
    with open((__file__.rstrip("main.py") + "input.txt"), 'r') as input_file:
        return input_file.read()


_input = read_input()

print("Part One : " + str(part_one(_input)))

print("Part Two : " + str(part_two(_input)))
