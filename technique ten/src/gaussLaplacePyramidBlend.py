"""
Name: Minh T. Nguyen
ECE 4580 - DIP Midterm
3/19/2021 

COLOR Blend
"""
import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage, misc, signal
from PIL import Image
import skimage
from skimage.transform import resize
import imageio

def split_rgb(im):
    """ Function split the 3 RGB channel of the image
    @param:
    im: the input image

    @return:
    the 3 array storing 3 RGB color
    """
    red = im[:, :, 0]
    green = im[:, :, 1]
    blue = im[:, :, 2]
    return blue, green, red

def combine_rgb(r, g, b):
    """ Function combine all RGB channel
    @param:
    r: red channel
    g: green channel
    b: blue channel

    @return:
    im: the image
    """
    im = np.zeros((r.shape[0], r.shape[1], 3)).astype(np.uint8)
    im[:, :, 0] = r
    im[:, :, 1] = g
    im[:, :, 2] = b
    return im

def reduce_im(im):
    """ Function convolve the input im with a generating kernel of param 0.4
        and reduce_im its width and height by 2
    @param: 
    im: grayscale image of shape (row, col)

    @return:
    out: an image of shape (ceil(row/2), ceil(col/2)), dtype = np.ndarray
    """
    out = im[::2, ::2]
    return out

def gauss_pyramid(im, levels):
    """ Function convolve the input im with a generating kernel of param 0.4
        and reduce_im its width and height by 2
    @param: 
    im: grayscale image of shape (row, col)

    @return:
    output: an image of shape (ceil(row/2), ceil(col/2)), dtype = np.ndarray
    """    
    output = []
    output.append(im)
    tmp = im
    for i in range(0, levels):
        tmp = reduce_im(tmp)
        output.append(tmp)
    return output

def expand_im(im):
    """ Function expand the image to double the size, then convolve it with a generating kernel withe the param of 0.4
    @param:
    im: a grayscale image of shape (row, col)
    
    @return:
    out: an image of shape (2*row, 2*col), dtype = numpy.ndarray
    """     
    w = np.array([0.25 - 0.4 / 2.0, 0.25, 0.4, 0.25, 0.25 - 0.4 / 2.0])
    T = np.outer(w, w)
    outimage = np.zeros((im.shape[0] * 2, im.shape[1] * 2), dtype=np.float64)
    outimage[::2, ::2] = im[:, :]
    out = 4 * signal.convolve2d(outimage, T, 'same')
    return out

def laplace_pyramid(gauss_pyramid_list):
    """ Function construct a laplacian pyramid from gaussian pyramid, of the height level
    @param: 
    gauss_pyramid_list: A Gaussian pyramid list returned by gauss_pyramid function, dtype: numpy.ndarray 

    @return:
    output[k] = gauss_pyramid_list[k] - expand_im(gauss_pyr[k + 1])
    """     
    output = []
    k = len(gauss_pyramid_list)
    for i in range(0, k - 1):
        gauss = gauss_pyramid_list[i]
        expand_gauss = expand_im(gauss_pyramid_list[i + 1])
        if expand_gauss.shape[0] > gauss.shape[0]:
            expand_gauss = np.delete(expand_gauss, (-1), axis=0)
        if expand_gauss.shape[1] > gauss.shape[1]:
            expand_gauss = np.delete(expand_gauss, (-1), axis=1)
        output.append(gauss - expand_gauss)
    output.append(gauss_pyramid_list.pop())
    return output 

def blend(first_laplace_pyr_list, second_laplace_pyr_list, mask_gaussian_pyr_list):
    """ Function blend the two laplacian pyramids list of the input image then weight them according to the gaussian mask
    @param:
    1.first_laplace_pyr_list: list of Laplace pyramid of input image 1
    2.second_laplace_pyr_list: list of Laplace pyramid of input image 2
    3.mask_gaussian_pyr_list: list of the Gaussian pyramid of input mask image
    
    LS(i, j) = (1 - GR(i, j))*LA(i, j) + GR(i, j,)*LB(i, j);

    @return:
    blended_pyramid: Laplace pyramid list that has the same dimention of the input image
    """    
    blended_pyramid = []
    k = len(mask_gaussian_pyr_list)
    for i in range(0, k):
        p1 = mask_gaussian_pyr_list[i] * first_laplace_pyr_list[i]
        p2 = (1 - mask_gaussian_pyr_list[i]) * second_laplace_pyr_list[i]
        blended_pyramid.append(p1 + p2)
    return blended_pyramid

