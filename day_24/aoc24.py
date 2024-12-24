from typing import Dict, List, Tuple


def parse_gate(line: str) -> Tuple[str, str, str, str]:
    parts = line.strip().split()
    return (parts[0], parts[1], parts[2], parts[4])


gates: List[Tuple[str, str, str, str]]
values: Dict[str, bool] = {}

with open("day_24/input.txt", "r") as f:
    parts = f.read().split("\n\n")
    for line in parts[0].split("\n"):
        lparts = line.strip().split(": ")
        values[lparts[0]] = lparts[1] == "1"

    gates = [parse_gate(line) for line in parts[1].split("\n")]

orig_gates = gates.copy()
orig_values = values.copy()


def simulate(values: Dict[str, bool], gates: List[Tuple[str, str, str, str]]):
    while True:
        start_len = len(values)

        for l, op, r, out in gates:
            if out in values or l not in values or r not in values:
                continue
            if op == "OR":
                values[out] = values[l] or values[r]
            elif op == "AND":
                values[out] = values[l] and values[r]
            elif op == "XOR":
                values[out] = values[l] != values[r]

        if len(values) == start_len:
            break


def get_num(l: str, values) -> int:
    total = 0
    for k, v in values.items():
        if k[0] == l and v:
            val = int(k[1:])
            total += 2**val
    return total


simulate(values, gates)
print(get_num("z", values))

potential_bits = []
for i in range(45):
    new_gates = orig_gates.copy()
    new_values = orig_values.copy()
    for j in range(45):
        new_values[f"y{j:02d}"] = j == i
        new_values[f"x{j:02d}"] = False
    simulate(new_values, new_gates)
    z = get_num("z", new_values)
    if z != 1 << i:
        potential_bits.append(i)

print("Look at bits", potential_bits)
with open("graph.txt", "+w") as f:
    f.write("digraph G {\n")
    color_map = {
        "XOR": "red",
        "AND": "blue",
        "OR": "green",
    }
    for gate in orig_gates:
        f.write(f'{gate[0]} -> {gate[3]} [color = "{color_map[gate[1]]}"]\n')
        f.write(f'{gate[2]} -> {gate[3]} [color = "{color_map[gate[1]]}"]\n')
    f.write("}")


ans = input("Enter the suspect nodes separated by spaces: ").split()
ans.sort()
print(",".join(ans))
