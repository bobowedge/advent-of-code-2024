from collections import defaultdict
from functools import cmp_to_key

def parse_data(data):
    rules = defaultdict(set)
    orders = []
    for line in data:
        line = line.strip()
        if len(line) == 0:
            continue
        if '|' in line:
            a, b = line.split('|')
            a = int(a)
            b = int(b)
            rules[a].add(b)
        else:
            order = [int(a) for a in line.split(",")]
            orders.append(order)
    return rules, orders


def solution1(data):
    rules, orders = parse_data(data)
    score = 0
    for order in orders:
        good = True
        for idx1, num1 in enumerate(order):
            if num1 not in rules:
                continue
            for num2 in rules[num1]:
                if num2 in order and order.index(num2) < idx1:
                    good = False
                    break
            if not good:
                break
        if good:
            midpt = (len(order) - 1)//2
            score += order[midpt]
    return score


def solution2(data):
    rules, orders = parse_data(data)
    score = 0

    def less(a, b):
        if a in rules and b in rules[a]:
            return -1
        if b in rules and a in rules[b]:
            return 1
        return 0

    for order in orders:
        sorted_order = sorted(order, key=cmp_to_key(less))
        if sorted_order == order:
            continue
        midpt = (len(sorted_order) - 1)//2
        score += sorted_order[midpt]
    return score
    
    
test_data = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47""".splitlines()
assert(solution1(test_data) == 143)
assert(solution2(test_data) == 123)
my_data = open("data/day05.txt").read().splitlines()
print(f"Solution 1: {solution1(my_data)}")
print(f"Solution 2: {solution2(my_data)}")