def collapse(blended_pyramid):
    """ Function collapse the list of blended list of image 
    @param: 
    blended_pyramid: list of the images from blend()

    @return:
    output: the "first" image with the same shape as the based layer of the blended pyramid

    HOW? Start at the smallest layer of the blended blended_pyramid; expand that smallest layer then 
        add it to the second smallest layer. Continue that process till I get to the largest image (index = 0 in blended_pyramid list)
    """    
    output = np.zeros(
        (blended_pyramid[0].shape[0], blended_pyramid[0].shape[1]), dtype=np.float64)
    for i in range(len(blended_pyramid) - 1, 0, -1):
        expanded_lap = expand_im(blended_pyramid[i])
        next_lap = blended_pyramid[i - 1]
        if expanded_lap.shape[0] > next_lap.shape[0]:
            expanded_lap = np.delete(expanded_lap, (-1), axis=0)
        if expanded_lap.shape[1] > next_lap.shape[1]:
            expanded_lap = np.delete(expanded_lap, (-1), axis=1)
        tmp = expanded_lap + next_lap
        blended_pyramid.pop()
        blended_pyramid.pop()
        blended_pyramid.append(tmp)
        output = tmp
    return output

def main():
    print("Running")
    image_2 = imageio.imread('orange.jpg')
    image_1 = imageio.imread('apple.jpg')
    mask = imageio.imread('mask.jpg')
    level = 4

    r1, g1, b1 = split_rgb(image_1)
    r2, g2, b2 = split_rgb(image_2)
    rm, gm, bm = split_rgb(mask)
    
    r1 = r1.astype(float)
    g1 = g1.astype(float)
    b1 = b1.astype(float)

    r2 = r2.astype(float)
    g2 = g2.astype(float)
    b2 = b2.astype(float)

    rm = rm.astype(float) / 255
    gm = gm.astype(float) / 255
    bm = bm.astype(float) / 255

    # first reduce image one channels

    mask_gaussian_image1r = gauss_pyramid(r1, level)
    mask_gaussian_image1g = gauss_pyramid(g1, level)
    mask_gaussian_image1b = gauss_pyramid(b1, level)

    mask_gaussian_image2r = gauss_pyramid(r2, level)
    mask_gaussian_image2g = gauss_pyramid(g2, level)
    mask_gaussian_image2b = gauss_pyramid(b2, level)

    mask_gaussian_pyr_listr = gauss_pyramid(rm, level)
    mask_gaussian_pyr_listg = gauss_pyramid(gm, level)
    mask_gaussian_pyr_listb = gauss_pyramid(bm, level)

    laplacian_pyramid_image1r = laplace_pyramid(mask_gaussian_image1r)
    laplacian_pyramid_image1g = laplace_pyramid(mask_gaussian_image1g)
    laplacian_pyramid_image1b = laplace_pyramid(mask_gaussian_image1b)


    laplacian_pyramid_image2r = laplace_pyramid(mask_gaussian_image2r)
    laplacian_pyramid_image2g = laplace_pyramid(mask_gaussian_image2g)
    laplacian_pyramid_image2b = laplace_pyramid(mask_gaussian_image2b)

    blend_red = blend(laplacian_pyramid_image2r,
                      laplacian_pyramid_image1r, mask_gaussian_pyr_listr)
    blend_green = blend(laplacian_pyramid_image2g,
                        laplacian_pyramid_image1g, mask_gaussian_pyr_listg)
    blend_blue = blend(laplacian_pyramid_image2b,
                       laplacian_pyramid_image1b, mask_gaussian_pyr_listb)

    collapse_red = collapse(blend_red).astype(np.uint8)
    collapse_green = collapse(blend_green).astype(np.uint8)
    collapse_blue = collapse(blend_blue).astype(np.uint8)

    # display the blended result
    result = np.zeros(image_1.shape, dtype=image_1.dtype)
    result = combine_rgb(collapse_blue, collapse_green, collapse_red)
    plt.figure("Blended Result Level "+str(level))
    plt.imshow(result)
    plt.show()

if __name__ == "__main__":
    main()