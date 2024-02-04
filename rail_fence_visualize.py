def physical_encode_example():
    plain_text = "Courage is grace under pressure SKY-AIQI-9380.".replace(" ", "_")
    rows = 5
    waves = [[] for x in range(rows)]
    this_row = 0
    updown = "down"
    for i, char in enumerate(plain_text):
        for j in range(rows):
            if this_row == j:
                waves[j].append(plain_text[i])
            else:
                waves[j].append(" ")
        if updown == "up":
            this_row -= 1
        if updown == "down":
            this_row += 1
        if this_row == rows - 1:
            updown = "up"
        if this_row == 0:
            updown = "down"
    for line in waves:
        print(list_to_string(line))
    visual_to_cipher(waves)


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
    print_rail_fence(rail_fence)
    visual_to_text(rail_fence)


def print_rail_fence(fence):
    for rail in fence:
        print(list_to_string(rail))


def visual_to_text(fence):
    for col in range(len(fence[0])):
        for row in range(len(fence)):
            if fence[row][col] != " ":
                print(fence[row][col].replace("_", " "), end="")
    print("")


def visual_to_cipher(fence):
    for row in range(len(fence)):
        for col in range(len(fence[row])):
            if fence[row][col] != " ":
                print(fence[row][col].replace("_", " "), end="")
    print("")


def list_to_string(character_list: list) -> str:
    return "".join(character_list)


def brute_force_decode(cipher_string: str, start: int, end: int):
    for i in range(start, end + 1):
        print(f"Trying {i} rails.")
        print()
        decode(cipher_string, i)
        print()


physical_encode_example()
print()
print()
encode("Courage is grace under pressure SKY-AIQI-9380.", 5)
print()
print()
decode("Cair eruSA-0org sgaeudrpesr K-II98.ue cn seYQ3", 3)
print()
print()
decode("F daS-eefn  n KZ3eheadty.YI8lta oiwy-Q0. r aI2", 5)
print()

print()
print("Brute force # of rails from 3-7")
print()
brute_force_decode("F daS-eefn  n KZ3eheadty.YI8lta oiwy-Q0. r aI2", 3, 7)

print()
print()
decode("5e 48 57 63 68 6e 5e 47 63 5e 68 67 67 69 67 67 47 68 5e 47 68 57 26 a6 94 26 95 67 55 26 45 e7 56 f6 a6 a6 94 83 24 23 96 e6 34 47 24 36 15 96 16 23 54 a6 55 87 94 67 24 56 a6 a6 94 83 24 c7 a6 d3 59 5f 43 49 43 67 59 65 40 48 6a 77 57 46 4f 72 46 57 59 71 65 3d", 3)
