"""
Find the next smallest power of 2 that contains the target number
works for numbers less than 2**16 (65536)

"""


def next_higher_power_of_two(target_num: int) -> int:
    target_num -= 1
    target_num |= target_num >> 1
    target_num |= target_num >> 2
    target_num |= target_num >> 4
    # target_num |= target_num >> 8
    # target_num |= target_num >> 16
    target_num += 1
    return target_num


def encompassing_power_of_two(target_num: int) -> int:
    target_num -= 1
    num_bits = 1
    bit_block = target_num >> num_bits
    while bit_block:
        target_num |= bit_block
        num_bits *= 2
        bit_block = target_num >> num_bits
    return target_num + 1

print("next higher")
print(next_higher_power_of_two(35))
print(next_higher_power_of_two(16))
print(next_higher_power_of_two(12345))
print(next_higher_power_of_two(123456789012345678901234567890))

print("encompassing")
print(encompassing_power_of_two(35))
print(encompassing_power_of_two(16))
print(encompassing_power_of_two(12345))
print(encompassing_power_of_two(123456789012345678901234567890))
