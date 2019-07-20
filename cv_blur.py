import cv2 as cv

from color import Color
from PIL import Image

GRANULARITY = 10
G_SQUARED = GRANULARITY * GRANULARITY

def main():
    path = input("Enter image to be 'blurred': ")
    #im = Image.open(path, 'r')
    #pix_val = list(im.getdata())
    face_cascade = cv.CascadeClassifier()
    if not face_cascade.load(cv.samples.findFile("haarcascade_frontalface_alt.xml")):
        print('--(!)Error loading face cascade')
        exit(0)
    cv_im = cv.imread(path)
    im = Image.open(path, 'r')
    pix_val = list(im.getdata())
    faces = face_cascade.detectMultiScale(cv_im)

    for (a, b, w, h) in faces:
        #print("FACE FOUND!")
    #input image
        pix_val_prime = pix_val
        #print(a)
        #print(b)
        for i in range(int(h/GRANULARITY)):
            for j in range(int(w/GRANULARITY)):
                totalR = 0
                totalG = 0
                totalB = 0
                for x in range(GRANULARITY):
                    for y in range(GRANULARITY):
                        tup = pix_val[(b + i*GRANULARITY + x)*im.size[0] + (a + j * GRANULARITY + y)]
                        totalR += tup[0]
                        totalG += tup[1]
                        totalB += tup[2]

                blur_tup = (int(totalR/G_SQUARED), int(totalG/G_SQUARED),int(totalB/G_SQUARED))
                for x in range(GRANULARITY):
                    for y in range(GRANULARITY):
                        pix_val_prime[(b + i*GRANULARITY + x)*im.size[0] + (a + j * GRANULARITY + y)] = blur_tup
        new_im = Image.new(im.mode, im.size)
        new_im.putdata(pix_val_prime)

    new_im.show()


if __name__ == "__main__":
    main()
