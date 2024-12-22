from collections import deque, Counter

def mix(secret, value):
    return secret ^ value
assert mix(42, 15) == 37

def prune(secret):
    secret %= 16777216
    return secret
assert prune(100000000) == 16113920

def next_secret(secret):
    x = secret * 64
    secret = mix(secret, x)
    secret = prune(secret)
    
    y = secret // 32
    secret = mix(secret, y)
    secret = prune(secret)

    z = secret * 2048
    secret = mix(secret, z)
    return prune(secret)

test_numbers = [
    123,
    15887950,
    16495136,
    527345,
    704524,
    1553684,
    12683156,
    11100544,
    12249484,
    7753432,
    5908254,
]
for idx, num in enumerate(test_numbers[:-1]):
    assert next_secret(num) == test_numbers[idx + 1]

def solution1(data):
    sum_secrets = 0
    for line in data:
        number = int(line)
        for _ in range(2000):
            number = next_secret(number)
        sum_secrets += number
    return sum_secrets


def solution2(data):
    banana_counts_per_diff = Counter()
    for line in data:
        number = int(line)
        seen_diffs = set()
        diffs = deque()
        previous_bananas = number % 10
        for jdx in range(2000):
            number = next_secret(number)
            current_bananas = number % 10
            diffs.append(current_bananas - previous_bananas)
            if jdx >= 3:
                if tuple(diffs) not in seen_diffs:
                    banana_counts_per_diff[tuple(diffs)] += current_bananas
                seen_diffs.add(tuple(diffs))
                diffs.popleft()
            previous_bananas = current_bananas
    max_bananas = max(banana_counts_per_diff.values())
    return max_bananas
    
    
test_data = """1
10
100
2024""".splitlines()
assert(solution1(test_data) == 37327623)
test_data2 = """1
2
3
2024""".splitlines()
assert(solution2(test_data2) == 23)
my_data = open("data/day22.txt").read().splitlines()
print(f"Solution 1: {solution1(my_data)}")
print(f"Solution 2: {solution2(my_data)}")
