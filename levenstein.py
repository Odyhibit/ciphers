def test_next_chr(original, target, i, j, match):
    if i >= (len(original) - 1) or j >= (len(target) - 1):
        return match
    if original[i + 1] == target[j + 1]:
        match += original[i + 1]
        return test_next_chr(original, target, i + 1, j + 1, match)
    else:
        return match


def find_longest_substring(original: str, target: str) -> str:
    current_longest = ""
    for i, original_char in enumerate(original):
        for j, target_char in enumerate(target):
            if original[i] == target[j]:
                testing = test_next_chr(original, target, i, j, original[i])
                if len(testing) > len(current_longest):
                    current_longest = testing
    return current_longest


def get_left(input_string, substring):
    return input_string[:input_string.find(substring)]


def get_right(input_string, substring):
    return input_string[input_string.find(substring) + len(substring):]


def distance(original, target, start_dist=0):
    longest_substring = find_longest_substring(original, target)
    if longest_substring == "":
        return start_dist + max(len(original), len(target))
    else:
        new_orig_left = get_left(original, longest_substring)
        new_targ_left = get_left(target, longest_substring)
        new_orig_right = get_right(original, longest_substring)
        new_targ_right = get_right(target, longest_substring)
        return start_dist + distance(new_orig_left, new_targ_left, start_dist) + distance(new_orig_right,
                                                                                          new_targ_right, start_dist)


originals = ["store", "apple", "nifty", "kitten", "eelephant", "opossum", "abc"]
targets = ["sore", "bapple", "stiff", "sitting", " elephants", " possums", "xyz"]

for i, word in enumerate(originals):
    print(f"The distance between {originals[i]} and {targets[i]} is {distance(originals[i], targets[i])}")
