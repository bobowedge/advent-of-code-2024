import re


def solution1(data):
    total = 0
    for line in data:
        matches = re.findall("mul\(\d{1,3},\d{1,3}\)", line)
        for m in matches:
            match = re.search("mul\((\d*),(\d*)\)", m)
            a = int(match.group(1))
            b = int(match.group(2))
            total += a * b
    return total


def solution2(data):
    total = 0
    data = "".join(data)
    mul_index = data.find("mul")
    while mul_index != -1:
        do_index = data.rfind("do()", 0, mul_index)
        dont_index = data.rfind("don't()", 0, mul_index)
        if dont_index == -1 or do_index > dont_index:
            match = re.match("mul\((\d{1,3}),(\d{1,3})\)", data[mul_index:])
            if match:
                a = int(match.group(1))
                b = int(match.group(2))
                total += a * b
        mul_index = data.find("mul", mul_index + 1)
    return total
    
    
test_data = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))""".splitlines()
assert(solution1(test_data) == 161)
test_data = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))""".splitlines()
assert(solution2(test_data) == 48)
my_data = open("data/day03.txt").read().splitlines()
print(f"Solution 1: {solution1(my_data)}")
print(f"Solution 2: {solution2(my_data)}")
