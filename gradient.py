from color import Color
from PIL import Image

GRANULARITY = 10
SQUARE = GRANULARITY * 2 + 3

def main():
    path = input("Enter image to be 'blurred': ")
    im = Image.open(path, 'r')
    pix_val = list(im.getdata())
    #input image
    pix_val_prime = pix_val
    for i in range(int(im.size[1])):
        for j in range(int(im.size[0])):
            totalR = 0
            totalG = 0
            totalB = 0
            count = 0
            for x in range(SQUARE):
                for y in range(SQUARE):
                    try:
                        tup = pix_val[(i + x - int(SQUARE/2))*im.size[0] + (j + y - int(SQUARE/2))]
                        totalR += tup[0]
                        totalG += tup[1]
                        totalB += tup[2]
                        count += 1
                    except:
                        pass
            blur_tup = (int(totalR/count), int(totalG/count),int(totalB/count))
            pix_val_prime[i*im.size[0] + j] = blur_tup
    new_im = Image.new(im.mode, im.size)
    new_im.putdata(pix_val_prime)
    new_im.show()


if __name__ == "__main__":
    main()
