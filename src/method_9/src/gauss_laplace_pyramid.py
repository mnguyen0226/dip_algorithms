"""
Author: Minh T. Nguyen
"""

import numpy as np
import scipy as sp
import scipy.signal
import cv2 as cv
import matplotlib.pyplot as plt
from skimage.color import rgb2gray


def kernel_generate(param):
    """ Function take in param value return a 5x5 generating kernel based on the input param 
    @paam:
    param: range of value [0, 1], based on my research, it is recommended to be 40%
    
    @return:
    A 5x5 kernel, dtype = np.ndarray
    """
    kernel = np.array([0.25 - param / 2.0, 0.25, param, 0.25, 0.25 - param / 2.0])
    return np.outer(kernel, kernel)


def reduce_im(im):
    """ Function convolve the input im with a generating kernel of param 0.4
        and reduce_im its width and height by 2
    @param: 
    im: grayscale image of shape (row, col)

    @return:
    convolved_im: an image of shape (ceil(row/2), ceil(col/2)), dtype = np.ndarray
    """
    kernel = kernel_generate(0.4)
    convolved_im = scipy.signal.convolve2d(im, kernel, "same")
    return convolved_im[::2, ::2]


def gauss_pyramid(im, levels):
    """ Function construct a pyramid from the im by reducing it by the number of 
        levels passed in by the input
    @param:
    im: grayscale input image
    levels: positive number of levels of gaussian that you want, according to the paper, at level 0 of the pyramid, G0 is equal to the origial im

    @return:
    output_list output list of resized images with gaussian pyramid, dtype = numpy.ndarray
    """
    output_list = [im]
    if levels == 0:
        return output_list
    for i in range(1, levels + 1):
        output_list.append(reduce_im(output_list[i - 1]))
    return output_list


def expand_im(im):
    """ Function expand the image to double the size, then convolve it with a generating kernel withe the param of 0.4
    @param:
    im: a grayscale image of shape (row, col)
    
    @return:
    output_im: an image of shape (2*row, 2*col), dtype = numpy.ndarray
    """
    kernel = kernel_generate(0.4)
    expanded_size = tuple(np.array(im.shape) * 2)
    output_im = np.zeros(expanded_size)
    output_im[::2, ::2] = im
    return scipy.signal.convolve2d(output_im, kernel, "same") * 4


def laplace_pyramid(gauss_pyramid_list):
    """ Function construct a laplacian pyramid from gaussian pyramid, of the height level
    @param: 
    gauss_pyramid_list: A Gaussian pyramid list returned by gauss_pyramid function, dtype: numpy.ndarray 

    @return:
    output_list[k] = gauss_pyramid_list[k] - expand_im(gauss_pyr[k + 1])
    """
    output_list = []
    for k in range(0, len(gauss_pyramid_list)):
        # Append the last element of the pyramid list to the output list
        if k + 1 == len(gauss_pyramid_list):
            output_list.append(gauss_pyramid_list[k])
        else:
            expandedImage = expand_im(gauss_pyramid_list[k + 1])
            # Crop image
            if expandedImage.size > gauss_pyramid_list[k].size:
                expandedImage = expandedImage[
                    : gauss_pyramid_list[k].shape[0], : gauss_pyramid_list[k].shape[1]
                ]
            output_list.append(gauss_pyramid_list[k] - expandedImage)
    return output_list


def blend(first_laplace_pyr_list, second_laplace_pyr_list, mask_gaussian_pyr_list):
    """ Function blend the two laplacian pyramids list of the input image then weight them according to the gaussian mask
    @param:
    1.first_laplace_pyr_list: list of Laplace pyramid of input image 1
    2.second_laplace_pyr_list: list of Laplace pyramid of input image 2
    3.mask_gaussian_pyr_list: list of the Gaussian pyramid of input mask image
    
    LS(i, j) = (1 - GR(i, j))*LA(i, j) + GR(i, j,)*LB(i, j);

    @return:
    blended_pyr: Laplace pyramid list that has the same dimention of the input image
    """
    blended_pyr = []
    for i in range(0, len(mask_gaussian_pyr_list)):
        # LS(i, j) = (1 - GR(i, j))*LA(i, j) + GR(i, j,)*LB(i, j);
        blended_layer = (1 - mask_gaussian_pyr_list[i]) * first_laplace_pyr_list[
            i
        ] + mask_gaussian_pyr_list[i] * second_laplace_pyr_list[i]
        blended_pyr.append(blended_layer)
    return blended_pyr


