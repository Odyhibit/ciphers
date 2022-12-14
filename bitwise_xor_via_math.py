import random


def no_carry_addition(p: int, q: int) -> int:
    accumulator = 0
    for i in range(max(p.bit_length(), q.bit_length())):
        bit = 2 ** i
        accumulator += (p & bit) + (q & bit) & bit
    return accumulator


one = random.randrange(0, 4084, 1)
two = random.randrange(0, 9999, 1)
print(f"{one}, {two} -> {no_carry_addition(one, two) == one ^ two} ")

'''
#  test all 8-bit numbers
for first_num in range(256):
    for second_num in range(256):
        ex_oar = no_carry_addition(first_num, second_num)
        xor = first_num ^ second_num
        if ex_oar != xor:
            print(f"no_carry_addition is {ex_oar} real xor is {xor}")
'''