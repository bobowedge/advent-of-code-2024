from collections import defaultdict
from functools import cmp_to_key, partial

def parse_data(data):
    rules = defaultdict(set)
    updates = []
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
            page = [int(a) for a in line.split(",")]
            updates.append(page)
    return rules, updates


def compare_rules(rules, a, b):
    """
    Comparison using the input rules
    Returns -1 if a|b
    Returns  1 if b|a
    Returns 0 otherwise
    """
    if a in rules and b in rules[a]:
        return -1
    if b in rules and a in rules[b]:
        return 1
    return 0


def solution1(data):
    # A cleaner version of first solution that used a lot of loops
    rules, updates = parse_data(data)
    compare = partial(compare_rules, rules)
    middle_page_sum = 0
    for update in updates:
        sorted_update = sorted(update, key=cmp_to_key(compare))
        if sorted_update == update:
            midpt = (len(update) - 1)//2
            middle_page_sum += update[midpt]
    return middle_page_sum


def solution2(data):
    rules, updates = parse_data(data)
    compare = partial(compare_rules, rules)
    middle_page_sum = 0
    for update in updates:
        sorted_update = sorted(update, key=cmp_to_key(compare))
        if sorted_update == update:
            continue
        midpt = (len(sorted_update) - 1)//2
        middle_page_sum += sorted_update[midpt]
    return middle_page_sum
    
    
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
