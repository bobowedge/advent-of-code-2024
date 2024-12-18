import re
def parse_data(data):
    A = None
    B = None
    C = None
    opcodes = []
    operands = []
    for line in data:
        line = line.strip()
        if len(line) == 0:
            continue
        matchA = re.match(r"Register A: (\d+)", line)
        matchB = re.match(r"Register B: (\d+)", line)
        matchC = re.match(r"Register C: (\d+)", line)
        matchProg = re.match(r"Program: (.*)", line)
        if matchA:
            A = int(matchA.group(1))
        elif matchB:
            B = int(matchB.group(1))
        elif matchC:
            C = int(matchC.group(1))
        elif matchProg:
            values = [int(x) for x in matchProg.group(1).split(",")]
            opcodes = values[::2]
            operands = values[1::2]
    return A, B, C, opcodes, operands

def solution1(data):
    A, B, C, opcodes, operands = parse_data(data)

    output = []
    idx = 0
    while idx < len(opcodes):
        opcode = opcodes[idx]
        operand = operands[idx]
        if opcode == 3 and A != 0:
            idx = operand
            continue
        elif opcode in [0, 2, 5, 6, 7]:
            combo = None
            if operand in [0, 1, 2, 3]:
                combo = operand
            elif operand == 4:
                combo = A
            elif operand == 5:
                combo = B
            elif operand == 6:
                combo = C
            else:
                assert False
            if opcode == 0:
                A = A // 2**combo
            elif opcode == 2:
                B = combo % 8
            elif opcode == 5:
                output.append(str(combo % 8))
            elif opcode == 6:
                B = A // 2**combo
            elif opcode == 7:
                C = A // 2**combo
        elif opcode == 1:
            B ^= operand
        elif opcode == 4:
            B ^= C
        idx += 1
    
    return ",".join(output)

def parse_data2(data):
    for line in data:
        matchProg = re.match(r"Program: (.*)", line)
        if matchProg:
            return [int(x) for x in matchProg.group(1).split(",")]

def one_round(program, A):
    """
    Do a single round of the program with starting value A
    """
    B = None
    C = None
    opcodes = program[::2]
    operands = program[1::2]
    for opcode, operand in zip(opcodes, operands):
        if opcode == 3:
            return A, B, C
        elif opcode in [0, 2, 5, 6, 7]:
            combo = None
            if operand in [0, 1, 2, 3]:
                combo = operand
            elif operand == 4:
                combo = A
            elif operand == 5:
                combo = B
            elif operand == 6:
                combo = C
            else:
                assert False
            if opcode == 0:
                A = A // 2**combo
            elif opcode == 2:
                B = combo % 8
            elif opcode == 5:
                B = combo % 8
            elif opcode == 6:
                B = A // 2**combo
            elif opcode == 7:
                C = A // 2**combo
        elif opcode == 1:
            B ^= operand
        elif opcode == 4:
            B ^= C
    return None

def solution2(data):
    """
    This is not a general solution, but it works for my input data program
    Key reasons:
    1. There is only one print and it always prints B
    2. The inputs B & C do not matter for my input data program because they are set
       by the program before they are used
    3. The input A is modified by integer dividing by 8 everytime
    4. The last command in the program is the only jump
    """
    program = parse_data2(data)

    # A = 0 at the end because otherwise the jump would restart the program
    nextA = set()
    nextA.add(0)
    
    # Work backwards from the end of the program
    for idx in range(len(program) - 1, -1, -1):
        # B is the printed output
        B = program[idx]
        
        # Find the possible values of A from the last round of the program
        prevA = set()    
        for A in nextA:
            for pA in [a for a in range(A*8, (A+1)*8)]:
                outA, outB, _ = one_round(program, pA)
                if outA != A or outB != B:
                    continue
                # Possible A
                prevA.add(pA)
        nextA = prevA
    # Take the smallest initial value
    return min(prevA)

    
test_data = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0""".splitlines()
assert(solution1(test_data) == "4,6,3,5,6,3,5,2,1,0")
test_data2 = """Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0""".splitlines()
assert(solution2(test_data2) == 117440)
my_data = open("data/day17.txt").read().splitlines()
print(f"Solution 1: {solution1(my_data)}")
print(f"Solution 2: {solution2(my_data)}")