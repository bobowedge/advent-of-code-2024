from collections import defaultdict

def parse_data(data):
    regions = defaultdict(set)
    for row, line in enumerate(data):
        for col, char in enumerate(line):
            regions[char].add((row, col))
    return regions

def area(bucket):
    return len(bucket)

def perimeter(bucket):
    length = 0
    for bx, by in bucket:
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if (bx + dx, by + dy) not in bucket:
                length += 1
    return length

def solution1(data):
    regions = parse_data(data)

    buckets = list()
    for region in regions.values():
        bucket = list()
        bucket.append(region.pop())
        while len(region) > 0:
            lenbucket = len(bucket)
            for i in range(len(bucket)):
                bx, by = bucket[i]
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_location = (bx + dx, by + dy)
                    if new_location in region:
                        region.discard(new_location)
                        bucket.append(new_location)
            if lenbucket == len(bucket):
                buckets.append(set(bucket))
                if len(region) > 0:
                    bucket = list()
                    bucket.append(region.pop())
        if len(bucket) > 0:
            buckets.append(set(bucket))
    price = 0
    for bucket in buckets:
        price += area(bucket) * perimeter(bucket)
    return price

def sides(bucket):
    sides_set = set()
    for bx, by in bucket:
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if (bx + dx, by + dy) not in bucket:
                inside = (bx, by)
                outside = (bx + dx, by + dy) 
                sides_set.add((inside, outside))
    
    bucket = list()
    bucket.append(sides_set.pop())
    sides = 0
    while len(sides_set) > 0:
        lenbucket = len(bucket)
        for i in range(lenbucket):
            inside, outside = bucket[i]
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_inside = (inside[0] + dx, inside[1] + dy)
                new_outside = (outside[0] + dx, outside[1] + dy)
                if (new_inside, new_outside) in sides_set:
                    sides_set.discard((new_inside, new_outside))
                    bucket.append((new_inside, new_outside))
        if lenbucket == len(bucket):
            sides += 1
            if len(sides_set) > 0:
                bucket = list()
                bucket.append(sides_set.pop())
    if len(bucket) > 0:
        sides += 1
    return sides

def solution2(data):
    regions = parse_data(data)

    buckets = list()
    for region in regions.values():
        bucket = list()
        bucket.append(region.pop())
        while len(region) > 0:
            lenbucket = len(bucket)
            for i in range(lenbucket):
                bx, by = bucket[i]
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_location = (bx + dx, by + dy)
                    if new_location in region:
                        region.discard(new_location)
                        bucket.append(new_location)
            if lenbucket == len(bucket):
                buckets.append(set(bucket))
                if len(region) > 0:
                    bucket = list()
                    bucket.append(region.pop())
        if len(bucket) > 0:
            buckets.append(set(bucket))

    price = 0
    for bucket in buckets:
        price += area(bucket) * sides(bucket)
    return price

    
test_data = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE""".splitlines()
# test_data = """AAAA
# BBCD
# BBCC
# EEEC""".splitlines()
assert(solution1(test_data) == 1930)
assert(solution2(test_data) == 1206)
my_data = open("data/day12.txt").read().splitlines()
print(f"Solution 1: {solution1(my_data)}")
print(f"Solution 2: {solution2(my_data)}")
