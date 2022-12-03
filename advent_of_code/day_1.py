highest = 0
current = 0
with open("day_1.txt", "r") as calories:
    for calorie in calories:
        if calorie != "\n":
            current += int(calorie.strip())
        else:
            if current > highest:
                highest = current
            current = 0

print(highest)