from collections import defaultdict

with open("day_23/input.txt", "r") as f:
    pairs = [l.strip().split("-") for l in f.readlines()]

neighbors = defaultdict(set)

for l,r in pairs:
    neighbors[l].add(r)
    neighbors[r].add(l)

found = set()
for node,adjs in neighbors.items():
    if node[0] != 't':
        continue
    for adj in adjs:
        for adj2 in neighbors[adj]:
            if node in neighbors[adj2]:
                l = [node, adj, adj2]
                l.sort()
                found.add(tuple(l))


print(len(found))

connected_components = set([(x,) for x in neighbors.keys()])

while len(connected_components) > 1:
    next_connected_components = set()
    for node, adjs in neighbors.items():
        for s in connected_components:
            if node in s:
                continue
            if all([(elem in adjs) for elem in s]):
                new = list(s)
                new.append(node)
                new.sort()
                next_connected_components.add(tuple(new))

    connected_components = next_connected_components

for e in connected_components:
    print(",".join(e))
