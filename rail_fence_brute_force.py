def decode(cipher_str, rails):
    cipher = list(cipher_str.replace(" ", "_"))
    period: int = 2 * (rails - 1)
    index = 0
    rail_fence = [[] for _ in range(rails)]
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
    return visual_to_text(rail_fence)


def print_rail_fence(fence):
    for i, rail in enumerate(fence):
        print(rail)


def visual_to_text(fence):
    out = ""
    for col in range(len(fence[0])):
        for row in range(len(fence)):
            if fence[row][col] != " ":
                out += fence[row][col]
    return out


print(decode("Tnex g hec xetsjn rtitenat iuiuoesn am t sesfsg ei pehttbe tnssla di", 6).replace("_"," "))

print(int(True), int(False))
print(14//6, 14 % 6)