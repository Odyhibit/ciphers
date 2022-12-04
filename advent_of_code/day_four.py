def get_list(text):
    start, end = text.split("-")
    output = []
    for i in range(int(start), int(end) + 1):
        output.append(int(i))
    return output


def get_subset(a, b):
    set_a = set(a)
    set_b = set(b)
    if (set_a <= set_b) or (set_b <= set_a):
        return True
    return False


def get_overlap(a, b):
    set_a = set(a)
    set_b = set(b)
    if set_a & set_b:
        return True
    return False


counts = [0, 0]
with open("day_four.txt", "r") as sections:
    for line in sections:
        one, two = line.strip().split(",")
        if get_subset(get_list(one), get_list(two)):
            counts[0] += 1
        if get_overlap(get_list(one), get_list(two)):
            counts[1] += 1

print("part 1", counts[0])
print("part 2", counts[1])