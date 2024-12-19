from functools import cache

def parse_data(data):
    patterns = None
    designs = []
    for line in data:
        line = line.strip()
        if len(line) == 0:
            continue
        if ',' in line:
            patterns = tuple([x.strip() for x in line.split(",")])
        else:
            designs.append(line)
    return patterns, designs

@cache
def is_possible(design, patterns):
    """
    Is this design possible with the given patterns?
    Use the cache to store previously seen designs
    """
    if len(design) == 0:
        return True
    
    possible = False
    for pattern in patterns:
        if pattern == design[:len(pattern)]:
            suffix = design[len(pattern):]
            possible ^= is_possible(suffix, patterns)
            if possible:
                break
    return possible
            
def solution1(data):
    patterns, designs = parse_data(data)
    count = 0
    for design in designs:
        if is_possible(design, patterns):
            count += 1
    return count

@cache
def num_ways(design, patterns):
    """
    How many ways can this design be made by the patterns?
    Use a cache to store previous values
    """
    if len(design) == 0:
        return 1
    ways = 0
    for pattern in patterns:
        if pattern == design[:len(pattern)]:
            suffix = design[len(pattern):]
            ways += num_ways(suffix, patterns)
    return ways

def solution2(data):
    patterns, designs = parse_data(data)
    count = 0
    for design in designs:
        count += num_ways(design, patterns)
    return count
    
test_data = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb""".splitlines()
assert(solution1(test_data) == 6)
assert(solution2(test_data) == 16)
my_data = open("data/day19.txt").read().splitlines()
print(f"Solution 1: {solution1(my_data)}")
print(f"Solution 2: {solution2(my_data)}")
