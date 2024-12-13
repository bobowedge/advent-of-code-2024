import re
def parse_data(data):
    games = []
    game = []
    for line in data:
        match = re.match("(.*): X[\+=](\d+), Y[\+=](\d+)", line)
        if match:
            game.append(int(match.group(2)))
            game.append(int(match.group(3)))
            if match.group(1) == "Prize":
                games.append(game)
                game = []
    return games

def score_game1(game):
    Ax, Ay, Bx, By, prizeX, prizeY = game
    determinant = Ax * By - Ay * Bx 
    assert determinant != 0
    buttonA = (By * prizeX - Bx * prizeY) // determinant
    buttonB = (-Ay * prizeX + Ax * prizeY) // determinant
    if ((buttonA * Ax + buttonB * Bx) == prizeX and 
        (buttonA * Ay + buttonB * By) == prizeY and
        0 <= buttonA <= 100 and 
        0 <= buttonB <= 100):
        return 3 * buttonA + buttonB
    return 0

def solution1(data):
    games = parse_data(data)
    tokens = 0
    for game in games:
        tokens += score_game1(game)
    return tokens

def score_game2(game):
    Ax, Ay, Bx, By, prizeX, prizeY = game
    determinant = Ax * By - Ay *  Bx 
    assert determinant != 0
    buttonA = (By * prizeX - Bx * prizeY) // determinant
    buttonB = (-Ay * prizeX + Ax * prizeY) // determinant
    if ((buttonA * Ax + buttonB * Bx) == prizeX and 
        (buttonA * Ay + buttonB * By) == prizeY and
        buttonA >=0 and buttonB >=0):
        return 3 * buttonA + buttonB
    return 0

def solution2(data):
    games = parse_data(data)
    tokens = 0
    for game in games:
        big_game = list(game)
        big_game[4] += 10000000000000
        big_game[5] += 10000000000000
        tokens += score_game2(big_game)
    return tokens    
    
test_data = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279""".splitlines()
assert(solution1(test_data) == 480)
def test_solution2(data):
    games = parse_data(data)
    win = [False] * len(games)
    for idx, game in enumerate(games):
        big_game = list(game)
        big_game[4] += 10000000000000
        big_game[5] += 10000000000000
        win[idx] = score_game2(big_game) > 0
    assert win[1]
    assert win[3]
    assert not win[0]
    assert not win[2]
test_solution2(test_data)
my_data = open("data/day13.txt").read().splitlines()
print(f"Solution 1: {solution1(my_data)}")
print(f"Solution 2: {solution2(my_data)}")
