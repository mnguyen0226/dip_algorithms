"""
Author: Minh T. Nguyen
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as pl
import math
from skimage.filters import gaussian
from skimage import io, img_as_float


def main():
    im = img_as_float(io.imread("blurry-moon.tif", as_gray=True))

    gaussian_img = gaussian(im, sigma=2, mode="constant", cval=0.0)
    im2 = (im - gaussian_img) * 5
    im3 = im + im2

    cv.imshow("Original", im)
    cv.imshow("Testing", im3)

    cv.waitKey(0)


if __name__ == "__main__":
    main()
