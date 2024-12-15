def parse_data1(data):
    boxes = set()
    walls = set()
    robot = None
    moves = []
    for row, line in enumerate(data):
        for col, char in enumerate(line):
            if char == "#":
                walls.add((row, col))
            elif char == "O":
                boxes.add((row, col))
            elif char == "@":
                robot = (row, col)
            elif char == "^":
                moves.append((-1, 0))
            elif char == ">":
                moves.append((0, 1))
            elif char == "<":
                moves.append((0, -1))           
            elif char == "v":
                moves.append((1, 0))
    return walls, boxes, robot, moves

def solution1(data):
    walls, boxes, robot, moves = parse_data1(data)
    for dx, dy in moves:
        rx = robot[0] + dx
        ry = robot[1] + dy
        # Empty space, free to move
        if (rx, ry) not in boxes and (rx, ry) not in walls:
            robot = (rx, ry)
            continue
        # Pass through to the last box to move
        while (rx, ry) in boxes:
            rx = rx + dx
            ry = ry + dy
        # Hit a wall, no move
        if (rx, ry) in walls:
            continue
        ## Moving 
        # Update robot
        robot = (robot[0] + dx, robot[1] + dy)
        # Shift boxes
        boxes.discard(robot)     
        boxes.add((rx, ry))

    sum_coordinates = 0
    for bx, by in boxes:
        sum_coordinates += 100 * bx + by
    return sum_coordinates

def parse_data2(data):
    boxes = dict()
    walls = set()
    empty = set()
    robot = None
    moves = []
    for row, line in enumerate(data):
        for col, char in enumerate(line):
            if char == "#":
                walls.add((row, 2*col))
                walls.add((row, 2*col + 1))
            elif char == "O":
                boxes[(row, 2*col)] = "["
                boxes[(row, 2*col + 1)] = "]"
            elif char == "@":
                robot = (row, 2*col)
                empty.add((row, 2*col + 1))
            elif char == ".":
                empty.add((row, 2*col))
                empty.add((row, 2*col + 1))
            elif char == "^":
                moves.append((-1, 0))
            elif char == ">":
                moves.append((0, 1))
            elif char == "<":
                moves.append((0, -1))           
            elif char == "v":
                moves.append((1, 0))
    return walls, boxes, empty, robot, moves

def warehouse_print(walls, boxes, empty, robot):
    warehouse = []
    for row in range(10):
        s = ""
        for col in range(20):
            if (row, col) in walls:
                s += "#"
            elif (row, col) in boxes:
                s += boxes[(row, col)]
            elif (row, col) == robot:
                s += "@"
            else:
                s += "."
                assert (row, col) in empty
        warehouse.append(s)
    for row in warehouse:
        print(row)

def solution2(data):
    walls, boxes, empty, robot, moves = parse_data2(data)
    for dx, dy in moves:
        rx = robot[0] + dx
        ry = robot[1] + dy
        
        ## Can't move, hit a wall
        if (rx, ry) in walls:
            continue

        ## Free to move to empty space
        if (rx, ry) in empty:
            empty.discard((rx, ry))
            empty.add(robot)
            robot = (rx, ry)
            continue
        
        ## Build up set of boxes to move
        # Initial box to hit (both parts)
        boxes_to_move = {}
        if boxes[(rx, ry)] == "[":
            boxes_to_move[(rx, ry)] = "["
            boxes_to_move[(rx, ry + 1)] = "]"
        else:
            boxes_to_move[(rx, ry)] = "]"
            boxes_to_move[(rx, ry - 1)] = "["
        hit_wall = False
        while not hit_wall:
            # Keep adding more boxes until we hit a wall or there are none to add
            new_boxes = set()
            for (x, y) in boxes_to_move:
                newx = x + dx
                newy = y + dy
                if (newx, newy) in boxes_to_move or (newx, newy) in empty:
                    continue
                if (newx, newy) in walls:
                    hit_wall = True
                    break
                new_boxes.add((newx, newy))
            if hit_wall or len(new_boxes) == 0:
                break
            # Add the new boxes to the ones to move
            for (x, y) in new_boxes:
                if boxes[(x, y)] == "[":
                    boxes_to_move[(x, y)] = "["
                    boxes_to_move[(x, y + 1)] = "]"
                else:
                    boxes_to_move[(x, y)] = "]"
                    boxes_to_move[(x, y - 1)] = "["
        if hit_wall:
            continue

        ## We're moving boxes, so we need to update everything
        empty.add(robot)
        robot = (rx, ry)
        for (x, y) in boxes_to_move:
            del boxes[(x, y)]
            empty.add((x, y))
        for (x, y), side in boxes_to_move.items():
            boxes[(x + dx, y + dy)] = side
            empty.discard((x + dx, y + dy))

    sum_coordinates = 0
    for (x, y), side in boxes.items():
        if side == "[":
            sum_coordinates += 100 * x + y
    return sum_coordinates
    
    
test_data = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^""".splitlines()

test_data2 = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<""".splitlines()
assert(solution1(test_data2) == 2028)
assert(solution1(test_data) == 10092)
# test_data3 = """#######
# #...#.#
# #.....#
# #..OO@#
# #..O..#
# #.....#
# #######

# <vv<<^^<<^^""".splitlines()
# solution2(test_data3)

assert(solution2(test_data) == 9021)
my_data = open("data/day15.txt").read().splitlines()
print(f"Solution 1: {solution1(my_data)}")
print(f"Solution 2: {solution2(my_data)}")
