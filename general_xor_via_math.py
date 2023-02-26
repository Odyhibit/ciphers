import string


def main():
    plain_text = 139
    key = 127
    base = 64

    math_functions = [difference, analytical, no_carry_addition, square_of_difference]
    for func in math_functions:
        test_1(func, plain_text, key, base)
    test_analytical(base)


def get_digits(p: int, number_base: int) -> [int]:
    """Returns a list with the least significant digit first. In the number_base chosen."""
    p_list = []
    while p > 0:
        p_digit = p % number_base
        p_list.append(p_digit)
        p //= number_base
    return p_list


def to_base(p: int, number_base: int) -> str:
    """Returns a string version of a number in a specific base. Used for displaying number"""
    symbols = string.digits + string.ascii_uppercase + string.ascii_lowercase + "*@"  # add more symbols here (64)
    p_list = get_digits(p, number_base)[::-1]
    return "".join(symbols[i] for i in p_list)


def math_xor(p: int, q: int, number_base: int, math_operator) -> int:
    """Returns the result of the given math_operator in the provided number base"""
    p_list = get_digits(p, number_base)
    q_list = get_digits(q, number_base)
    accumulator = 0
    longest_list = max(len(p_list), len(q_list))
    p_list = fill_zero_to(p_list, longest_list)
    q_list = fill_zero_to(q_list, longest_list)
    p_length = len(p_list)
    q_length = len(q_list)
    for i in range(max(p_length, q_length)):
        accumulator += math_operator(p_list[i], q_list[i], number_base) * number_base ** i
    return accumulator


def no_carry_addition(p: int, q: int, number_base: int) -> int:
    return (p + q) % number_base


def square_of_difference(p: int, q: int, number_base: int) -> int:
    return ((p - q) ** 2) % number_base


def difference(p: int, q: int, number_base: int) -> int:
    return abs(p - q) % number_base


def analytical(p: int, q: int, number_base: int) -> int:
    return ((p + q) - (2 * p * q)) % number_base


def fill_zero_to(lst: [int], num: int) -> [int]:
    """Returns a list that is extended to length of num padded with 0 if it is shorter."""
    if len(lst) >= num:
        return lst
    for i in range(len(lst), num):
        lst.append(0)
    return lst


def test_1(math_function: string, plain_text, key, base):
    print()
    print(math_function.__name__)
    print(f"Base:{base}  plaintext:{to_base(plain_text, base)}  key:{to_base(key, base)}")
    temp = math_xor(plain_text, key, base, math_function)
    print(f"1 time  {to_base(temp, base): >8}")
    for i in range(base - 1):
        temp = math_xor(temp, key, base, math_function)
        print(f"{i + 2} times {to_base(temp, base): >8}", end="")
        if temp == plain_text:
            print("  \tmatch")
        else:
            print()


def test_2(math_function: string, plain_text: int, key: int, base: int):
    print()
    print("Base:", base, "Plain text:", plain_text, "key:", key, "Using:", math_function.__name__)
    temp = math_xor(plain_text, key, base, math_function)
    for i in range(base - 1):
        temp = math_xor(temp, key, base, math_function)
        if temp == plain_text:
            print("After", i + 2, "iterations there is a match", temp, "==", plain_text)
            return
    print("No match")


def add_create(dictionary, key, value=1):
    if key not in dictionary:
        dictionary[key] = value
    else:
        dictionary[key] += value

def test_analytical(base):
    print("Analytical test:")
    print("Testing numbers 0-127 x 0-127, should get 16384")
    match_at = {}
    for p in range(128):
        for q in range(128):
            temp = math_xor(p, q, base, analytical)
            for i in range(base-1):
                temp = math_xor(temp, q, base, analytical)
                if temp == p:
                    add_create(match_at, i)
                    continue
    for num in match_at:
        print(num + 2, "iterations", match_at[num])

if __name__ == "__main__":
    main()
