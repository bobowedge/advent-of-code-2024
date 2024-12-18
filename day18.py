import heapq

ORTHOGONAL = {(1, 0), (-1, 0), (0, 1), (0, -1)}

def parse_data(data):
    fall_bytes = []
    for line in data:
        x, y = line.split(",")
        fall_bytes.append((int(x), int(y)))
    return fall_bytes

def dijkstra(corrupted, start, end):
    queue = [(0, start)]
    seen = set()
    while len(queue) > 0:
        length, point = heapq.heappop(queue)
        if point == end:
            return length
        if point in seen:
            continue
        seen.add(point)
        for d in ORTHOGONAL:
            px = point[0] + d[0]
            py = point[1] + d[1]
            new_point = (px, py)
            if px < 0 or py < 0 or px > end[0] or py > end[1] or new_point in corrupted:
                continue
            heapq.heappush(queue, (length + 1, new_point))
    return None

def solution1(data, size, number):
    fall_bytes = parse_data(data)
    corrupted = set(fall_bytes[:number])
    start = (0, 0)
    end = (size, size)
    return dijkstra(corrupted, start, end)

def solution2(data, size):
    fall_bytes = parse_data(data)
    start = (0, 0)
    end = (size, size)
    corrupted = set()
    for byte in fall_bytes:
        corrupted.add(byte)
        length = dijkstra(corrupted, start, end)
        if length is None:
            return f"{byte[0]},{byte[1]}"
    return None
    
    
test_data = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0""".splitlines()
assert(solution1(test_data, size=6, number=12) == 22)
assert(solution2(test_data, size=6) == "6,1")
my_data = open("data/day18.txt").read().splitlines()
print(f"Solution 1: {solution1(my_data, size=70, number=1024)}")
print(f"Solution 2: {solution2(my_data, size=70)}")
