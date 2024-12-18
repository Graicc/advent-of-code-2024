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
    return output[:-1]


with open("day_17/input.txt", "r") as f:
    lines = f.readlines()
    reg_a = int(lines[0].split(" ")[-1])
    reg_b = int(lines[1].split(" ")[-1])
    reg_c = int(lines[2].split(" ")[-1])

    program = list(map(int, lines[-1].split()[-1].split(",")))

    print(run(reg_a, reg_b, reg_c, program))


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
    return output[:-1]


# print(fast_run(50230824))


def solve(pattern: List[int], lower_seven_bits: int) -> int:
    if len(pattern) == 0:
        if lower_seven_bits == 0:
            return 0
        else:
            return -1

    to_match = pattern[0]
    rest = pattern[1:]

    for i in range(8):
        a = i << 7 | lower_seven_bits
        if val(a) == to_match:
            s = solve(rest, a >> 3)
            if s == -1:
                continue
            else:
                return s << 3 | a

    return -1


# str_program = ",".join(map(str, program))
# print(str_program)
for i in range(2**7):
    a = solve(program, i)
    if a != -1:
        print(a)
        # print(fast_run(a))
        break
