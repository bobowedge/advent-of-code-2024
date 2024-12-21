from collections import defaultdict
import heapq

ORTHOGONAL = {(1, 0), (-1, 0), (0, 1), (0, -1)}

numeric_keypad = {
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

directional_keypad = {
    (0, 1): '^',
    (0, 2): 'A',
    (1, 0): '<',
    (1, 1): 'v',
    (1, 2): '>',
}

def dijkstra(start, padset):
    queue = [(0, start)]
    seen = set()
    dist = {}
    prev = defaultdict(set)
    for pt in padset:
        dist[pt] = 25
    dist[start] = 0
    while len(queue) > 0:
        length, point = heapq.heappop(queue)
        if point in seen:
            continue
        seen.add(point)
        for d in ORTHOGONAL:
            px = point[0] + d[0]
            py = point[1] + d[1]
            new_point = (px, py)
            if new_point not in padset:
                continue
            alt = length + 1
            if alt < dist[new_point]:
                heapq.heappush(queue, (alt, new_point))
                dist[new_point] = alt
                prev[new_point] = set([point])
            if alt == dist[new_point]:
                prev[new_point].add(point)
    return dist, prev

def build_numeric_keypad_map():
    padset = [(row, col) for row in range(4) for col in range(3)]
    padset.remove((3, 0))

    paths = []
    for pt1 in padset:
        distances, points = dijkstra(pt1, padset)
        for pt2 in padset:
            if pt1 == pt2:
                continue
            queue = [[pt2]]
            while len(queue) > 0:
                path = queue.pop()
                if len(path) > distances[pt2] + 1:
                    continue
                if path[-1] == pt1:
                    paths.append(tuple(path))
                else:
                    for pt in points[path[-1]]:
                        new_path = path + [pt]
                        queue.append(new_path)

    numeric_keypad_map = defaultdict(set)
    for path in paths:
        val1 = numeric_keypad[path[0]]
        val2 = numeric_keypad[path[-1]]
        pathstr = ""
        for (x1, y1), (x2, y2) in zip(path[:-1], path[1:]):
            drow = x2 - x1
            dcol = y2 - y1
            if drow == -1:
                pathstr += "^"
            elif drow == 1:
                pathstr += "v"
            elif dcol == -1:
                pathstr += "<"
            else:
                pathstr += ">"
        numeric_keypad_map[(val1, val2)].add(pathstr)
    
    for key in "A0123456789":
        numeric_keypad_map[(key, key)] = set([""])

    return numeric_keypad_map

def build_directional_keypad_map():
    padset = [(0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]

    paths = []
    for pt1 in padset:
        distances, points = dijkstra(pt1, padset)
        for pt2 in padset:
            if pt1 == pt2:
                continue
            queue = [[pt2]]
            while len(queue) > 0:
                path = queue.pop()
                if len(path) > distances[pt2] + 1:
                    continue
                if path[-1] == pt1:
                    paths.append(tuple(path))
                else:
                    for pt in points[path[-1]]:
                        new_path = path + [pt]
                        queue.append(new_path)

    directional_keypad_map = defaultdict(set)
    for path in paths:
        val1 = directional_keypad[path[0]]
        val2 = directional_keypad[path[-1]]
        pathstr = ""
        for (x1, y1), (x2, y2) in zip(path[:-1], path[1:]):
            drow = x2 - x1
            dcol = y2 - y1
            if drow == -1:
                pathstr += "^"
            elif drow == 1:
                pathstr += "v"
            elif dcol == -1:
                pathstr += "<"
            else:
                pathstr += ">"
        directional_keypad_map[(val1, val2)].add(pathstr)
    
    for key in "v^<>A":
        directional_keypad_map[(key, key)] = set([""])
    
    return directional_keypad_map

def next_subpaths(path, key_map):
    subpaths = []
    for edge in key_map[("A", path[0])]:
        subpaths.append(edge + "A")
    for keys in zip(path[:-1], path[1:]):
        new_subpaths = []
        for subpath in subpaths:
            for value in key_map[keys]:
                new_subpaths.append(subpath + value + "A")
        subpaths = list(new_subpaths)
    return subpaths

def next_paths(paths, key_map):
    new_paths = []
    for path in paths:
        new_paths += next_subpaths(path, key_map)
    return new_paths

def trim_paths(paths):
    minlen = min([len(path) for path in paths])
    return [path for path in paths if len(path) == minlen]

def solution1(data):
    numkey_map = build_numeric_keypad_map()
    dirkey_map = build_directional_keypad_map()

    complexity = 0
    for code in data:
        paths = next_paths([code], numkey_map)
        paths = trim_paths(paths)
        for i in range(1):
            paths = next_paths(paths, dirkey_map)
            paths = trim_paths(paths)
        paths = next_paths(paths, dirkey_map)

        shortest = min([len(path) for path in paths])
        numeric = int(code[:-1])
        complexity += shortest * numeric
    return complexity


def solution2(data):
    numkey_map = build_numeric_keypad_map()
    dirkey_map = build_directional_keypad_map()

    complexity = 0
    for code in data:
        paths = next_paths([code], numkey_map)
        paths = trim_paths(paths)
        for i in range(24):
            paths = next_paths(paths, dirkey_map)
            paths = trim_paths(paths)
        paths = next_paths(paths, dirkey_map)
        
        shortest = min([len(path) for path in paths])
        numeric = int(code[:-1])
        complexity += shortest * numeric
    return complexity
    
    
test_data = """029A
980A
179A
456A
379A""".splitlines()
assert(solution1(test_data) == 126384)
# assert(solution2(test_data) == 0)
my_data = open("data/day21.txt").read().splitlines()
print(f"Solution 1: {solution1(my_data)}")
print(f"Solution 2: {solution2(my_data)}")
