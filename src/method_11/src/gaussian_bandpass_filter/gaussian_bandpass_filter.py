"""
Author: Minh T. Nguyen
3/19/2021 

Filtering in the Frequency Domain
Write the function bpFilterTF4e(type,M,N,C0,W) for performing bandpass filtering where type refers to either Ideal or Gaussian

ACTIVATE GAUSSIAN BANDPASS FILTER
"""

import math
import cv2 as cv
import numpy as np
from skimage.util import random_noise


def bgFilterTF4e(type, M, N, C0, W):
    """
    Filter in the frequency domain
    @param:
    1. type: can be gaussian or ideal
    2. M = row
    3. N = col
    4. W = the W value

    @return
    The mask of the Gaussian or ideal
    """
    if type == "Gaussian":
        d0 = C0
        # rows, cols = shape
        rows = M
        cols = N

        mask = np.zeros((rows, cols))
        mid_row, mid_col = int(rows / 2), int(cols / 2)
        for i in range(rows):
            for j in range(cols):
                d = math.sqrt((i - mid_row) ** 2 + (j - mid_col) ** 2)
                if d == 0:
                    mask[i, j] = np.exp(-(((d * d - d0 * d0) / (0.000001 * W)) ** 2))
                else:
                    mask[i, j] = np.exp(-(((d * d - d0 * d0) / (d * W)) ** 2))
        return mask

    elif type == "Ideal":
        d0 = C0
        rows = M
        cols = N

        mask = np.zeros((rows, cols))
        mid_row, mid_col = int(rows / 2), int(cols / 2)
        for i in range(rows):
            for j in range(cols):
                d = math.sqrt((i - mid_row) ** 2 + (j - mid_col) ** 2)
                lower_range = d0 - W / 2
                upper_rangge = d0 + W / 2
                if d >= lower_range and d <= upper_rangge:
                    mask[i, j] = 1
                else:
                    mask[i, j] = 0
        return mask


def post_process_image(image):
    """Post process the image to create a full constrast stretch of the image
    @param:
    The image after inverse fourier transform

    @return:
    The image with full contrast stretch
    """
    a = 0
    b = 255
    c = np.min(image)
    d = np.max(image)
    rows, cols = np.shape(image)
    out_im = np.zeros((rows, cols), dtype=int)
    for i in range(rows):
        for j in range(cols):
            if d - c == 0:  # avoid to have d-c = 0 which give infinite answer
                out_im[i, j] = ((b - a) / 0.000001) * (image[i, j] - c) + a
            else:
                out_im[i, j] = ((b - a) / (d - c)) * (image[i, j] - c) + a

    return np.uint8(out_im)


def main():
    im = cv.imread("testpattern1024.tif", 0)

    # 1. Input the image and obtain the padding size
    im = cv.copyMakeBorder(
        im, 512, 512, 512, 512, cv.BORDER_CONSTANT, value=0
    )  # make sure to pad
    cv.imshow("Original", im[512:1535, 512:1535])

    # 2. Generate the Gaussian noise
    gauss = np.random.normal(0, 1, im.size)
    gauss = gauss.reshape(im.shape[0], im.shape[1]).astype("uint8")

    # Add the Gaussian noise to the image
    im = cv.add(im, gauss)
    cv.imshow("Noise-corrupted Image", im[512:1535, 512:1535])

    # 3. Get the rows and cols of the image
    M, N = np.shape(im)

    # 4. Computer the fft of the image
    fft = np.fft.fft2(im)

    # 5. Shift the fft to the center of the low frequencies
    shift_fft = np.fft.fftshift(fft)

    # 6. Get the mask
    mask = bgFilterTF4e(type="Gaussian", M=M, N=N, C0=45, W=100)

    # 7. Filter the image frequency based on the mask
    filtered_image = np.multiply(mask, shift_fft)
    mag_filtered_dft = np.log(np.abs(filtered_image) + 1)
    filtered_dft = post_process_image(mag_filtered_dft)

    # 8. Compute the inverest shift
    shift_ifft = np.fft.ifftshift(filtered_image)

    # 9. Compute the inverse fourier transform
    ifft = np.fft.ifft2(shift_ifft)

    # 10. Compute the magnitude
    mag = np.abs(ifft)

    # 11. full contrast stretch
    filtered_image = post_process_image(mag)

    cv.imshow("Gaussian LPF Filtered Image", filtered_image[512:1535, 512:1535])

    cv.waitKey(0)
    cv.destroyAllWindows()  # Allow to press enter to delete all


if __name__ == "__main__":
    main()
