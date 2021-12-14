# Author = Valerii Vorobiov
# Date = 14 December, 2021
from collections import Counter, defaultdict


def part_one(_input):
    template = _input.split('\n\n')[0]
    replacements = {repl.split(' -> ')[0]: repl.split(' -> ')[1] for repl in _input.split('\n\n')[1].split('\n')}
    modified_replacements = {k: v + k[1] for k, v in replacements.items()}
    for step in range(10):
        to_replace = split_to_elements(template)
        for i in range(len(to_replace)):
            to_replace[i] = modified_replacements.get(to_replace[i], to_replace[i])
        template = template[0] + ''.join(to_replace)
    c = Counter(template)
    return max(i for i in c.values()) - min(i for i in c.values())


def split_to_elements(s):
    return [s[i - 2:i] for i in range(2, len(s) + 1)]


def split_to_elements_dict(s):
    d = defaultdict(int)
    for i in range(2, len(s) + 1):
        d[s[i - 2:i]] += 1
    return d


def part_two(_input):
    template = _input.split('\n\n')[0]
    replacements = {repl.split(' -> ')[0]: repl.split(' -> ')[1] for repl in _input.split('\n\n')[1].split('\n')}
    modified_replacements = {k: (k[0] + v, v + k[1]) for k, v in replacements.items()}
    freq = defaultdict(int)
    for k in template:
        freq[k] += 1
    template = split_to_elements_dict(template)
    for day in range(40):
        for k, v in template.copy().items():
            if k in modified_replacements:
                template[k] -= v
                template[modified_replacements[k][0]] += v
                template[modified_replacements[k][1]] += v
                freq[modified_replacements[k][1][0]] += v
    return max(i for i in freq.values()) - min(i for i in freq.values())


def read_input():
    with open((__file__.rstrip("main.py") + "input.txt"), 'r') as input_file:
        return input_file.read()


_input = read_input()

print("Part One : " + str(part_one(_input)))

print("Part Two : " + str(part_two(_input)))
