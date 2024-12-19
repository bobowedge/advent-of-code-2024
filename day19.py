def parse_data(data):
    patterns = set()
    designs = []
    for line in data:
        line = line.strip()
        if len(line) == 0:
            continue
        if ',' in line:
            patterns = set([x.strip() for x in line.split(",")])
        else:
            designs.append(line)
    return patterns, designs

def is_possible(design, patterns, cache):
    """
    Is this design possible with the given patterns?
    Use the cache to store previously seen designs
    """
    if len(design) == 0 or design in patterns:
        return True
    possible = cache.get(design, None)
    if possible is not None:
        return possible
    
    possible = False
    for pattern in patterns:
        if pattern == design[:len(pattern)]:
            suffix = design[len(pattern):]
            possible ^= is_possible(suffix, patterns, cache)
            if possible:
                break
    cache[design] = possible
    return possible
            
def solution1(data):
    patterns, designs = parse_data(data)
    count = 0
    cache = {}
    for design in designs:
        possible = is_possible(design, patterns, cache)
        if possible:
            count += 1
    return count

def num_ways(design, patterns, cache):
    """
    How many ways can this design be made by the patterns?
    Use a cache to store previous values
    """
    if len(design) == 0:
        return 1
    ways = cache.get(design, None)
    if ways is not None:
        return ways
    ways = 0
    for pattern in patterns:
        if pattern == design[:len(pattern)]:
            suffix = design[len(pattern):]
            ways += num_ways(suffix, patterns, cache)
    cache[design] = ways
    return ways

def solution2(data):
    patterns, designs = parse_data(data)
    count = 0
    cache = {}
    for design in designs:
        count += num_ways(design, patterns, cache)
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
