from PIL import Image
import numpy as np


def main():
    path = input("Enter image to be scrambled: ")
    im = Image.open(path, 'r')
    pix_val = list(im.getdata())
    shift = list(map(int, input("Shift vector in form R G B: ").split()))
    pix_val = np.mod(np.add(pix_val, shift), [256, 256, 256])
    new_im = Image.new(im.mode, im.size)
    new_im.putdata(list(map(tuple, pix_val)))
    new_im.show()


if __name__ == "__main__":
    main()
