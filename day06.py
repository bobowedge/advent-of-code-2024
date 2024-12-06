ROTATE_RIGHT = {(-1, 0) : (0, 1), (0, 1) : (1, 0), (1, 0) : (0, -1), (0, -1): (-1, 0)}

def parse_data(data):
    guard_init = (None, None)
    blocks = set()
    rows = len(data)
    cols = len(data[0])
    for row, line in enumerate(data):
        for col, char in enumerate(line):
            if char == "^":
                guard_init = (row, col)
            elif char == "#":
                blocks.add((row, col))
    return guard_init, blocks, rows, cols

def find_visited(initial_pos, initial_dir, blocks, rows, cols):
    visited = set()
    guard_position = initial_pos
    guard_direction = initial_dir
    while 0 <= guard_position[0] < rows and 0 <= guard_position[1] < cols:
        visited.add(guard_position)
        new_position = (guard_position[0] + guard_direction[0], guard_position[1] + guard_direction[1])
        if new_position in blocks:
            guard_direction = ROTATE_RIGHT[guard_direction]
        else:
            guard_position = new_position
    return visited

def solution1(data):
    init_pos, blocks, rows, cols = parse_data(data)
    init_dir = (-1, 0)
    visited = find_visited(init_pos, init_dir, blocks, rows, cols)
    return len(visited)

def solution2(data):
    # This is faster but uglier that the previous commit (14 seconds vs. 2 seconds)
    init_pos, blocks, rows, cols = parse_data(data)
    init_dir = (-1, 0)
    visited = find_visited(init_pos, init_dir, blocks, rows, cols)
    
    loops = 0
    for v in visited:
        guard_position = init_pos
        guard_direction = (-1, 0)
        guard_path = {(guard_position, guard_direction)}
        while 0 <= guard_position[0] < rows and 0 <= guard_position[1] < cols:
            if guard_direction[0] == -1:
                for row in range(guard_position[0] - 1, -1, -1):
                    p = (row, guard_position[1])
                    if p in blocks or p == v:
                        guard_position = (p[0] + 1, guard_position[1])
                        guard_direction = ROTATE_RIGHT[guard_direction]
                        break
                else:
                    guard_position = None
            elif guard_direction[0] == 1:
                for row in range(guard_position[0] + 1, rows + 1, 1):
                    p = (row, guard_position[1])
                    if p in blocks or p == v:
                        guard_position = (p[0] - 1, guard_position[1])
                        guard_direction = ROTATE_RIGHT[guard_direction]
                        break
                else:
                    guard_position = None
            elif guard_direction[1] == -1:
                for col in range(guard_position[1] - 1, -1, -1):
                    p = (guard_position[0], col)
                    if p in blocks or p == v:
                        guard_position = (guard_position[0], p[1] + 1)
                        guard_direction = ROTATE_RIGHT[guard_direction]
                        break
                else:
                    guard_position = None
            elif guard_direction[1] == 1:
                for col in range(guard_position[1] + 1, cols + 1, 1):
                    p = (guard_position[0], col)
                    if p in blocks or p == v:
                        guard_position = (guard_position[0], p[1] - 1)
                        guard_direction = ROTATE_RIGHT[guard_direction]
                        break
                else:
                    guard_position = None
            if guard_position is None:
                break
            if (guard_position, guard_direction) in guard_path:
                loops += 1
                break
            guard_path.add((guard_position, guard_direction))
    return loops
    
    
test_data = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""".splitlines()
assert(solution1(test_data) == 41)
assert(solution2(test_data) == 6)
my_data = open("data/day06.txt").read().splitlines()
print(f"Solution 1: {solution1(my_data)}")
# print(f"Solution 2: {solution2(my_data)}")

import time
t1 = time.process_time()
print(f"Solution 2: {solution2(my_data)}")
t2 = time.process_time()
print(t2 - t1)
