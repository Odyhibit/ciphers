def common_member(a, b, c=None):
    a_set = set(a)
    b_set = set(b)
    if c is None and a_set & b_set:
        return a_set & b_set
    c_set = set(c)
    if a_set & b_set & c_set:
        return a_set & b_set & c_set


symbols = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
totals = [0, 0]

with open("day_3.txt", "r") as rucksacks:
    while rucksacks:
        lines = [line.strip() for line in [rucksacks.readline() for _ in range(3)] if len(line)]
        if len(lines) == 3:
            item = common_member(lines[0], lines[1], lines[2])
            totals[1] += symbols.index(list(item)[0])
            for line in lines:
                item = common_member(line[:len(line) // 2], line[len(line) // 2:])
                totals[0] += symbols.index(list(item)[0])
        else:
            rucksacks = False

print("part 1\n", "Total is:", totals[0])
print("part 2\n", "Total is:", totals[1])
