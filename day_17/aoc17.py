from typing import Set, Dict, List, Tuple


def run(reg_a, reg_b, reg_c, program):
    def get_combo_operand(operand: int) -> int:
        if operand >= 0 and operand <= 3:
            return operand
        elif operand == 4:
            return reg_a
        elif operand == 5:
            return reg_b
        elif operand == 6:
            return reg_c
        else:
            raise ValueError()

    ip = 0
    output = ""
    while ip >= 0 and ip < len(program):
        instruction = program[ip]
        operand = program[ip + 1]
        if instruction == 0:  # adv
            reg_a = int(reg_a / 2 ** get_combo_operand(operand))
        elif instruction == 1:  # bxl
            reg_b = reg_b ^ operand
        elif instruction == 2:  # bst
            reg_b = get_combo_operand(operand) % 8
        elif instruction == 3:  # jnz
            if reg_a != 0:
                ip = operand
                continue
        elif instruction == 4:  # bxc
            reg_b = reg_b ^ reg_c
        elif instruction == 5:  # out
            output += f"{get_combo_operand(operand) % 8},"
        elif instruction == 6:  # bdv
            reg_b = int(reg_a / 2 ** get_combo_operand(operand))
        elif instruction == 7:  # cdv
            reg_c = int(reg_a / 2 ** get_combo_operand(operand))
        else:
            raise ValueError()

        ip += 2
    return output


with open("day_17/input.txt", "r") as f:
    lines = f.readlines()
    reg_a = int(lines[0].split(" ")[-1])
    reg_b = int(lines[1].split(" ")[-1])
    reg_c = int(lines[2].split(" ")[-1])

    program = list(map(int, lines[-1].split()[-1].split(",")))

    print(run(reg_a, reg_b, reg_c, program)[:-1])


def val(a: int) -> int:
    return (~(a % 8) ^ (a >> ((a % 8) ^ 3))) % 8


def fast_run(a: int):
    output = ""
    while True:
        output += str((~(a % 8) ^ (a >> ((a % 8) ^ 3))) % 8)
        output += ","
        a //= 8
        if a == 0:
            break
    return output


# Ensure that run == fast_run
# for i in range(100000):
#     slow = run(i, 0, 0, program)
#     fast = fast_run(i)
#     assert slow == fast

print(fast_run(50230824)[:-1])
# for i in range(50230824 // 8 * 8, 50230824 // 8 * 8 + 8):
#     print(i)
#     print(fast_run(i)[:-1])

l = 7


def solve(pattern: List[int], lower_seven_bits: int) -> int:
    # print("solve", pattern, lower_three_bits)
    # if len(pattern) == len(program) - 3:
    # print(len(pattern))
    # if len(pattern) == len(program) - 2:
    if len(pattern) == 0:
        if lower_seven_bits == 0:
            return 0
        else:
            return -1

    to_match = pattern[0]
    rest = pattern[1:]

    for i in range(8):
        a = i << l | lower_seven_bits
        if i == 4:
            assert len(bin(a)) == 7 + 3 + 2
        if val(a) == to_match:
            # print("l7b", len(pattern), lower_seven_bits)
            # print(a, to_match)
            # return solve(rest, i) << 3 | lower_three_bits
            # print("match", to_match, i, a)
            s = solve(rest, a >> 3)
            # print("post match", s)
            if s == -1:
                # return -1
                continue
            else:
                return s << 3 | a

    # print(f"no match at {len(program) - len(pattern)}")
    return -1


str_program = ",".join(map(str, program))
print(str_program)
for i in range(2**l):
    a = solve(program, i)
    if a != -1:
        if fast_run(a) == str_program + ",":
            print("SOLVED")
            print(a)
            print(bin(a))
            print(fast_run(a))
            break
        else:
            print(a)
            print(fast_run(a))

# print(fast_run(477489078123537 >> 3))
# # sol = 0b10001101100100100011000010110111000101011110000010001
# sol = 0b01100100100011000010110111000101011110000010001
# print(sol)
# print(fast_run(sol))
# curr = 0
# while True:
#     if curr % 1_000_000 == 0:
#         print(curr)

#     if fast(curr):
#         print(curr)
#         break

#     curr += 1
