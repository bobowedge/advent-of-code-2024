def parse_data(data):
    guard_pos = (None, None)
    blocks = set()
    rows = len(data)
    cols = len(data[0])
    for row, line in enumerate(data):
        
        for col, char in enumerate(line):
            if char == "^":
                guard_pos = (row, col)
            elif char == "#":
                blocks.add((row, col))
    return guard_pos, blocks, rows, cols

def solution1(data):
    guard_pos, blocks, rows, cols = parse_data(data)
    guard_dir = (-1, 0)
    visited = set()
    while 0 <= guard_pos[0] < rows and 0 <= guard_pos[1] < cols:
        visited.add((guard_pos[0], guard_pos[1]))
        new_guard_pos = (guard_pos[0]+guard_dir[0], guard_pos[1] + guard_dir[1])
        if new_guard_pos in blocks:
            if guard_dir == (-1, 0):
                guard_dir = (0, 1)
            elif guard_dir == (0, 1):
                guard_dir = (1, 0)
            elif guard_dir == (1, 0):
                guard_dir = (0, -1)
            else:
                guard_dir = (-1, 0)
        else:
            guard_pos = new_guard_pos
    return len(visited)


def solution2(data):
    guard_init, blocks, rows, cols = parse_data(data)
    guard_pos = guard_init
    guard_dir = (-1, 0)
    visited = set()
    while 0 <= guard_pos[0] < rows and 0 <= guard_pos[1] < cols:
        visited.add(guard_pos)
        new_guard_pos = (guard_pos[0]+guard_dir[0], guard_pos[1] + guard_dir[1])
        if new_guard_pos in blocks:
            if guard_dir == (-1, 0):
                guard_dir = (0, 1)
            elif guard_dir == (0, 1):
                guard_dir = (1, 0)
            elif guard_dir == (1, 0):
                guard_dir = (0, -1)
            else:
                guard_dir = (-1, 0)
        else:
            guard_pos = new_guard_pos
    
    loops = 0
    for v in visited:
        blocks.add(v)
        guard_pos = guard_init
        guard_dir = (-1, 0)
        guard_path = set()
        guard_path.add((guard_pos, guard_dir))
        while 0 <= guard_pos[0] < rows and 0 <= guard_pos[1] < cols:
            new_guard_pos = (guard_pos[0]+guard_dir[0], guard_pos[1] + guard_dir[1])
            if new_guard_pos in blocks:
                if guard_dir == (-1, 0):
                    guard_dir = (0, 1)
                elif guard_dir == (0, 1):
                    guard_dir = (1, 0)
                elif guard_dir == (1, 0):
                    guard_dir = (0, -1)
                else:
                    guard_dir = (-1, 0)
            else:
                guard_pos = new_guard_pos
            if (guard_pos, guard_dir) in guard_path:
                loops += 1
                break
            guard_path.add((guard_pos, guard_dir))
        blocks.remove(v)
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
print(f"Solution 2: {solution2(my_data)}")
