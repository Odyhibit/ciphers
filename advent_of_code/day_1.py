highest = [0, 0, 0]
current = 0
with open("day_1.txt", "r") as calories:
    for calorie in calories:
        if calorie != "\n":
            current += int(calorie.strip())
        else:
            if current > highest[0]:
                highest[0] = current
            elif current > highest[1]:
                highest[1] = current
            elif current > highest[2]:
                highest[2] = current
            current = 0

print("part 1", highest[0])
print("part 2", highest[0] + highest[1] + highest[2])
