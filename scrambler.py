from PIL import Image
import random


def main():
    path = input("Enter image to be scrambled: ")
    im = Image.open(path, 'r')
    pix_val = list(im.getdata())
    random.shuffle(pix_val)
    new_im = Image.new(im.mode, im.size)
    new_im.putdata(pix_val)
    new_im.show()


if __name__ == "__main__":
    main()
