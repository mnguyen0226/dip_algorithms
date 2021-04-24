"""
ECE 4580 - HW4
Name: Minh T. Nguyen
Question 1: Lowpass Filtering
"""
import cv2 as cv
import numpy as np
from matplotlib import pyplot as pl
import math

# TODO 1b/ Lowpass filter it using Gaussian Kernel of your specification so that,
#  when thresholded, the filtered image contains only part of the large square on top right
def main():
    print("Running")
    im = cv.imread("testpattern1024.tif")
    im = -im # reverse the mage

    cv.imshow(" Reversed Original ", im) # Show the reversed image

    blur = cv.GaussianBlur(im, (155 ,155), 0)
    
    _,th3 = cv.threshold(blur, 200, 255, cv.THRESH_BINARY)

    cv.imshow("1b - Gaussian Kernal Blur", blur) # Show gaussian blur image
    cv.imshow("1b - Threshold Gaussian", th3) # Show the thresholded gaussian image

    cv.waitKey(0)

if __name__ == "__main__":
    main()