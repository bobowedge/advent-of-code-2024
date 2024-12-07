def parse_data(data):
    test_values = {}
    for line in data:
        value, numbers = line.split(": ")
        value = int(value)
        numbers = [int(x) for x in numbers.split()]
        test_values[value] = numbers
    return test_values


def solution1(data):
    test_values = parse_data(data)
    total_calibration_result = 0
    for value, numbers in test_values.items():
        number_paths = [numbers]
        while len(number_paths) > 0:
            path = number_paths.pop()
            path_add = path[0] + path[1]
            path_mul = path[0] * path[1]
            if len(path) == 2:
                if path_add == value or path_mul == value:
                    total_calibration_result += value
                    number_paths = []
            else:
                number_paths.append([path_add] + path[2:])
                number_paths.append([path_mul] + path[2:])
    return total_calibration_result


def solution2(data):
    test_values = parse_data(data)
    total_calibration_result = 0
    for value, numbers in test_values.items():
        number_paths = [numbers]
        while len(number_paths) > 0:
            path = number_paths.pop()
            path_add = path[0] + path[1]
            path_mul = path[0] * path[1]
            path_cat = int(str(path[0]) + str(path[1]))
            if len(path) == 2:
                if path_add == value or path_mul == value or path_cat == value:
                    total_calibration_result += value
                    number_paths = []
            else:
                number_paths.append([path_add] + path[2:])
                number_paths.append([path_mul] + path[2:])
                number_paths.append([path_cat] + path[2:])
    return total_calibration_result

from time import process_time    
    
test_data = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20""".splitlines()
assert(solution1(test_data) == 3749)
assert(solution2(test_data) == 11387)
my_data = open("data/day07.txt").read().splitlines()
print(f"Solution 1: {solution1(my_data)}")
print(f"Solution 2: {solution2(my_data)}")




