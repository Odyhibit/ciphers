def test_next_chr(input_text, index, count=1):
    if index + 1 >= len(input_text):
        return str(count) + input_text[index]
    if input_text[index] == input_text[index + 1]:
        count += 1
        return test_next_chr(input_text, index + 1, count)
    else:
        return str(count) + input_text[index]


def run_length_encoding(input_text, index=0):
    output = ""
    while index < len(input_text):
        this_cluster = test_next_chr(input_text, index)
        output += this_cluster
        index = int(index) + int(this_cluster[:-1])
    return output


def get_next_num(input_text: str, index=0):
    number_string = ""
    while index < len(input_text):
        if input_text[index].isdigit():
            number_string += input_text[index]
        else:
            return int(number_string)
        index += 1


def run_length_decoding(input_text, index=0):
    output = ""
    while index < len(input_text):
        multiplier = get_next_num(input_text, index)
        index += len(str(multiplier))
        character = input_text[index]
        index += 1
        output += character * multiplier
    return output


print(get_next_num("10d"))

tests = ["AAAABBBCCDAA", "hhhheelllooo", "AAAAAAAAAAAABBBBBBBCCCC"]
for test in tests:
    print(test, " -> ", run_length_encoding(test))
    print(run_length_decoding(run_length_encoding(test)), " <- ", run_length_encoding(test), )
    print()
