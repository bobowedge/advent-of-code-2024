def checksum(memory):
    value = 0
    for idx, file_id in enumerate(memory):
        if file_id is None:
            continue
        value += idx * file_id
    return value

def solution1(data):
    memory = []
    for idx, value in enumerate(data):
        value = int(value)
        if idx % 2 == 0:
            memory.extend([idx//2] * value)
        else:
            memory.extend([None] * value)

    first_empty = memory.index(None)
    last_block = len(memory) - 1
    while first_empty < last_block:
        memory[first_empty] = memory[last_block]
        memory[last_block] = None
        while memory[last_block] is None:
            last_block -= 1
        first_empty = memory.index(None, first_empty)

    return checksum(memory)


def solution2(data):
    memory = []
    file_blocks = {}
    position = 0
    for idx, num_blocks in enumerate(data):
        num_blocks = int(num_blocks)
        if idx % 2 == 0:
            memory.extend([idx//2] * num_blocks)
            file_blocks[idx//2] = (position, num_blocks)
        else:
            memory.extend([None] * num_blocks)
        position += num_blocks

    for _, (file_position, file_size) in sorted(file_blocks.items(), reverse=True):
        # Find the next set of empty blocks that will fit this file
        empty = memory.index(None)
        while empty < file_position and empty != -1:
            size = 1
            while memory[empty + size] is None:
                size += 1
            if size >= file_size:
                break
            empty = memory.index(None, empty + size)
        
        # If no such empty blocks, go down to the next file
        if empty > file_position or empty == -1:
            continue

        # Swap the blocks
        memory[empty : empty + file_size] = memory[file_position : file_position + file_size]
        memory[file_position: file_position + file_size] = [None] * file_size

    return checksum(memory)
    
    
test_data = """2333133121414131402"""
assert(solution1(test_data) == 1928)
assert(solution2(test_data) == 2858)
my_data = open("data/day09.txt").read()
print(f"Solution 1: {solution1(my_data)}")
print(f"Solution 2: {solution2(my_data)}")