def collapse(blended_pyramid):
    """ Function collapse the list of blended list of image 
    @param: 
    blended_pyramid: list of the images from blend()

    @return:
    blended_pyramid[0]: the "first" image with the same shape as the based layer of the blended pyramid

    HOW? Start at the smallest layer of the blended blended_pyramid; expand that smallest layer then 
        add it to the second smallest layer. Continue that process till I get to the largest image (index = 0 in blended_pyramid list)
    """
    for i in range(len(blended_pyramid) - 1, 0, -1):
        expanded_layer = expand_im(blended_pyramid[i])
        if expanded_layer.size > blended_pyramid[i - 1].size:
            expanded_layer = expanded_layer[
                : blended_pyramid[i - 1].shape[0], : blended_pyramid[i - 1].shape[1]
            ]
        blended_pyramid[i - 1] += expanded_layer
    return blended_pyramid[0]


def main():
    # 1. Read in the testing image
    im = plt.imread("testpattern1024.tif")
    im = rgb2gray(im)

    # 2. Create a gaussian pyramid list from testing image with 3 level 0-3
    gaus_list = gauss_pyramid(im, 3)

    # 3. Plot the original image
    plt.figure(figsize=(14, 14))
    plt.imshow(im, cmap="gray"), plt.title("Original", size=12)

    # 4. Plot all Gaussian pyramid image in the list
    plt.figure(figsize=(14, 14))
    plt.subplots_adjust(
        left=0.05, top=0.95, right=0.95, bottom=0, wspace=0.05, hspace=0.05
    )
    plt.subplot(221), plt.imshow(gaus_list[0], cmap="gray"), plt.title(
        "Gaussian Pyramid Level 0", size=8
    )
    plt.subplot(222), plt.imshow(gaus_list[1], cmap="gray"), plt.title(
        "Gaussian Pyramid Level 1", size=8
    )
    plt.subplot(223), plt.imshow(gaus_list[2], cmap="gray"), plt.title(
        "Gaussian Pyramid Level 2", size=8
    )
    plt.subplot(224), plt.imshow(gaus_list[3], cmap="gray"), plt.title(
        "Gaussian Pyramid Level 3", size=8
    )

    # 5. Create a laplace pyramid list from testing image with 3 level 0-3
    laplace_list = laplace_pyramid(gaus_list)

    # 6. Plot all Laplace pyramid image in the list
    plt.figure(figsize=(14, 14))
    plt.subplots_adjust(
        left=0.05, top=0.95, right=0.95, bottom=0, wspace=0.05, hspace=0.05
    )
    plt.subplot(221), plt.imshow(laplace_list[0], cmap="gray"), plt.title(
        "Laplace Pyramid Level 0", size=8
    )
    plt.subplot(222), plt.imshow(laplace_list[1], cmap="gray"), plt.title(
        "Laplace Pyramid Level 1", size=8
    )
    plt.subplot(223), plt.imshow(laplace_list[2], cmap="gray"), plt.title(
        "Laplace Pyramid Level 2", size=8
    )
    plt.subplot(224), plt.imshow(laplace_list[3], cmap="gray"), plt.title(
        "Laplace Pyramid Level 3", size=8
    )

    """
    # GRAY SCALE - Do not Grade
    # 1. Read in all apple, orange, mask image and grayscale them
    im_apple = plt.imread("apple.jpg")
    im_apple = rgb2gray(im_apple)

    im_orange = plt.imread("orange.jpg")
    im_orange = rgb2gray(im_orange)

    im_mask = plt.imread("mask.jpg")
    im_mask = rgb2gray(im_mask)

    # 2. Calculate the gaussian and laplace accordingly
    gaus_apple = gauss_pyramid(im_apple, 4)
    laplace_apple = laplace_pyramid(gaus_apple)

    gaus_orange = gauss_pyramid(im_orange, 4)
    laplace_orange = laplace_pyramid(gaus_orange)

    gaus_mask = gauss_pyramid(im_mask, 4)

    # 3. Calculate the blended_pyramid list
    blended_output = blend(laplace_apple, laplace_orange, gaus_mask)

    # 4. Collapse all image in the blended_pyramid list
    collapse_output = collapse(blended_output)

    # 5. Plot the output image
    plt.figure(figsize=(14,14))
    plt.imshow(collapse_output, cmap="gray"), plt.title("Blended Apple, Orange, Mask with Gaussian and Laplace Pyramid", size=8)
    """

    plt.show()


if __name__ == "__main__":
    main()
