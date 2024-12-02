import bisect
from collections import Counter

def solution1(data):
    list1 = []
    list2 = []
    for line in data:
        a, b = line.split()
        bisect.insort(list1, int(a))
        bisect.insort(list2, int(b))
    total = 0 
    for x, y in zip(list1, list2):
        total += abs(x-y)
    return total


def solution2(data):
    list1 = []
    counter2 = Counter()
    for line in data:
        a, b = line.split()
        list1.append(int(a))
        counter2[int(b)] += 1

    sim_score = 0
    for x in list1:
        sim_score += x * counter2[x]
    return sim_score
    
test_data = """3   4
4   3
2   5
1   3
3   9
3   3""".splitlines()
assert(solution1(test_data) == 11)
assert(solution2(test_data) == 31)
my_data = open("data/day01.txt").read().splitlines()
print(f"Solution 1: {solution1(my_data)}")
print(f"Solution 2: {solution2(my_data)}")
