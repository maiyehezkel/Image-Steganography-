import numpy as np
from PIL import Image




def Decode(src):
    img = Image.open(src, 'r')
    array = np.array(list(img.getdata()))

    if img.mode == 'L' or img.mode == 'P':
        n = 1
    elif img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4

    total_pixels = array.size // n
    hidden_bits = ""

    for p in range(total_pixels):
        if n == 1:
            hidden_bits += (bin(array[p])[2:][-1])
        else:
            for q in range(0, n):
                hidden_bits += (bin(array[p][q])[2:][-1])

    hidden_bits = [hidden_bits[i:i + 8] for i in range(0, len(hidden_bits), 8)]
    message = ""

    for i in range(len(hidden_bits)):
        if message[-9:] == "$TAL2MAI5":
            break
        else:
            message += chr(int(hidden_bits[i], 2))
    if "$TAL2MAI5" in message:
        print("Hidden Message:", message[:-9])
    else:
        print("No Hidden Message Found")


def Menu():
    print("Welcome to Image Steganography Based on Local Variance")
    print("1: Decode")
    print("2: Exit")
    func = input()

    if func == '1':
        src = input("Enter Image Name (2.png/2.gif): ")
        print("Decoding...")
        Decode(src)
        print("")
        Menu()

    elif func == '2':
        exit(1)
    else:
        print("ERROR: Invalid option chosen")
        exit(0)

Menu()
