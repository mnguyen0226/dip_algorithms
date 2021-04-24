"""
ECE 4580 - HW4
Name: Minh T. Nguyen
Question 1: Lowpass Filtering
"""
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import math

# TODO 1c/Reproduce the result in example 3.18
# Question: is the size correct? Is the technique valid?

def main():
    print("Running")
    im = cv.imread("checkerboard1024-shaded.tif")
    
    im = im.astype(float) / 255 # normalized the original image

    # resize original image
    scale_percent = 1024/64 # scale to smaller image for showing the result together
    width = int(im.shape[1] * scale_percent / 100)
    height = int(im.shape[0] * scale_percent / 100)
    dsize = (width, height)
    out = cv.resize(im, dsize)

    blur = cv.GaussianBlur(out, (55 , 55), 0) # Gaussian Blur image

    result = out/blur # result we want

    # Make sure to normalize the image
    normalized_result = cv.normalize(result, None, alpha = 0, beta = 1, norm_type = cv.NORM_MINMAX, dtype = cv.CV_32F)     # normalize to scale [0, 1]    

    blank = np.ones((163, 20, 3)) # just blank square that separate images

    together = np.concatenate((out, blank, blur, blank, normalized_result), axis=1) # concatenate result horizontally
    cv.imshow("1c", together)

    cv.imshow("Blur image", blur)

    cv.waitKey(0)
    cv.destroyAllWindows() 

if __name__ == "__main__":
    main()