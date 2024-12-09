def solution1(data):
    memory = []
    for idx, value in enumerate(data):
        value = int(value)
        if idx % 2 == 0:
            memory.extend([idx//2] * value)
        else:
            memory.extend([None] * value)

    first_bad = memory.index(None)
    last_good = len(memory) - 1
    while first_bad < last_good:
        memory[first_bad] = memory[last_good]
        memory[last_good] = None
        while memory[last_good] is None:
            last_good -= 1
        first_bad = memory.index(None, first_bad)
    checksum = 0
    for idx, val in enumerate(memory):
        if val is None:
            break
        checksum += idx * val
    return checksum


def solution2(data):
    memory = []
    file_blocks = {}
    position = 0
    for idx, value in enumerate(data):
        value = int(value)
        if idx % 2 == 0:
            memory.extend([idx//2] * value)
            file_blocks[idx//2] = (position, value)
        else:
            memory.extend([None] * value)
        position += value

    insert = True
    while insert:
        first_bad = memory.index(None)
        size = 1
        while memory[first_bad + size] is None:
            size += 1
        
        insert = False
        for idx in sorted(file_blocks.keys(), reverse=True):
            file_position, file_size = file_blocks[idx]
            bad = memory.index(None)
            size = 1
            while bad < file_position and bad != -1:
                while memory[bad + size] is None:
                    size += 1
                if size >= file_size:
                    break
                else:
                    bad = memory.index(None, bad + size)
                    size = 1
            if bad > file_position or bad == -1:
                continue
            for pos in range(file_size):
                memory[bad + pos] = idx
                memory[file_position + pos] = None
                
    checksum = 0
    for idx, val in enumerate(memory):
        if val is None:
            continue
        checksum += idx * val
    return checksum
    
    
test_data = """2333133121414131402"""
assert(solution1(test_data) == 1928)
assert(solution2(test_data) == 2858)
my_data = open("data/day09.txt").read()
print(f"Solution 1: {solution1(my_data)}")
print(f"Solution 2: {solution2(my_data)}")
