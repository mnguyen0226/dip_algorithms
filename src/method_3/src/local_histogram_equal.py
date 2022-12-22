"""
Author: Minh T. Nguyen
"""

import cv2 as cv
import numpy as np
import math
from matplotlib import pyplot as plt


def localHisEqual4e2(f, m, n):
    """
        perform local histogram equalization of 
        8 bit grayscale image f based on the neighborhood of size mxn
        Use replicate padding to pad the image border
        Note: The value of the image is already 8 bit
    """
    h, w = f.shape
    out_img = np.ones(f.shape)
    mid_val = math.ceil((m * n) / 2)
    PadM = 0
    PadN = 0
    ele = 0
    pos = 0

    # Find the number of rows and col to be padded with 0
    num = 0  # pad number
    for i in range(m):
        for j in range(n):
            num = num + 1
            if num == mid_val:
                PadM = i - 1
                PadN = j - 1

    for i in range(h - PadM * 2 - 1):
        for j in range(h - PadN * 2 - 1):
            cdf = np.zeros(256)
            inc = 1
            for x in range(m):
                for y in range(n):
                    if inc == mid_val:
                        ele = f[i + x - 1, j + y - 1] + 1

                    pos = f[i + x - 1, j + y - 1] + 1
                    cdf[pos] = cdf[pos] + 1
                    inc = inc + 1

            # Computer cdf for value in the windeow
            for l in range(1, 255):
                cdf[l] = cdf[l] + cdf[l - 1]
            out_img[i, j] = math.ceil(cdf[ele] / (m * n) * 255)
    out_img = cv.copyMakeBorder(out_img, m, m, n, n, cv.BORDER_REPLICATE)

    return out_img


def main():
    f = plt.imread("hidden-symbols.tif")
    print(f"The shape of origin is {f.shape}")
    plt.imshow(f, cmap="gray")
    plt.title("Original", fontweight="bold")
    plt.show()

    out1 = localHisEqual4e2(f, 3, 3)
    print(f"The shape of 3x3 is {out1.shape}")
    cv.imshow("Output 3x3", out1.astype(np.uint8))

    f2 = plt.imread("hidden-symbols.tif")
    out2 = localHisEqual4e2(f2, 7, 7)
    print(f"The shape of 7x7x is {out2.shape}")
    cv.imshow("Output 7x7", out2.astype(np.uint8))

    print("Finish")
    cv.waitKey(0)


if __name__ == "__main__":
    main()
