import string


def common_member_two(pocket_one, pocket_two):
    p1 = set(pocket_one)
    p2 = set(pocket_two)
    if p1 & p2:
        return p1 & p2


symbols = "0" + string.ascii_lowercase + string.ascii_uppercase
total = 0
with open("day_3.txt", "r") as rucksacks:
    for rucksack in rucksacks:
        item = common_member_two(rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:])
        total += symbols.index(list(item)[0])
        match_found = True
print("part 1")
print("Total is:", total)


# *** part 2 ***

def common_member_three(a, b, c):
    a_set = set(a)
    b_set = set(b)
    c_set = set(c)
    if a_set & b_set & c_set:
        return a_set & b_set & c_set


total = 0
with open("day_3.txt", "r") as rucksacks:
    while rucksacks:
        lines = [line.strip() for line in [rucksacks.readline() for _ in range(3)] if len(line)]
        if len(lines) == 3:
            item = common_member_three(lines[0], lines[1], lines[2])
            total += symbols.index(list(item)[0])
        else:
            rucksacks = False

print("part 2")
print("Total is:", total)
