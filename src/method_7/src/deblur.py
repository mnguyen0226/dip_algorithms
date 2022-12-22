"""
Author: Minh T. Nguyen 
Frequency - domain filtering for Motion Deblurring
"""

import math
import cmath
import cv2 as cv
import numpy as np
import random
import scipy.fftpack as fp
from skimage.color import rgb2gray
from skimage.io import imread
from PIL import Image
import PIL
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage import color
from skimage import io


def motion_blur_mask(im, a, b, T):
    """
    Function motion blur get the mask in the prompt
    @param:
    1. im = input image
    2. a = horizontal position
    3. b = vertical position
    4. T = shifting time

    @return:
    mask = mask 
    """
    rows, cols = im.shape
    mask = np.zeros((rows, cols), dtype=np.complex64)  # is this correct?
    mid_row = im.shape[0] / 2
    mid_col = im.shape[1] / 2

    for x in range(rows):
        for y in range(cols):
            temp = np.pi * ((x - mid_row) * a + (y - mid_col) * b)
            nominator = np.sin(temp)
            if temp == 0:
                mask[x, y] = 1
            else:
                mask[x, y] = T * nominator * np.exp(-1j * temp) / temp
    return mask


def apply_mask(im, mask):
    """
    Function use Fast Fourier Transform with mask to implement the blur
    @param: 
    1. im = input image
    2. mask = mask get from the motion blur

    @return:
    out = the real part of the output image
    """
    # 1. Computer the fft of the image
    fft = np.fft.fft2(im)

    # 2. Shift the fft to the center of the low frequencies
    shift_fft = np.fft.fftshift(fft)

    # 3. Filter the image frequency based on the mask
    filtered_image = np.multiply(mask, shift_fft)

    # 4. Compute the inverest shift
    shift_ifft = np.fft.ifftshift(filtered_image)

    # 5. Compute the inverse fourier transform
    ifft = np.fft.ifft2(shift_ifft)

    out = ifft.real

    return out


def get_gaussian_noise(im, mean, var):
    """
    Function use Gaussian noise corruption
    @param:
    1. im = input image
    2. mean 
    3. var = variance

    @return 
    noisy_im = corrupted output image 
    """
    rows, cols = im.shape
    sigma = var ** 0.5
    gauss = np.random.normal(mean, sigma, (rows, cols))
    gauss = gauss.reshape(rows, cols)
    noisy_im = im + gauss
    return noisy_im


def get_pseudo_inverse_mask(im, delta, a, b, T):
    """
    Function implememnt the pseudo-inverse filter to filter the noise corrpted, blurred image
    @param:
    im = input image
    delta = delta param
    """
    rows, cols = im.shape
    mask = np.zeros((rows, cols), dtype=np.complex64)  # is this correct?
    mid_row = im.shape[0] / 2
    mid_col = im.shape[1] / 2

    for x in range(rows):
        for y in range(cols):
            temp = np.pi * ((x - mid_row) * a + (y - mid_col) * b)
            nominator = np.sin(temp)
            if temp == 0:
                mask[x, y] = 1
            else:
                mask[x, y] = T * nominator * np.exp(-1j * temp) / temp

            # pseudo_inverse mask
            if (np.abs(mask[x, y])) > delta:
                mask[x, y] = 1 / mask[x, y]
            else:
                mask[x, y] = 0
    return mask


def get_wiener_mask(im, a, b, T, var, origin_im):
    """
    Function wiener get the mask in the prompt
    @param:
    1. im = input image original
    2. a = horizontal position
    3. b = vertical position
    4. T = shifting time
    5. var = variance in the prompt

    @return:
    mask = mask 
    """
    rows, cols = im.shape
    mask = np.zeros((rows, cols), dtype=np.complex64)  # is this correct?
    mid_row = im.shape[0] / 2
    mid_col = im.shape[1] / 2
    var_im = np.var(origin_im)  # variance of the input images
    K = (var) / (var_im)

    for x in range(rows):
        for y in range(cols):
            temp = np.pi * ((x - mid_row) * a + (y - mid_col) * b)
            nominator = np.sin(temp)
            if temp == 0:
                mask[x, y] = 1
            else:
                mask[x, y] = T * nominator * np.exp(-1j * temp) / temp

            # Wiener filter
            nom = np.conj(mask[x, y])
            denom = np.abs(mask[x, y]) ** 2 + K
            mask[x, y] = nom / denom

    return mask


