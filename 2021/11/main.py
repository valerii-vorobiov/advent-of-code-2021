# Author = Valerii Vorobiov
# Date = 11 December, 2021
def get_neughbours_indices(i, j):
    size = 10
    res = []
    n = 1
    for h in range(-n, n + 1, 1):
        res.extend([(i + n, j + h),
                    (i - n, j + h),
                    (i + h, j + n),
                    (i + h, j - n)])
    return set(i for i in res if all(0 <= c < size for c in i))


def part_one(_input):
    state = [[int(i) for i in j] for j in _input.split('\n')]
    return sum(main(state) for _ in range(100))


def evolutionate(i, j, state, flash, recalc):
    if state[j][i] > 9:
        state[j][i] = 0
        flash += 1
        recalc.append((i, j))
    return state, flash, recalc


def add_one(state):
    for j in range(10):
        for i in range(10):
            state[j][i] += 1
    return state


def part_two(_input):
    state = [[int(i) for i in j] for j in _input.split('\n')]
    flash = 0
    step = 0
    while flash < 100:
        step += 1
        flash = main(state)
    return step


def read_input():
    with open((__file__.rstrip("main.py") + "input.txt"), 'r') as input_file:
        return input_file.read()


def main(state):
    recaculate_stack = []
    flash = 0
    state = add_one(state)
    for j in range(10):
        for i in range(10):
            state, flash, recaculate_stack = evolutionate(i, j, state, flash, recaculate_stack)
            while recaculate_stack:
                i, j = recaculate_stack.pop(-1)
                neughbours = get_neughbours_indices(i, j)
                for ni, nj in neughbours:
                    if state[nj][ni] > 0:
                        state[nj][ni] += 1
                    state, flash, recaculate_stack = evolutionate(ni, nj, state, flash, recaculate_stack)
    return flash


_input = read_input()

print("Part One : " + str(part_one(_input)))

print("Part Two : " + str(part_two(_input)))
