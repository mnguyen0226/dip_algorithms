"""
Name: Minh T. Nguyen
ECE 4580
Homework 6

TODO: noise the image 
TODO: use AMF to filter
TODO: filter with regular filter
"""

import math
import cv2 as cv
import numpy as np
from skimage.util import random_noise
import pandas as pd
from PIL import Image, ImageFilter

def rgb2gray(im):
    """ Function gray out input image and make sure to output the gray scale one
    @param: im - input rgb or gray scale images
    @return: im - the output gray scale image
    """
    if(len(im.shape) == 3):
        return np.uint8(np.dot(im[...,:3], [0.2989, 0.5870, 0.1140]))
    else:
        return im

def calculate_median(array):
    """ Function return the median of 1d array 
    @oaram: array:; the input 1 d array
    @return: median: the median of that array 
    """
    sorted_array = np.sort(array)
    median = sorted_array[len(array)//2]
    return median

def level_A(z_min, z_med, z_max, z_xy, S_xy, S_max):
    """ Function calculate the median for the kernel for level A 
    @param:
        z_min: the minimum gray level in S_xy
        z_med: the median gray level in S_xy
        z_max: the max gray level in S_xy
        z_xy: the gray level at coordinates (x,y)
        S_xy: the support of the filter centered at (x,y)
        S_max: the max allowed size of S_xy
    @return:
        z_med: the median gray level in S_xy 
    """
    if(z_min < z_med < z_max):
        return level_B(z_min, z_med, z_max, z_xy, S_xy, S_max)
    else:
        S_xy += 2 
        if(S_xy <= S_max):
            return level_A(z_min, z_med, z_max, z_xy, S_xy, S_max)
        else:
            return z_med

def level_B(z_min, z_med, z_max, z_xy, S_xy, S_max):
    """ Function calculate the median for the kernel for level B
        @param:
        z_min: the minimum gray level in S_xy
        z_med: the median gray level in S_xy
        z_max: the max gray level in S_xy
        z_xy: the gray level at coordinates (x,y)
        S_xy: the support of the filter centered at (x,y)
        S_max: the max allowed size of S_xy
    @return:
        z_med: the median gray level in S_xy 
    """
    if(z_min < z_xy < z_max):
        return z_xy
    else:
        return z_med

def amf(im, initial_window, max_window):
    """Function runs the Adaptive Median Filter process to output a singular intensity value that'll 
        replace the existing intensity value at a certain point x,y
    @param:
        im: the input image
        initial_window:
        max_window   
    @return:
        out_im: The output image
    """
    xlen, ylen = im.shape 
    
    z_min, z_med, z_max, z_xy = 0, 0, 0, 0
    S_max = max_window
    S_xy = initial_window 
    
    out_im = im.copy()
    
    for row in range(S_xy, xlen-S_xy-1):
        for col in range(S_xy, ylen-S_xy-1):
            filter_window = im[row - S_xy : row + S_xy + 1, col - S_xy : col + S_xy + 1] 
            target = filter_window.reshape(-1) 
            z_min = np.min(target)
            z_max = np.max(target)
            z_med = calculate_median(target) 
            z_xy = im[row, col]
            
            new_intensity = level_A(z_min, z_med, z_max, z_xy, S_xy, S_max)
            out_im[row, col] = new_intensity
    return out_im

##########################################################################
def main():
    print("Running")
    # original image
    im = Image.open("orchid.tif")
    im.show()

    # Gray out image
    im = np.array(im)
    im = rgb2gray(im)

    # noise the image with Gaussian and save it to file 
    gauss = np.random.normal(0,1,im.size)
    gauss = gauss.reshape(im.shape[0],im.shape[1]).astype('uint8')
    im_corrupt = cv.add(im, gauss)
    result = Image.fromarray(im_corrupt)
    cv.imshow("Noise-corrupted image", im_corrupt)

    # Apply AMF to the noise corrupted image
    amf_im = amf(im_corrupt, 3, 11)
    cv.imshow("AMF Filtering", amf_im)

    # # Apply built-in Python Filter    
    noise_im = Image.open("noise_im.tif")
    med_filter_im = noise_im.filter(ImageFilter.MedianFilter(size=3))
    med_filter_im.show() # show filtered image

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()