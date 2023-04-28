"""
Find the next smallest power of 2 that contains the target number
works for numbers less than 2**16 (65536)

"""


def next_higher_power_of_two(target_num: int) -> int:
    target_num -= 1
    target_num |= target_num >> 1
    target_num |= target_num >> 2
    target_num |= target_num >> 4
    target_num |= target_num >> 8
    target_num |= target_num >> 16
    target_num += 1
    return target_num


print(next_higher_power_of_two(35))
print(next_higher_power_of_two(16))
print(next_higher_power_of_two(12345))
