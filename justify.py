wordlist = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
max_columns = 16
index = 0


def can_fit_one_more(this_index, words, current, maximum) -> bool:
    if current + len(words[this_index]) < maximum:
        return True
    return False


def justify_words(words, maximum_columns):
    rows = []
    this_row = []
    this_index = 0
    current_count = 0
    for word in words:
        if can_fit_one_more(this_index, wordlist, current_count, maximum_columns):
            current_count += len(word)
            this_index += 1
            this_row.append(word)

        else:
            current_count = 0
            rows.append(this_row)
            this_row = [word]
            current_count += len(word)
    rows.append(this_row)
    return rows


justified = justify_words(wordlist, max_columns)
print(justified)
for line in justified:
    print_str = " ".join(line)
    print(print_str, len(print_str))
