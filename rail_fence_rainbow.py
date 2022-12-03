def reset_color() -> str:
    reset = "\u001b[0m"
    return reset


def rainbow_by_index(index: int) -> str:
    red = "\u001b[31m"
    green = "\u001b[32m"
    yellow = "\u001b[33m"
    blue = "\u001b[34m"
    magenta = "\u001b[35m"
    cyan = "\u001b[36m"
    white = "\u001b[37m"

    rainbow = [red, green, yellow, blue, magenta, cyan, white]
    return rainbow[index % 7]


def encode(cipher_in: str, rails: int):
    cipher = cipher_in.replace(" ", "_")
    rail_fence = [[] for x in range(rails)]
    period: int = 2 * (rails - 1)
    for index, character in enumerate(cipher):
        active_row = index % period
        if active_row >= rails:
            active_row = period - active_row
        for row in range(rails):
            if row == active_row:
                rail_fence[row].append(cipher[index])
            else:
                rail_fence[row].append(" ")
    visual_to_text(rail_fence)
    print_rail_fence(rail_fence)
    visual_to_cipher(rail_fence)


def decode(cipher_str, rails):
    cipher = list(cipher_str.replace(" ", "_"))
    period: int = 2 * (rails - 1)
    index = 0
    rail_fence = [[] for x in range(rails)]
    for row in range(rails):
        for i in range(len(cipher)):
            if i % period == row:
                rail_fence[row].append(cipher[index])
                index += 1
            elif period - (i % period) == row:
                rail_fence[row].append(cipher[index])
                index += 1
            else:
                rail_fence[row].append(" ")
    visual_to_cipher(rail_fence)
    print_rail_fence(rail_fence)
    visual_to_text(rail_fence)


def print_rail_fence(fence):
    for i, rail in enumerate(fence):
        print(rainbow_by_index(i), list_to_string(rail), reset_color())


def visual_to_text(fence):
    print(" ", end="")
    for col in range(len(fence[0])):
        for row in range(len(fence)):
            print(rainbow_by_index(row), end="")
            if fence[row][col] != " ":
                print(fence[row][col].replace("_", " "), end="")
    print(reset_color())


def visual_to_cipher(fence):
    print(" ", end="")
    for row in range(len(fence)):
        print(rainbow_by_index(row), end="")
        for col in range(len(fence[row])):
            if fence[row][col] != " " and fence[row][col] is not None:
                print(fence[row][col].replace("_", " "), end="")
    print(reset_color())


def list_to_string(character_list: list) -> str:
    return "".join(character_list)


def brute_force_decode(cipher_string: str, start: int, end: int):
    for i in range(start, end + 1):
        print(f"Trying {i} rails.")
        print()
        decode(cipher_string, i)
        print()


print()
print()
encode("This sentence is an example text that is just being used for testing", 3)
print()
print()
decode("Tnex g hec xetsjn rtitenat iuiuoesn am t sesfsg ei pehttbe tnssla di", 6)
