from collections import defaultdict

def parse_data(data):
    lans = set()
    connections = defaultdict(set)
    for line in data:
        computer1, computer2 = line.split('-')
        lan = frozenset([computer1, computer2])
        lans.add(lan)
        connections[computer1].add(computer2)
        connections[computer2].add(computer1)
    return lans, connections


def extend_lan(lan, connections):
    """
    Given an existing LAN of length N, compute the possible LANs of 
        length N + 1 (possibly empty)
    """
    # Find computers connected to every node of LAN
    connected_computers: set = set()
    for idx, computer in enumerate(lan):
        if idx == 0:
            connected_computers = set(connections[computer])
        else:
            connected_computers &= connections[computer]
    
    # Make new LANs by extending the LAN from the connected computers
    new_lans = set()
    for computer in connected_computers:
        new_lan = set(lan)
        new_lan.add(computer)
        new_lans.add(frozenset(new_lan))
    return new_lans


def solution1(data):
    lans, connections = parse_data(data)
    t_lans = set()
    for lan in lans:
        for x, y, z in extend_lan(lan, connections):
            if 't' in [x[0], y[0], z[0]]:
                t_lans.add(frozenset([x, y, z]))
    return len(t_lans)

def solution2(data):
    lans, connections = parse_data(data)

    # Extend all the lans of length N to length N+1
    # Done when there's only 1 left
    while len(lans) > 1:
        new_lans = set()
        for lan in lans:
            new_lans.update(extend_lan(lan, connections))
        lans = set(new_lans)

    assert len(lans) == 1

    best_lan = list(lans.pop())
    best_lan.sort()
    return ",".join(best_lan)
    
test_data = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn""".splitlines()
assert(solution1(test_data) == 7)
assert(solution2(test_data) == "co,de,ka,ta")
my_data = open("data/day23.txt").read().splitlines()
print(f"Solution 1: {solution1(my_data)}")
print(f"Solution 2: {solution2(my_data)}")
