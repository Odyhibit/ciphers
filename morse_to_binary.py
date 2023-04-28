binary_representation = {".": "10", "-": "1110", "_": "1110", " ": "00", "/": "0000"}
morse_example = "-- --- .-. ... . / -.-. --- -.. . / .. ... / -- .- -.. . / ..- .--. / --- ..-. / -.. --- - ... / -.. " \
                ".- ... .... . ... --..-- / .- -. -.. / --. .- .--. ... .-.-.- "


def morse_str_to_bin_str(morse_str: str) -> str:
    binary_str = ""
    for char in morse_example:
        binary_str += binary_representation[char]
    binary_str += "0" * (8 - (len(binary_str) % 8))
    return binary_str


def bin_str_to_bytearray(binary_str: str) -> []:
    byte_array = bytearray()
    for byte_index in range(0, len(binary_str), 8):
        start = byte_index
        byte_array.append(int(binary_str[start: start + 8], 2))
    return byte_array



bin_str = morse_str_to_bin_str(morse_example)
print(f"The binary string is {len(bin_str)} character long. Mod 8 is {len(bin_str) % 8}")
print(bin_str)
bin_output = bin_str_to_bytearray(bin_str)
print(bin_str_to_bytearray(bin_str))
with open("morse_bin_output", "wb") as output:
    output.write(bin_output)
