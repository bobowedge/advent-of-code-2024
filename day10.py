def parse_data(data):
    trailheads = set()
    heights = {} 
    for row, line in enumerate(data):
        for col, char in enumerate(line):
            height = None
            if char != ".":
                height = int(char)                
                if height == 0:
                    trailheads.add((row, col))
            heights[(row, col)] = height
    return trailheads, heights

def solution1(data):
    trailheads, heights = parse_data(data)

    score = 0
    for trailhead in trailheads:
        paths = []
        paths.append(trailhead)
        peaks = set()
        while len(paths) > 0:
            location = paths.pop(-1)
            height = heights[location]
            if height == 9:
                peaks.add(location)
                continue
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_location = (location[0] + dx, location[1] + dy)
                new_height = heights.get(new_location, None)
                if new_height == height + 1:
                    paths.append(new_location)
        score += len(peaks)
    return score


def solution2(data):
    trailheads, heights = parse_data(data)

    rating = 0
    for trailhead in trailheads:    
        paths = []
        paths.append(trailhead)
        while len(paths) > 0:
            location = paths.pop(-1)
            height = heights[location]
            if height == 9:
                rating += 1
                continue
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_location = (location[0] + dx, location[1] + dy)
                new_height = heights.get(new_location, None)
                if new_height == height + 1:
                    paths.append(new_location)
    return rating
    
    
test_data = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732""".splitlines()
assert(solution1(test_data) == 36)
assert(solution2(test_data) == 81)
my_data = open("data/day10.txt").read().splitlines()
print(f"Solution 1: {solution1(my_data)}")
print(f"Solution 2: {solution2(my_data)}")
