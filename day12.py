from collections import defaultdict

ORTHOGONAL = {(0, 1), (0, -1), (1, 0), (-1, 0)}

def neighbor_generator(value: tuple):
    for dx, dy in ORTHOGONAL:
        # plot
        if type(value[0]) is int:
            yield (value[0] + dx, value[1] + dy)
        # fence
        else:
            yield ((value[0][0] + dx, value[0][1] + dy), (value[1][0] + dx, value[1][1] + dy))


def parse_data(data):
    """Produces dict of letters to the set of all garden plots with that letter"""
    letter_plots = defaultdict(set)
    for row, line in enumerate(data):
        for col, char in enumerate(line):
            letter_plots[char].add((row, col))
    return letter_plots

def find_connected_components(plots: set):
    """Find the connected components of a set"""
    components = list()
    component = [plots.pop()]
    while len(plots) > 0:
        component_size = len(component)
        # Loop over the current members of the component
        for idx in range(component_size):
            # Check the neighbors
            for neighbor in neighbor_generator(component[idx]):
                # If neighbor is in plots, add to component
                if neighbor in plots:
                    component.append(neighbor)
                    plots.discard(neighbor)
        # If we didn't add anything, component is complete
        if component_size == len(component):
            components.append(set(component))
            # Reset if there are some more plots to do
            if len(plots) > 0:
                component = [plots.pop()]
    if len(component) > 0:
        components.append(set(component))
    return components

def area(region):
    return len(region)

def perimeter(region):
    length = 0
    for plot in region:
        for neighbor in neighbor_generator(plot):
            if neighbor not in region:
                length += 1
    return length

def solution1(data):
    letter_plots = parse_data(data)

    regions = list()
    for plots in letter_plots.values():
        regions.extend(find_connected_components(plots))

    price = 0
    for region in regions:
        price += area(region) * perimeter(region)
    return price

def sides(region):
    """Calculate the number of sides for the region"""

    # Find all the fences for the region
    fences = set()
    for plot in region:
        for neighbor in neighbor_generator(plot):
            if neighbor not in region:
                # Need orientation of fence (inside, outside)
                fences.add((plot, neighbor))

    # Count the connect components of the fences (similar code to find_connected_components)
    return len(find_connected_components(fences))

def solution2(data):
    letter_plots = parse_data(data)

    regions = list()
    for plots in letter_plots.values():
        regions.extend(find_connected_components(plots))

    price = 0
    for region in regions:
        price += area(region) * sides(region)
    return price

    
test_data = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE""".splitlines()
assert(solution1(test_data) == 1930)
assert(solution2(test_data) == 1206)
my_data = open("data/day12.txt").read().splitlines()
print(f"Solution 1: {solution1(my_data)}")
print(f"Solution 2: {solution2(my_data)}")
