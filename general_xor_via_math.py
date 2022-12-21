import string


def main():
    plain_text = 127
    key = 198
    base = 5

    math_functions = [difference, analytical, no_carry_addition]
    for func in math_functions:
        test(plain_text, key, base, func, plain_text, key, base)


def get_digit_lists(p: int, q: int, number_base: int) -> ():
    """Returns a list for each number with the least significant digit first. In the number_base chosen.
    The smaller number is padded with zeros. The returned lists have the SAME LENGTH"""
    p_list = []
    q_list = []
    while p > 0 or q > 0:
        p_digit = p % number_base
        q_digit = q % number_base
        p_list.append(p_digit)
        q_list.append(q_digit)
        p //= number_base
        q //= number_base
    return p_list, q_list


def get_digits_single(p: int, number_base: int):
    """Returns a list with the least significant digit first. In the number_base chosen."""
    p_list = []
    while p > 0:
        p_digit = p % number_base
        p_list.append(p_digit)
        p //= number_base
    return p_list


def to_base(p: int, number_base: int) -> str:
    symbols = string.digits + string.ascii_uppercase   # add more symbols here for number base > 36
    p_list = get_digits_single(p, number_base)[::-1]
    return "".join(symbols[i] for i in p_list)


def math_xor(p: int, q: int, number_base: int, math_operator) -> int:
    p_list, q_list = get_digit_lists(p, q, number_base)
    accumulator = 0
    for i in range(len(p_list)):
        accumulator += math_operator(p_list[i], q_list[i], number_base) * number_base ** i
    return accumulator


def no_carry_addition(p: int, q: int, number_base: int) -> int:
    return (p + q) % number_base


def difference(p: int, q: int, number_base: int) -> int:
    return abs(p - q) % number_base


def analytical(p: int, q: int, number_base: int) -> int:
    return ((p + q) - (2 * p * q)) % number_base


def test(p: int, q: int, number_base: int, math_function: string, plain_text, key, base):
    print()
    print(math_function.__name__)
    print(f"Base:{number_base}  plaintext:{to_base(p, number_base)}  key:{to_base(q, number_base)}")
    temp = math_xor(plain_text, key, base, math_function)
    print("1 time  ", to_base(temp, number_base))
    for i in range(number_base - 1):
        temp = math_xor(temp, key, base, math_function)
        print(i + 2, "times ", to_base(temp, number_base), end="")
        if temp == plain_text:
            print("  \tmatch")
        else:
            print()


if __name__ == "__main__":
    main()
