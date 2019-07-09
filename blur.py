from color import Color
from PIL import Image

GRANULARITY = 20
G_SQUARED = GRANULARITY * GRANULARITY

def main():
    path = input("Enter image to be 'blurred': ")
    im = Image.open(path, 'r')
    pix_val = list(im.getdata())
    #input image
    pix_val_prime = pix_val
    for i in range(int(im.size[1]/GRANULARITY)):
        for j in range(int(im.size[0]/GRANULARITY)):
            totalR = 0
            totalG = 0
            totalB = 0
            for x in range(GRANULARITY):
                for y in range(GRANULARITY):
                    tup = pix_val[(i*GRANULARITY + x)*im.size[0] + (j * GRANULARITY + y)]
                    totalR += tup[0]
                    totalG += tup[1]
                    totalB += tup[2]

            blur_tup = (int(totalR/G_SQUARED), int(totalG/G_SQUARED),int(totalB/G_SQUARED))
            for x in range(GRANULARITY):
                for y in range(GRANULARITY):
                    pix_val_prime[(i*GRANULARITY + x)*im.size[0] + (j * GRANULARITY + y)] = blur_tup
    new_im = Image.new(im.mode, im.size)
    new_im.putdata(pix_val_prime)
    new_im.show()


if __name__ == "__main__":
    main()
