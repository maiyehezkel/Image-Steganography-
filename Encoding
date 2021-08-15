import numpy as np
from PIL import Image


#Encoding function
def Encode(src, message, dest):
    numOfchar = len(message)
    img = Image.open(src, 'r')
    width, height = img.size
    array = np.array(list(img.getdata()))

    # Improvement number 3:
    if img.mode == 'L' or img.mode == 'P':
        n = 1
    elif img.mode == 'RGB':
        print("Type RGB")
        n = 3
    elif img.mode == 'RGBA':
        print("Type RGBA")
        n = 4

    total_pixels = array.size // n

    message += "$Mai2MAI5"
    b_message = ''.join([format(ord(i), "08b") for i in message])
    req_pixels = len(b_message)

    if req_pixels > total_pixels:
        print("ERROR: Need larger file size")

    else:
        index = 0
        for p in range(total_pixels):
            if n == 1:
                if index < req_pixels:
                    array[p] = int(bin(array[p])[4:6] + b_message[index], 2)
                    index += 1
            else:
                for q in range(0, n):
                    if index < req_pixels:
                        array[p][q] = int(bin(array[p][q])[4:6] + b_message[index], 2)
                        index += 1

        if (n == 1):
            array = array.reshape(height, width)
            dest += ".gif"
        else:
            array = array.reshape(height, width, n)
            dest += ".png"

        enc_img = Image.fromarray(array.astype('uint8'), img.mode)
        enc_img.save(dest)
        count = Message_Security(dest, numOfchar)

        if count == True:
            print("All the Data Encoded Successfully")
        else:
            print("Data lost in the process: ", numOfchar, "charters")


def Message_Security(src, numOfchar):
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
        message = message[:-9]
        if numOfchar == len(message):
            return True
    else:
        return numOfchar - len(message)





def Menu():
    print("Welcome to Image Steganography Based on Local Variance")
    print("1: Encode")
    print("2: Exit")
    func = input()

    if func == '1':
        src = input("Enter Name Of Image (inside your project folder):")
        message = input("Enter Message to Hide:")
        dest = "2"
        print("Encoding...")
        Encode(src, message, dest)
        print("")
        Menu()
    elif func == '2':
        exit(1)

    else:
        print("ERROR: Invalid option chosen")
        exit(0)

Menu()
