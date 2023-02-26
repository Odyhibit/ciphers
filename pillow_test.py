from PIL import Image


def hide_bit(original: int, bit: int) -> int:
    striped = original & 0b01111111
    hidden_bit = bit << 7
    return striped + hidden_bit


with Image.open("worn.png") as img, open("final_exam.png", "rb") as hidden:
    px = img.load()
    data = hidden.read()
    b_message = [format(int(data[i]), "08b") for i in data]
    width, height = img.width, img.height
    for y in range(height):
        for x in range(width):
            if len(b_message) > 0:
                bit_to_hide = b_message.pop(0)
                image_byte = px[x, y]
                px[x, y] = hide_bit(image_byte, int(bit_to_hide))
    img.save("test.png")

    orgnl = px[100, 100]
    print(format(orgnl, "08b"))
    print(format(hide_bit(orgnl, 0), "08b"))
    print(format(hide_bit(orgnl, 1), "08b"))
