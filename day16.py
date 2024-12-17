import heapq
from math import inf

ORTHOGONAL = {(1, 0), (-1, 0), (0, 1), (0, -1)}

def parse_data(data):
    walls = set()
    nodes = set()
    start = None
    end = None
    for row, line in enumerate(data):
        for col, char in enumerate(line):
            if char == "#":
                walls.add((row, col))
            elif char == "S":
                start = (row, col)
            elif char == "E":
                end = (row, col)
            else:
                nodes.add((row, col))
    return walls, start, end

def solution1(data):
    walls, start, end = parse_data(data)
    start_direction = (0, 1)

    queue = [(0, start, start_direction)]
    seen = set()
    while len(queue) > 0:
        score, point, direction = heapq.heappop(queue)
        if point == end:
            return score
        if (point, direction) in seen:
            continue
        seen.add((point, direction))
        for d in ORTHOGONAL:
            new_point = (point[0] + d[0], point[1] + d[1])
            if new_point in walls:
                continue
            if d == direction:
                heapq.heappush(queue, (score + 1, new_point, d))
            elif (d[0] == 0 and direction[0] == 0) or (d[1] == 0 and direction[1] == 0):
                continue
            else:
                heapq.heappush(queue, (score + 1001, new_point, d))
    return None


def solution2(data):
    walls, start, end = parse_data(data)
    start_direction = (0, 1)
    
    dist = {}
    dist[(start, start_direction)] = 0
    prev = {}
    queue = [(0, start, start_direction)]
    seen = set()
    while len(queue) > 0:
        score, point, direction = heapq.heappop(queue)
        if point == end:
            break
        if (point, direction) in seen:
            continue
        seen.add((point, direction))
        for d in ORTHOGONAL:
            new_pt = (point[0] + d[0], point[1] + d[1])
            if new_pt in walls:
                continue
            # Don't turn around
            if (d[0] == -direction[0] and d[1] == -direction[1]):
                continue
            
            current_score = dist.get((new_pt, d), inf)
            # Same direction
            if d == direction:
                new_score = score + 1
            # Turn 90 degrees
            else:
                new_score = score + 1000
            if new_score < current_score:
                dist[(new_pt, d)] = new_score
                prev[(new_pt, d)] = set([(point, direction)])
                heapq.heappush(queue, (new_score, new_pt, d))
            if new_score == current_score:
                prev[(new_pt, d)].add((point, direction))

    # Trace back all shortest paths
    seen = set([(start, (0, 1))])
    current = set([(end, d) for d in ORTHOGONAL])
    while len(current) > 0:
        node = current.pop()
        if node in prev:
            seen.add(node)
            for neighbor in prev.get(node):
                if neighbor not in seen:
                    current.add(neighbor)
    
    # Direction don't matter, only nodes
    nodes = set()
    for pt, d in seen:
        nodes.add(pt)
    return len(nodes)
    
test_data = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############""".splitlines()
assert(solution1(test_data) == 7036)
assert(solution2(test_data) == 45)
my_data = open("data/day16.txt").read().splitlines()
print(f"Solution 1: {solution1(my_data)}")
print(f"Solution 2: {solution2(my_data)}")
