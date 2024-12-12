from collections import Counter

def apply_rules(stone):
    if stone == 0:
        return [1]
    strstone = str(stone)
    lenstone = len(str(stone))
    if lenstone % 2 == 1:
        return [stone * 2024]
    return [int(strstone[:lenstone//2]), int(strstone[lenstone//2:])]

def solution1(data):
    stones = [int(x) for x in data.split()]
    for blink in range(25):
        new_stones = []
        for stone in stones:
            new_stones.extend(apply_rules(stone))                
        stones = new_stones
    return len(stones)

def solution2(data):
    # Basic idea: don't apply rules to repeats, just count them
    stones = Counter()
    for x in data.split():
        stones[int(x)] += 1

    for blink in range(75):
        new_stones = Counter()
        for stone, count in stones.items():
            for new_stone in apply_rules(stone):
                new_stones[new_stone] += count
        stones = new_stones
    return sum(stones.values()) # in Python 3.10+, use stones.total()
    
test_data = "125 17"
assert(solution1(test_data) == 55312)
my_data = open("data/day11.txt").read()
print(f"Solution 1: {solution1(my_data)}")
print(f"Solution 2: {solution2(my_data)}")
