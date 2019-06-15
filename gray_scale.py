from color import Color
from PIL import Image

def main():
    path = input("Enter image to be 'grayed': ")
    im = Image.open(path, 'r')
    pix_val = list(im.getdata())
    pix_val_prime = list(map(Color.tuple,
                         map(Color.toGray,
                         map(Color.colorFromTuple, pix_val))))
    new_im = Image.new(im.mode, im.size)
    new_im.putdata(pix_val_prime)
    new_im.show()

if __name__ == "__main__":
    main()
