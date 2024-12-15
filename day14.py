import re
from collections import Counter

class Robot:    
    def __init__(self, px, py, vx, vy):
        self.px = int(px)
        self.py = int(py)
        self.vx = int(vx)
        self.vy = int(vy)

def parse_data(data):
    robots: list[Robot] = []
    for line in data:
        match = re.match("p=(\d+),(\d+)\s+v=(-?\d+),(-?\d+)", line)
        robot = Robot(*match.groups())
        robot.px, robot
        robots.append(robot)
    return robots

def safety_factor(robots, height, width):
    q = [0] * 4
    for robot in robots:
        if robot.px < width // 2 and robot.py < height // 2:
            q[0] += 1
        elif robot.px > width // 2 and robot.py < height // 2:
            q[1] += 1
        elif robot.px < width // 2 and robot.py > height // 2:
            q[2] += 1
        elif robot.px > width // 2 and robot.py > height // 2:
            q[3] += 1
    return q[0] * q[1] * q[2] * q[3]

def solution1(data, height, width):
    robots = parse_data(data)
    for robot in robots:
        robot.px += robot.vx * 100
        robot.py += robot.vy * 100
        robot.px %= width
        robot.py %= height
    return safety_factor(robots, height, width)

def solution2_first(data, height, width):
    """First solution using visual inspection of robots at various timesteps"""
    robots = parse_data(data)
    max_ycount = 0
    max_xcount = 0
    for idx in range(height * width):
        y_count = Counter()
        x_count = Counter()
        for robot in robots:
            robot.px += robot.vx 
            robot.py += robot.vy 
            robot.px %= width
            robot.py %= height
            y_count[robot.py] += 1
            x_count[robot.px] += 1
        
        max_ycount = max(y_count.values())
        max_xcount = max(x_count.values())

        # 31 and 34 are the max scores from previous runs
        if max_ycount == 31 and max_xcount == 34:
            print(idx)
            positions = set((robot.px, robot.py) for robot in robots)
            bathroom = ""
            for y in range(103):
                for x in range(101):
                    if (x, y) in positions:
                        bathroom += "R"
                    else:
                        bathroom += "."
                bathroom += "\n"
            print(bathroom)
            return idx
    return None

def solution2(data, height, width):
    """Cleaner solution, relying on safety factor, after some internet help"""
    robots = parse_data(data)
    best_idx = 100
    best_safety_factor = 210587128
    for idx in range(height * width):
        for robot in robots:
            robot.px += robot.vx 
            robot.py += robot.vy 
            robot.px %= width
            robot.py %= height
        
        local_sf = safety_factor(robots, height, width)
        if local_sf < best_safety_factor:
            best_safety_factor = local_sf
            best_idx = idx + 1
    return best_idx


test_data = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3""".splitlines()
assert(solution1(test_data, 7, 11) == 12)
# assert(solution2(test_data) == 0)
my_data = open("data/day14.txt").read().splitlines()
print(f"Solution 1: {solution1(my_data, 103, 101)}")
print(f"Solution 2: {solution2(my_data, 103, 101)}")
