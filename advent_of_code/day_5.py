def visualize_stacks(stack_list: []):
    for i in range(len(max(stack_list, key=len)), 0, -1):
        for stack in stack_list:
            if len(stack) >= i:
                print(stack[i - 1] + " ", end="")
            else:
                print("  ", end="")
        print()
    print("1 2 3 4 5 6 7 8 9")


stacks = [[] for i in range(9)]
with open("input/day_5.txt", "r") as manifest:
    while change := manifest.readline().strip("\n"):
        change += " "
        if len(change) > 3:
            for i in range(0, len(change), 4):
                item = change[i + 1:i + 2]
                if item != " " and item.isalpha():
                    stacks[i // 4].insert(0, item)
    for line in manifest:
        numbers = line.strip("\n").split(" ")
        repeats = int(numbers[1])
        stack_from = int(numbers[3]) - 1
        stack_to = int(numbers[5]) - 1
        for i in range(repeats, 0, -1):
            this_item = stacks[stack_from].pop(-1 * i)  # delete content of parenthesis for part 1
            stacks[stack_to].append(this_item)

visualize_stacks(stacks)
