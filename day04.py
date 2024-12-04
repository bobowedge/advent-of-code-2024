def solution1(data):
    total = 0
    for row, line in enumerate(data):
        for col, char in enumerate(line):
            # Start has to be an 'X'
            if char != "X":
                continue

            # Check strings each of the 8 directions
            for delta_row, delta_col in [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                # Not near the edges
                if row + 3 * delta_row >= len(data) or row + 3 * delta_row < 0:
                    continue
                if col + 3 * delta_col >= len(line) or col + 3 * delta_col < 0:
                    continue

                putative_xmas = "X"
                for idx in range(1, 4):
                    putative_xmas += data[row + idx * delta_row][col + idx * delta_col]
                if putative_xmas == "XMAS":
                    total += 1
    return total


def solution2(data):
    total = 0
    for row, line in enumerate(data):
        for col, char in enumerate(line):
            # Middle has to be an 'A'
            if char != "A":
                continue

            # Not at the edges
            if row + 1 >= len(data) or row == 0:
                continue
            if col + 1 >= len(line) or col == 0:
                continue

            # top left and bottom right
            tlbr= {data[row - 1][col - 1], data[row + 1][col + 1]}

            # top right and bottom left
            trbl = {data[row + 1][col - 1], data[row - 1][col + 1]}

            # both have to be {"M", "S"} to be make cross
            if tlbr == trbl and tlbr == {"M", "S"}:
                total +=1 
    return total
    
    
test_data = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".splitlines()
assert(solution1(test_data) == 18)
assert(solution2(test_data) == 9)
my_data = open("data/day04.txt").read().splitlines()
print(f"Solution 1: {solution1(my_data)}")
print(f"Solution 2: {solution2(my_data)}")
