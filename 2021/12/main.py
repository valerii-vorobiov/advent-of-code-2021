# Author = Valerii Vorobiov
# Date = 12 December, 2021
from collections import defaultdict


class Graph:
    def __init__(self, lines, end):
        self.edges = [self.from_line(line) for line in lines.split('\n')]
        self.adj = defaultdict(list)
        self.count = 0
        self.paths = set()
        for e in self.edges:
            if e[0] != end:
                self.adj[e[0]].append(e[1])
        for e in self.edges:
            if e[1] != end:
                self.adj[e[1]].append(e[0])

    @property
    def lower_vertices(self):
        return set(i for i in self.adj)

    def all_possible_path(self, start, end, path, visited):
        visited[start] += 1
        path.append(start)
        if start == end:
            self.count += 1

        neig = self.adj[start]
        for n in neig:
            if self.check_possible_way(n, visited):
                self.all_possible_path(n, end, path.copy(), visited.copy())

    def all_possible_path_2(self, start, end, path, visited, twice):
        visited[start] += 1
        path.append(start)
        if start == end:
            self.paths.add(tuple(path))

        neig = self.adj[start]
        for n in neig:
            if self.check_possible_way_2(n, visited, twice):
                self.all_possible_path_2(n, end, path.copy(), visited.copy(), twice)

    def check_possible_way(self, end, visited):
        return False if (end.islower() and end in visited) else True

    def check_possible_way_2(self, end, visited, twice):
        if end.islower() and end == twice:
            return False if visited.get(end, 0) >= 2 else True
        return False if (end.islower() and end in visited) else True

    @classmethod
    def from_line(cls, line):
        return line.split('-')


def part_one(_input):
    g = Graph(_input, 'end')
    g.all_possible_path('start', 'end', [], defaultdict(int))
    return g.count


def part_two(_input):
    g = Graph(_input, 'end')
    for i in g.lower_vertices - {'start', 'end'}:
        g.all_possible_path_2('start', 'end', [], defaultdict(int), i)
    return len(g.paths)


def read_input():
    with open((__file__.rstrip("main.py") + "input.txt"), 'r') as input_file:
        return input_file.read()


_input = read_input()

print("Part One : " + str(part_one(_input)))

print("Part Two : " + str(part_two(_input)))
