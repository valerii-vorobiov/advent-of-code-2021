# Author = Valerii Vorobiov
# Date = 09 December, 2021
import operator
from collections import defaultdict
from functools import reduce


def part_one(_input):
    res = []
    numbers = []
    for line in _input.split('\n'):
        numbers.append([int(h) for h in line])
    for i in range(len(numbers)):
        for j in range(len(numbers[i])):
            n = get_neughbours(i, j, numbers)
            num = numbers[i][j]
            if min(n) > num:
                res.append(num + 1)
    return sum(res)


def get_neughbours(i, j, numbers):
    top = numbers[i - 1][j] if i - 1 >= 0 else None
    bottom = numbers[i + 1][j] if i + 1 < len(numbers) else None
    left = numbers[i][j - 1] if j - 1 >= 0 else None
    right = numbers[i][j + 1] if j + 1 < len(numbers[i]) else None
    return [n for n in [left, right, top, bottom] if n is not None]


def get_neughbours_2(j, i, numbers):
    top = numbers[i - 1][j] if i - 1 >= 0 else None
    bottom = numbers[i + 1][j] if i + 1 < len(numbers) else None
    left = numbers[i][j - 1] if j - 1 >= 0 else None
    right = numbers[i][j + 1] if j + 1 < len(numbers[0]) else None
    return [n for n in [left, right, top, bottom] if n is not None]


def get_neughbours_indices(i, j, numbers):
    left = (i - 1, j) if i - 1 >= 0 else None
    right = (i + 1, j) if i + 1 < len(numbers[0]) else None
    top = (i, j + 1) if j + 1 < len(numbers) else None
    bottom = (i, j - 1) if j - 1 >= 0 else None

    return [n for n in [left, right, top, bottom] if n is not None]


def part_two(_input):
    low_res = []
    numbers = []
    for line in _input.split('\n'):
        numbers.append([int(h) for h in line])
    lenth = len(numbers)
    for i in range(lenth):
        height = len(numbers[i])
        for j in range(height):
            n = get_neughbours(i, j, numbers)
            num = numbers[i][j]
            if min(n) > num:
                low_res.append((j, i))

    res = low_res.copy()
    d = defaultdict(list)
    for point in low_res:
        d[point].append(point)

        neughbours = get_neughbours_indices(i=point[0],
                                              j=point[1],
                                              numbers=numbers)
        neughbours = verify_neughbours(neughbours, lenth, height, numbers, res)
        res.extend(neughbours)
        d[point].extend(neughbours)
        while neughbours:
            p = neughbours.pop()
            neig = get_neughbours_indices(i=p[0],
                                          j=p[1],
                                          numbers=numbers)
            neig = verify_neughbours(neig, lenth, height, numbers, res)
            neughbours.extend(neig)
            res.extend(neig)
            d[point].extend(neig)
    basins_size = sorted([len(v)for v in d.values()], reverse=True)
    return reduce(operator.mul, basins_size[:3], 1)

def have_downward_neughbour(point, numbers):
    i, j = point
    neughbours = get_neughbours_2(i, j, numbers)
    num = numbers[j][i]
    return min(neughbours) < num


def add_neughbours(n, point):
    i, j = point
    res = []
    for h in range(-n, n + 1, 1):
        res.extend([(i + n, j + h),
                    (i - n, j + h),
                    (i + h, j + n),
                    (i + h, j - n)])
    return set(res)


def verify_neughbours(neughbours, le, h, numbers, res):
    neughbours = [neughbour for neughbour in neughbours
                  if (0 <= neughbour[0] < h and 0 <= neughbour[1] < le)]
    neughbours = [neughbour for neughbour in neughbours if neughbour not in res]
    neughbours = [neughbour for neughbour in neughbours if numbers[neughbour[1]][neughbour[0]] < 9]
    neughbours = [neughbour for neughbour in neughbours if have_downward_neughbour(neughbour, numbers)]
    return neughbours


def read_input():
    with open((__file__.rstrip("main.py") + "input.txt"), 'r') as input_file:
        return input_file.read()


_input = read_input()

print("Part One : " + str(part_one(_input)))

print("Part Two : " + str(part_two(_input)))
