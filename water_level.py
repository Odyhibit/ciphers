import ctypes
import os

if os.name == "nt":
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)


def fill(input_array):
    water = 0
    water_depth = [0]
    for fillable_spot_index in range(1, len(input_array) - 1):
        left = max(input_array[0:fillable_spot_index])
        right = max(input_array[fillable_spot_index + 1:])
        potential_pool = min(left, right)
        if potential_pool - input_array[fillable_spot_index] > 0:
            water += potential_pool - input_array[fillable_spot_index]
            water_depth.append(potential_pool - input_array[fillable_spot_index])
        else:
            water_depth.append(0)
    water_depth.append(0)
    return water_depth, water


def visualize_water(wall: [int]):
    water = fill(wall)
    water_char = "\033[34m\033[46m▒"
    wall_char = "\033[0m█"
    print("  water", water[0], "Total :", water[1])
    print("  walls", wall)
    for height in range(max(wall) + 1, 0, -1):  # rows
        print("  ", end="")
        for value in range(0, len(wall)):  # cols
            if wall[value] >= height:
                print(wall_char, end="")  # draw wall
            elif wall[value] + water[0][value] >= height:
                print(water_char, end="")  # draw water
            else:
                print(" ", end="")
        print()
    print()


def main():
    walls = [[2, 1, 2],
             [3, 0, 1, 3, 0, 5],
             [3, 0, 1, 3, 0, 5, 0, 8, 0, 5],
             [3, 0, 0, 0, 0, 1, 2, 3, 4, 0, 4, 3, 2, 1, 3]]
    for wall in walls:
        visualize_water(wall)


if __name__ == "__main__":
    main()
