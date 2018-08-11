from PIL import Image

IMG = "C:\\Users\\typeo\\Pictures\\Saved Pictures\\BULOGO.jpg"
WIDTH = 80
HEIGHT = 35
OUTPUT = "C:\\Users\\typeo\\Pictures\\Saved Pictures\\output.txt"

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    return ascii_char[int(gray * length / 257)]


if __name__ == '__main__':
    im = Image.open(IMG)
    im = im.resize((WIDTH, HEIGHT), Image.ANTIALIAS)

    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'

    # Output the image
    try:
        with open(OUTPUT, 'w') as f:
            f.write(txt)
        print("success")
    except:
        print(txt)
