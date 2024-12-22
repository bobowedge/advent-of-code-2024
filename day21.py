from collections import defaultdict
from functools import cache
import heapq

DIRECTIONS = {(1, 0): 'v', (-1, 0): '^', (0, 1): '>', (0, -1): '<'}

NUMPAD = {
    (0, 0): '7',
    (0, 1): '8',
    (0, 2): '9',
    (1, 0): '4',
    (1, 1): '5',
    (1, 2): '6',
    (2, 0): '1',
    (2, 1): '2',
    (2, 2): '3',
    (3, 1): '0',
    (3, 2): 'A',
}
NUMPAD.update({value: key for key, value in NUMPAD.items()})

DPAD = {
    (0, 1): '^',
    (0, 2): 'A',
    (1, 0): '<',
    (1, 1): 'v',
    (1, 2): '>',
}
DPAD.update({value: key for key, value in DPAD.items()})

def dijkstra(source, target, keypad):
    start = keypad[source]
    end = keypad[target]
    queue = [(0, start)]
    seen = set()
    dist = {}
    prev = defaultdict(set)
    for pt in keypad:
        dist[pt] = 25
    dist[start] = 0
    while len(queue) > 0:
        length, point = heapq.heappop(queue)
        if point == end:
            break
        if point in seen:
            continue
        seen.add(point)
        for d in DIRECTIONS:
            px = point[0] + d[0]
            py = point[1] + d[1]
            new_point = (px, py)
            if new_point not in keypad:
                continue
            alt = length + 1
            if alt < dist[new_point]:
                heapq.heappush(queue, (alt, new_point))
                dist[new_point] = alt
                prev[new_point] = set([point])
            if alt == dist[new_point]:
                prev[new_point].add(point)
    paths = []
    queue = [[end]]
    while len(queue) > 0:
        path = queue.pop()
        if len(path) > dist[end] + 1:
            continue
        if path[-1] == start:
            path.reverse()
            paths.append(tuple(path))
        else:
            for pt in prev[path[-1]]:
                new_path = path + [pt]
                queue.append(new_path)

    dpaths = []
    for path in paths:
        dpath = ""
        for pt1, pt2 in zip(path[:-1], path[1:]):
            d1 = pt2[0] - pt1[0]
            d2 = pt2[1] - pt1[1]
            dpath += DIRECTIONS[(d1, d2)]
        dpath += "A"
        dpaths.append(dpath)
    return dpaths

@cache
def cost_dpad(source: str, target: str, N: int, last: int):
    if N == last:
        return 1
    else:
        best = None
        for path in dijkstra(source, target, DPAD):
            length = 0
            current = 'A'
            for point in path:
                length += cost_dpad(current, point, N + 1, last)
                current = point
            if best is None or length < best:
                best = length
        return best

def cost_numpad(source: str, target: str, last: int):
    best = None
    for path in dijkstra(source, target, NUMPAD):
        length = 0
        current = 'A'
        for point in path:
            length += cost_dpad(current, point, 1, last)
            current = point
        if best is None or length < best:
            best = length
    return best

def solution1(data):
    complexity = 0
    for code in data:
        shortest = 0
        Acode = 'A' + code
        for key1, key2 in zip(Acode[:-1], Acode[1:]):
            shortest += cost_numpad(key1, key2, 3)
        numeric = int(code[:-1])
        complexity += shortest * numeric
    return complexity

def solution2(data):
    complexity = 0
    for code in data:
        shortest = 0
        Acode = 'A' + code
        for key1, key2 in zip(Acode[:-1], Acode[1:]):
            shortest += cost_numpad(key1, key2, 26)
        numeric = int(code[:-1])
        complexity += shortest * numeric
    return complexity

test_data = """029A
980A
179A
456A
379A""".splitlines()
assert(solution1(test_data) == 126384)
my_data = open("data/day21.txt").read().splitlines()
print(f"Solution 1: {solution1(my_data)}")
print(f"Solution 2: {solution2(my_data)}")
