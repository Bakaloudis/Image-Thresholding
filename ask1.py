import sys
import numpy as np
import matplotlib.pyplot as plt 

from PIL import Image

image = np.array(Image.open(sys.argv[1])) # opening image as an array
th = sys.argv[3]

#print(image)

if(len(image.shape)<3): # check if image is rgb or gray scale
    grayImage = image
elif len(image.shape)==3:
    grayImage = np.dot(image[...,:3], [0.2989, 0.5870, 0.1140]) # rbg to grayscale

grayImage_bool = ( grayImage > float(th) ) * 255 # mult. by 255 to make True == White and False == Black 

Image.fromarray(np.uint8(grayImage_bool)).save(sys.argv[2]) # saving the image to disk

plt.imshow(grayImage_bool, cmap="gray")  # Showing the image
plt.show()