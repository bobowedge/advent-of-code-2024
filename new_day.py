import argparse

parser = argparse.ArgumentParser("Generate new python file and data file")
parser.add_argument("day", type=int)

args = parser.parse_args()

python_file = f"day{args.day:02}.py"
data_file = f"data/day{args.day:02}.txt"

with open(python_file, "w") as f:
    f.write('''def solution1(data):
    return 0


def solution2(data):
    return 0
    
    
test_data = """""".splitlines()
assert(solution1(test_data) == 0)
assert(solution2(test_data) == 0)
''')
    f.write(f'''my_data = open("{data_file}").read().splitlines()''')
    f.write('\nprint(f"Solution 1: {solution1(my_data)}")\nprint(f"Solution 2: {solution2(my_data)}")\n')


open(data_file, 'a').close()