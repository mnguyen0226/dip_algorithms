"""
Author: Minh T. Nguyen
Lowpass filtering in the frequency domain. 
Read the image testpattern1024.tif. 
Lowpass filter it using a Butterworth filter of your specification so that, 
when thresholded, the filtered images contains only part of the large square on the top, right.
"""

import math
import cv2 as cv
import numpy as np


def get_butterworth_low_pass_filter(shape, cutoff, order):
    """ Computer the butterworth lowpass mask
    @param:
    1.shape: The shape of the mask to be generated
    2.cutoff: tje cutoff frequency of the butterworth filter
    3.order: The order of the butterworthy filter

    @return:
    a butterworth lowpass mask
    """
    d0 = cutoff
    n = order
    rows, cols = shape
    mask = np.zeros((rows, cols))
    mid_row, mid_col = int(rows / 2), int(cols / 2)
    for i in range(rows):
        for j in range(cols):
            d = math.sqrt((i - mid_row) ** 2 + (j - mid_col) ** 2)
            mask[i, j] = 1 / (1 + (d / d0) ** (2 * n))
    return mask


def post_process_image(image):
    """Post process the image to craeate  a full constrast streach of the image
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
            if d - c == 0:
                out_im[i, j] = ((b - a) / 0.000001) * (image[i, j] - c) + a
            else:
                out_im[i, j] = ((b - a) / (d - c)) * (image[i, j] - c) + a

    return np.uint8(out_im)


def main():
    im = cv.imread("testpattern1024.tif", 0)

    # 1. Input the image and obtain the padding size
    im = cv.copyMakeBorder(im, 512, 512, 512, 512, cv.BORDER_CONSTANT, value=0)
    cv.imshow("Original", im[512:1535, 512:1535])

    # 2. Inverse the image
    im = -im

    shape = np.shape(im)
    cutoff_freq = 8
    order = 2

    # 3. Computer the fft of the image
    fft = np.fft.fft2(im)

    # 4. Shift the fft to the center of the low frequencies
    shift_fft = np.fft.fftshift(fft)

    # 5. Get the mask
    mask = get_butterworth_low_pass_filter(shape, cutoff_freq, order)

    # 6. Filter the image frequency based on the mask
    filtered_image = np.multiply(mask, shift_fft)
    mag_filtered_dft = np.log(np.abs(filtered_image) + 1)
    filtered_dft = post_process_image(mag_filtered_dft)

    # 7. Compute the inverest shift
    shift_ifft = np.fft.ifftshift(filtered_image)

    # 8. Compute the inverse fourier transform
    ifft = np.fft.ifft2(shift_ifft)

    # 9. Compute the magnitude
    mag = np.abs(ifft)

    # 10. full contrast stretch
    filtered_image = post_process_image(mag)

    # 11. Get the threshold for the output
    _, th3 = cv.threshold(filtered_image, 200, 255, cv.THRESH_BINARY)

    cv.imshow("Butterworth LPF", th3[512:1535, 512:1535])

    cv.waitKey(0)
    cv.destroyAllWindows()  # Allow to press enter to delete all


if __name__ == "__main__":
    main()
