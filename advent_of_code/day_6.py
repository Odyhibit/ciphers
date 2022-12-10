def test(word: str, match: int):
    result = set()
    for letter in word:
        result.add(letter)
    if len(result) == match:
        print(f"testing {word} it is {len(result)} long")
        return True
    return False


marker_length = 14  # change this to 4 to get answer for part 1
with open("input/day_6.txt", "r") as streams:
    for stream in streams:
        str_part = stream[0:marker_length]
        for i in range(marker_length, len(stream) + 1):
            if test(str_part, marker_length):
                print(i)
                break
            str_part = str_part[1:marker_length] + stream[i]
