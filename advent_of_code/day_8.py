def in_red(num):
    return "\u001b[31m" + str(num) + "\u001b[0m"


def in_green(num):
    return "\u001b[32m" + str(num) + "\u001b[0m"


def get_visible(x: int, y: int, trees: []) -> bool:
    if clear_up(x, y, grid) or clear_down(x, y, grid):
        return True
    if clear_left(x, y, grid) or clear_right(x, y, grid):
        return True
    return False


def clear_right(x, y, grid):
    current = grid[x][y]
    #print(f"range({x+1}, {len(grid[x])})")
    for i in range(y + 1, len(grid[x])):
        #print(f"{x+1} to {len(grid[x]) - 1}    {x},{i} {grid[x][i]} > current {current} blocked = {grid[x][i] >= current}")
        if grid[x][i] >= current:
            return False
    return True


def clear_left(x, y, grid):
    current = grid[x][y]
    for i in range(0, y):
        #print(f"{x + 1} to {len(grid[x])}    {x},{i} {grid[x][i]} > current {current} = {grid[x][i] >= current}")
        if grid[x][i] >= current:
            return False
    return True


def clear_up(x, y, grid):
    current = grid[x][y]
    for i in range(0, x):
        #print(f"    {i},{y} {grid[i][y]} > current {current} = {grid[i][y] >= current}")
        if grid[i][y] >= current:
            #print("view blocked")
            return False
    return True


def clear_down(x, y, grid):
    current = grid[x][y]
    for i in range(x + 1, len(grid)):
        if grid[i][y] >= current:
            return False
    return True


lines = map(str.split, open('input/day_8.txt').read().splitlines())
grid = []
for i, row in enumerate(lines):
    grid.append([])
    for col in row:
        for letter in col:
            grid[i].append(int(letter))

count = 0

for row in range(0, len(grid)):
    for col in range(0, len(grid[0])):
        if (row == 0) or (row == len(grid) - 1) or (col == 0) or (col == len(grid[0]) - 1):
            print(grid[row][col], end="")
        elif get_visible(row, col, grid):
            print(in_green(grid[row][col]), end="")
            count += 1
        else:
            print(in_red(grid[row][col]), end="")
    print()

print()
edges = 2 * ((len(grid) - 1) + (len(grid[0]) - 1))
print(f"edges {edges} + middle {count} = {edges + count}")

test_x = 2
test_y = 3
print(f"testing {test_x},{test_y} = {grid[test_x][test_y]}")
print("clear left 3,1 ", clear_left(test_x, test_y, grid))
print("clear right 3,1 ", clear_right(test_x, test_y, grid))
print("clear up 3,1 ", clear_up(test_x, test_y, grid))
print("clear down 3,1 ", clear_down(test_x, test_y, grid))
print("len(grid", len(grid),"len(grid[0]", len(grid[0]))
