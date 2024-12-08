from collections import defaultdict
from itertools import combinations

def parse_data(data):
    freq_antennas = defaultdict(list)
    for row, line in enumerate(data):
        for col, ch in enumerate(line):
            if ch != ".":
                freq_antennas[ch].append((row, col))
    return freq_antennas, len(data), len(data[0])

def solution1(data):
    freq_antennas, rows, cols = parse_data(data)
    antinodes = set()
    for antennas in freq_antennas.values():
        for a1, a2 in combinations(antennas, 2):
            dx = a2[0] - a1[0]
            dy = a2[1] - a1[1]
            anti1 = (a1[0] - dx, a1[1] - dy)
            anti2 = (a2[0] + dx, a2[1] + dy)
            if 0 <= anti1[0] < rows and 0 <= anti1[1] < cols:
                antinodes.add(anti1)
            if 0 <= anti2[0] < rows and 0 <= anti2[1] < cols:
                antinodes.add(anti2)
    return len(antinodes)

def solution2(data):
    freq_antennas, rows, cols = parse_data(data)
    antinodes = set()
    for antennas in freq_antennas.values():
        for a1, a2 in combinations(antennas, 2):
            antinodes.add(a1)
            antinodes.add(a2)
            dx = a2[0] - a1[0]
            dy = a2[1] - a1[1]
            antix = a1[0] - dx 
            antiy = a1[1] - dy
            while 0 <= antix < rows and 0 <= antiy < cols:
                antinodes.add((antix, antiy))
                antix -= dx
                antiy -= dy
            antix = a2[0] + dx
            antiy = a2[1] + dy
            while 0 <= antix < rows and 0 <= antiy < cols:
                antinodes.add((antix, antiy))
                antix += dx
                antiy += dy                        
    return len(antinodes)

test_data = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............""".splitlines()
assert(solution1(test_data) == 14)
assert(solution2(test_data) == 34)
my_data = open("data/day08.txt").read().splitlines()
print(f"Solution 1: {solution1(my_data)}")
print(f"Solution 2: {solution2(my_data)}")
