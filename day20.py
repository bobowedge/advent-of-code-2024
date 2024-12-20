import heapq
from collections import Counter
ORTHOGONAL = {(1, 0), (-1, 0), (0, 1), (0, -1)}

def parse_data(data):
    walls = set()
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
    return walls, start, end

def find_track(walls, start, end):
    """
    No Dijkstra, because there's a single path through
    """
    track = []
    current = start
    while current != end:
        track.append(current)
        for d in ORTHOGONAL:
            new_pt = (current[0] + d[0], current[1] + d[1])
            if new_pt in walls or (len(track) >= 2 and new_pt == track[-2]):
                continue
            current = new_pt
            break
    track.append(end)
    return track

def solution1(data, min_time_saved):
    walls, start, end = parse_data(data)
    track = find_track(walls, start, end)
    cheats = 0
    for idx, pt in enumerate(track):
        for d1 in ORTHOGONAL:
            collision_pt = (pt[0] + d1[0], pt[1] + d1[1])
            if collision_pt not in walls:
                continue
            for d2 in ORTHOGONAL:
                track_pt = (collision_pt[0] + d2[0], collision_pt[1] + d2[1])
                if track_pt in walls:
                    continue
                try:
                    new_idx = track.index(track_pt)
                except ValueError:
                    continue
                # (New index - old index) - 2 cheat nanoseconds
                time_saved = new_idx - idx - 2
                if time_saved >= min_time_saved:
                    cheats += 1
    return cheats

def solution2(data, min_time_saved):
    walls, start, end = parse_data(data)
    track = find_track(walls, start, end)
    cheats = 0
    for idx1, pt1 in enumerate(track[:-min_time_saved]):
        for idx2, pt2 in enumerate(track[idx1+min_time_saved:]):
            # Manhattan distance (row diff + column diff)
            manhattan = abs(pt2[0] - pt1[0]) + abs(pt2[1] - pt1[1])
            # saved_time = new_idx - old_idx - cheat_time
            # saved time = (idx2 + idx1 + min_time_saved) - idx1 - cheat time
            # saved_time = idx2 + min_time_saved  - manhattan
            # saved_time >= min_time_saved 
            # ==> idx2 >= manhattan
            # Also, need manhattan <= 20
            if manhattan <= min(idx2, 20):
                cheats += 1
    return cheats
    
test_data = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############""".splitlines()
assert(solution1(test_data, 2) == 44)
assert(solution2(test_data, 76) == 3)
assert(solution2(test_data, 74) == 7)
assert(solution2(test_data, 50) == 285)
my_data = open("data/day20.txt").read().splitlines()
print(f"Solution 1: {solution1(my_data, 100)}")
print(f"Solution 2: {solution2(my_data, 100)}")
