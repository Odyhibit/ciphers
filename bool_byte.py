

def bits_to_byte(bits):
    byte  = bits[0] << 7
    byte += bits[1] << 6
    byte += bits[2] << 5
    byte += bits[3] << 4
    byte += bits[4] << 3
    byte += bits[5] << 2
    byte += bits[6] << 1
    byte += bits[7] << 0
    return byte

bits = [False, False, False, False, True, False, False, False]
num = 0
for i, bit in enumerate(bits):
    num += bit << 7 - i
print(num)
print(bits_to_byte(bits))

