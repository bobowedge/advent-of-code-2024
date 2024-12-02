def is_safe(x):
    diffs = set([int(j)-int(i) for i, j in zip(x[:-1], x[1:])])
    return diffs.issubset({1, 2, 3}) or diffs.issubset({-1, -2, -3})

def solution1(data):
    safe = 0
    for line in data:
        line = line.split()
        if is_safe(line):
            safe += 1
    return safe

def solution2(data):
    safe = 0
    for line in data:
        line = line.split()
        if is_safe(line):
            safe += 1
            continue
        for i in range(len(line)):
            new_line = line[:i] + line[i+1:]
            if is_safe(new_line):
                safe += 1
                break
    return safe
    
    
test_data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9""".splitlines()
assert(solution1(test_data) == 2)
assert(solution2(test_data) == 4)
my_data = open("data/day02.txt").read().splitlines()
print(f"Solution 1: {solution1(my_data)}")
print(f"Solution 2: {solution2(my_data)}")
