"""
Author: Minh T. Nguyen
Lowpass filtering in the frequency domain.
Read the image testpattern1024.tif and lowpass filtering it using a Gaussian 
filter so that the large letter “a” is barely readable, and the other letters are not
"""

import math
import cv2 as cv
import numpy as np


def get_gaussian_low_pass_filter(shape, cutoff):
    """ Computer the gaussian low pass mask 
    @param:
    1. shape: the shape of the mask to be generated
    2. cutoff: the cutoff frequency of the gaussian filter / sigma
        
    @return:
    the gaussian lowpass mask in frequency domain
    """
    d0 = cutoff
    rows, cols = shape
    mask = np.zeros((rows, cols))
    mid_row, mid_col = int(rows / 2), int(cols / 2)
    for i in range(rows):
        for j in range(cols):
            d = math.sqrt((i - mid_row) ** 2 + (j - mid_col) ** 2)
            mask[i, j] = np.exp(-(d * d) / (2 * d0 * d0))
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

    shape = np.shape(im)
    cutoff_freq = 15

    # 2. Computer the fft of the image
    fft = np.fft.fft2(im)

    # 3. Shift the fft to the center of the low frequencies
    shift_fft = np.fft.fftshift(fft)

    # 4. Get the mask
    mask = get_gaussian_low_pass_filter(shape, cutoff_freq)

    # 5. Filter the image frequency based on the mask
    filtered_image = np.multiply(mask, shift_fft)
    mag_filtered_dft = np.log(np.abs(filtered_image) + 1)
    filtered_dft = post_process_image(mag_filtered_dft)

    # 6. Compute the inverest shift
    shift_ifft = np.fft.ifftshift(filtered_image)

    # 7. Computer the inverse fourier transform
    ifft = np.fft.ifft2(shift_ifft)

    # 8. Compute the magnitude
    mag = np.abs(ifft)

    # 9. full contrast stretch
    filtered_image = post_process_image(mag)

    cv.imshow("Gaussian LPF", filtered_image[512:1535, 512:1535])

    cv.waitKey(0)
    cv.destroyAllWindows()  # Allow to press enter to delete all


if __name__ == "__main__":
    main()
