"""
Author: Minh T. Nguyen
2/9/2021
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import math


def intXform4e(f, mode="negative", param=0):
    """
    Function that do 3 modes of intensity transformation
    @param  f = the image
            mode = negative, log, gamma
            param = for gamma mode
    """
    if mode == "negative":
        print("Negative mode")
        h, w, _ = f.shape
        out_img = np.zeros(f.shape)
        for m in range(0, h - 1):
            for n in range(0, w - 1):
                pixColorValues = f[m, n]

                pixColorValues[0] = 1 - pixColorValues[0]  # Red
                pixColorValues[1] = 1 - pixColorValues[1]  # green
                pixColorValues[2] = 1 - pixColorValues[2]  # blue

                out_img[m, n] = pixColorValues
        return out_img

    elif mode == "log":
        print("Log Mode")
        h, w, _ = f.shape
        out_img = np.zeros(f.shape)
        for m in range(0, h - 1):
            for n in range(0, w - 1):
                pixColorValues = f[m, n]

                pixColorValues[0] = 1 * math.log(pixColorValues[0] + 1)  # Red
                pixColorValues[1] = 1 * math.log(pixColorValues[1] + 1)  # green
                pixColorValues[2] = 1 * math.log(pixColorValues[2] + 1)  # blue

                out_img[m, n] = pixColorValues
        return out_img

    elif mode == "gamma":
        print("Gamma Mode")
        h, w, _ = f.shape
        out_img = np.zeros(f.shape)
        for m in range(0, h - 1):
            for n in range(0, w - 1):
                pixColorValues = f[m, n]

                pixColorValues[0] = pixColorValues[0] ** param  # Red
                pixColorValues[1] = pixColorValues[1] ** param  # green
                pixColorValues[2] = pixColorValues[2] ** param  # blue

                out_img[m, n] = pixColorValues
        return out_img
    else:
        print("Please choose negative, log , or gamma mode")


def main():
    img = cv.imread("spillway-dark.tif")
    cv.imshow("Spillway Unnormalize", img)
    normalized_img1 = cv.normalize(
        img, None, alpha=0, beta=1, norm_type=cv.NORM_MINMAX, dtype=cv.CV_32F
    )
    normalized_img2 = cv.normalize(
        img, None, alpha=0, beta=1, norm_type=cv.NORM_MINMAX, dtype=cv.CV_32F
    )

    cv.imshow("Normalized Spillway", normalized_img1)

    # From the histogram, we can see that the image has been normalized to 0-1
    plt.hist(normalized_img1.ravel(), 256, [0, 1])
    plt.show()

    # Work
    a = intXform4e(normalized_img1)
    cv.imshow("Negated Spillway", a)

    b = intXform4e(normalized_img2, "log")
    cv.imshow("Log Spillway", b)

    c = intXform4e(b, "gamma", 0.70)  # Show more details
    cv.imshow("Gamma Spillway", c)

    cv.waitKey(0)


if __name__ == "__main__":
    main()