def main():
    im = color.rgb2gray(io.imread("cameraman.tif"))

    # 1. Input the image and obtain the padding size
    # plt.imshow(im, cmap = "gray")

    # 2. Get the mask
    a = 0.05
    b = 0.02
    T = 1
    mask = motion_blur_mask(im, a, b, T)

    # 3. Get the blur from motion mask
    out_motion_blur = apply_mask(im, mask)

    # 4 Get Gaussian noise image corruption => Display
    gauss_out_light = get_gaussian_noise(out_motion_blur, 0, 0.0065)
    gauss_out_heavy = get_gaussian_noise(out_motion_blur, 0, 650)
    gauss_out_medium = get_gaussian_noise(out_motion_blur, 0, 65)

    # 5 Get Pseudo-filter mask + Display results
    pseudo_mask_light = get_pseudo_inverse_mask(gauss_out_light, 0.1, a, b, T)
    pseudo_mask_medium = get_pseudo_inverse_mask(gauss_out_medium, 0.1, a, b, T)
    pseudo_mask_heavy = get_pseudo_inverse_mask(gauss_out_heavy, 0.1, a, b, T)
    # pseudo_mask_light = get_pseudo_inverse_mask(im, 0.1, a, b, T)
    # pseudo_mask_medium = get_pseudo_inverse_mask(im, 0.1, a, b, T)
    # pseudo_mask_heavy = get_pseudo_inverse_mask(im, 0.1, a, b, T)

    out_pseudo_filter_light = apply_mask(gauss_out_light, pseudo_mask_light)
    out_pseudo_filter_heavy = apply_mask(gauss_out_heavy, pseudo_mask_heavy)
    out_pseudo_filter_medium = apply_mask(gauss_out_medium, pseudo_mask_medium)

    ######################################################################
    # 6 Get Wiener-filter mask + Display results
    wiener_mask_light = get_wiener_mask(gauss_out_light, a, b, T, 0.0065, im)
    wiener_mask_heavy = get_wiener_mask(gauss_out_heavy, a, b, T, 650, im)
    wiener_mask_medium = get_wiener_mask(gauss_out_medium, a, b, T, 65, im)
    # wiener_mask_light = get_wiener_mask(im, a, b, T, 0.0065, im)
    # wiener_mask_heavy = get_wiener_mask(im, a, b, T, 650, im)
    # wiener_mask_medium = get_wiener_mask(im, a, b, T, 65, im)

    out_wiener_filter_light = apply_mask(gauss_out_light, wiener_mask_light)
    out_wiener_filter_heavy = apply_mask(gauss_out_heavy, wiener_mask_heavy)
    out_wiener_filter_medium = apply_mask(gauss_out_medium, wiener_mask_medium)

    my_dpi = 150
    fig = plt.figure(figsize=(10, 10), dpi=my_dpi)
    # ============ AX1 ============ GAUSS
    ax1 = fig.add_subplot(3, 3, 1)
    ax1.axis("off")
    ax1.set_title("Gaussian Noise Light", size=7)
    ax1.imshow(gauss_out_light, cmap="gray")

    # ============ AX2 ============ GAUSS
    ax2 = fig.add_subplot(3, 3, 4)
    ax2.axis("off")
    ax2.set_title("Gaussian Noise Medium", size=7)
    ax2.imshow(gauss_out_medium, cmap="gray")

    # ============ AX3 ============ GAUSS
    ax3 = fig.add_subplot(3, 3, 7)
    ax3.axis("off")
    ax3.set_title("Gaussian Noise Heavy", size=7)
    ax3.imshow(gauss_out_heavy, cmap="gray")

    # ============ AX4 ============ PSEUDO
    ax4 = fig.add_subplot(3, 3, 2)
    ax4.axis("off")
    ax4.set_title("Pseudo-filter Light", size=7)
    ax4.imshow(out_pseudo_filter_light, cmap="gray")

    # ============ AX5 ============ PSEUDO
    ax5 = fig.add_subplot(3, 3, 5)
    ax5.axis("off")
    ax5.set_title("Pseudo-filter Medium", size=7)
    ax5.imshow(out_pseudo_filter_medium, cmap="gray")

    # ============ AX6 ============ PSEUDO
    ax6 = fig.add_subplot(3, 3, 8)
    ax6.axis("off")
    ax6.set_title("Pseudo-filter Heavy", size=7)
    ax6.imshow(out_pseudo_filter_heavy, cmap="gray")

    # ============ AX7 ============ WIENER
    ax7 = fig.add_subplot(3, 3, 3)
    ax7.axis("off")
    ax7.set_title("Wiener-filter Light", size=7)
    ax7.imshow(out_wiener_filter_light, cmap="gray")

    # ============ AX8 ============ WIENER
    ax8 = fig.add_subplot(3, 3, 6)
    ax8.axis("off")
    ax8.set_title("Wiener-filter Medium", size=7)
    ax8.imshow(out_wiener_filter_medium, cmap="gray")

    # ============ AX9 ============ WIENER
    ax9 = fig.add_subplot(3, 3, 9)
    ax9.axis("off")
    ax9.set_title("Wiener-filter Heavy", size=7)
    ax9.imshow(out_wiener_filter_heavy, cmap="gray")

    plt.show()


if __name__ == "__main__":
    main()
