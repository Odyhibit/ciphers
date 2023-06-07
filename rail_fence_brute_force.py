red = "\u001b[31m"
orange = "\u001b[38:5:208m"
yellow = "\u001b[38:5:227m"
green = "\u001b[32m"
blue = "\u001b[34m"
indigo = "\u001b[38:5:93m"
violet = "\u001b[38:5:54m"
reset = "\u001b[0m"
rainbow = [red, orange, yellow, green, blue, indigo, violet]


def decode(cipher_str: str, rails: int, offset: int = 0):
    cipher = cipher_str.replace(" ", "_")
    period: int = 2 * (rails - 1)
    index = offset
    rail_fence = [[] for _ in range(rails)]
    for row in range(rails):
        for i in range(len(cipher)):
            if i % period == row or period - (i % period) == row:
                rail_fence[row].append(cipher[index])
                index += 1
            else:
                rail_fence[row].append(" ")
    return visual_to_text(rail_fence).replace("_", " "), rail_fence


def visual_to_text(fence):
    out = ""
    for col in range(len(fence[0])):
        for row in range(len(fence)):
            if fence[row][col] != " ":
                out += fence[row][col]
    return out


def load_word_list(path: str) -> []:
    with open(path, "r") as common_words:
        common_word_list = []
        while line := common_words.readline():
            common_word_list.append(line.strip())
        return common_word_list


def list_to_string(character_list: list) -> str:
    return "".join(character_list)


def display_rainbow_rails(fence: []):
    for i, rail in enumerate(fence):
        print(rainbow[i], list_to_string(rail), reset)


def display_rainbow_plaintext(fence: []):
    print(" ", end="")
    for col in range(len(fence[0])):
        for row in range(len(fence)):
            print(rainbow[row], end="")
            if fence[row][col] == "_":
                print(" ", end="")
            elif fence[row][col] != " ":
                print(fence[row][col], end="")
    print(reset)


cipher = "Tnex g hec xetsjn rtitenat iuiuoesn am t sesfsg ei pehttbe tnssla di"
common_word_list = load_word_list("common_words_min_3_letters.txt")
highest_word_count = 0
row_candidate = 0
offset_candidate = 0

for key in range(2, len(cipher) // 2 + 4):
    period = 2 * (key - 1)
    for offset in range(period):
        word_count = 0
        candidate, rails = decode(cipher, key)
        for word in common_word_list:
            if word in candidate:
                word_count += 1
        if word_count > highest_word_count:
            highest_word_count = word_count
            row_candidate = key
            offset_candidate = offset
        #  print(f"if there are {i} rows the word count is {word_count}")

print(f"Looks like the row count is most likely {row_candidate} with offset {offset_candidate}")
plaintext, rails = decode(cipher, row_candidate, offset_candidate)

display_rainbow_rails(rails)
display_rainbow_plaintext(rails)

