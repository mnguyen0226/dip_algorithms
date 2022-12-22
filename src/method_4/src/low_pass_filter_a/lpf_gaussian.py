"""
Author: Minh T. Nguyen
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as pl
import math


def main():
    #  Using Gaussian kernel large enouth to blue the image so that the large letter a is barely readble, and other letter is not
    im = cv.imread("testpattern1024.tif")
    cv.imshow("Test Pattern Original", im)  # Show the original image

    blur = cv.GaussianBlur(im, (155, 155), 0)

    cv.imshow("1a - Gaussian Kernal Blur", blur)  # Show the Gaussian blurred imamge

    cv.waitKey(0)


if __name__ == "__main__":
    main()
