"""
Name: Minh T. Nguyen
ECE 4580 - Digital Image Processing
4/13/2021
Project Assignment 3 - Edge Detection
"""
import math
import cv2 as cv
import numpy as np
from scipy.ndimage.filters import convolve
from scipy import ndimage
from matplotlib import pyplot as plt

def get_sobel_kernel(im):
    """
    Function takes in smoothed images then do matrix multiplication with Sobel kernel to get the gradient magnitude and angle
    @param:
    im = input blurred image

    @return:
    1. gradient = gradient magnitude of sobel filter
    2. theta = the angle of sobel filter
    """
    kernel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], np.float32)
    kernel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]], np.float32)

    image_x = ndimage.filters.convolve(im, kernel_x)
    image_y = ndimage.filters.convolve(im, kernel_y)
    
    gradient = np.hypot(image_x, image_y) 
    gradient = gradient / gradient.max() * 255
    theta = np.arctan2(image_y, image_x)
    
    return (gradient, theta)

def non_max_supression(grad_im, theta):
    """
    Function goes thru all points on the gradient intensity matrix to finds the pixels with the max value in the edge directions
    @param:
    1. grad_im = gradient magnitude from sobel filter
    2. theta = angle from sobel filter

    @return:
    out_im = Output images
    """
    row, col = grad_im.shape # M, N
    out_im = np.zeros((row, col), dtype=np.int32)
    angle = theta*180. / np.pi
    angle[angle < 0] += 180

    for i in range(1,row-1):
        for j in range(1,col-1):
            q = 255
            r = 255
                
            # for angle 0
            if (0 <= angle[i,j] < 22.5) or (157.5 <= angle[i,j] <= 180):
                q = grad_im[i, j+1]
                r = grad_im[i, j-1]
            # for angle 45
            elif (22.5 <= angle[i,j] < 67.5):
                q = grad_im[i+1, j-1]
                r = grad_im[i-1, j+1]
            # for angle 90
            elif (67.5 <= angle[i,j] < 112.5):
                q = grad_im[i+1, j]
                r = grad_im[i-1, j]
            # for angle 135
            elif (112.5 <= angle[i,j] < 157.5):
                q = grad_im[i-1, j-1]
                r = grad_im[i+1, j+1]

            if (grad_im[i,j] >= q) and (grad_im[i,j] >= r):
                out_im[i,j] = grad_im[i,j]
            else:
                out_im[i,j] = 0
    return out_im

def double_threshold(im, ltr, htr):
    """
    Function double threshold aim to identify strong, weak, and non-relevant pixels
    @param: 
    1. im = imput image
    2. ltr = low threshold ratio
    3. htr = high threshold ratio

    @return:
    1: weak = weak pixel that has intensity value that is not enough to be considered strong ones, but not non-relevant
    2. strong = pixel with very high intensity
    3. res = non-relevant pixel, not high, not low
    """
    high_thres = im.max() * htr
    low_thres = high_thres * ltr
    
    row, col = im.shape
    res = np.zeros((row,col), dtype=np.int32)
    
    weak = np.int32(25)
    strong = np.int32(255)
    
    strong_i, strong_j = np.where(im >= high_thres)
    zeros_i, zeros_j = np.where(im < low_thres)
    
    weak_i, weak_j = np.where((im <= high_thres) & (im >= low_thres))
    
    res[strong_i, strong_j] = strong
    res[weak_i, weak_j] = weak
    
    return (res, weak, strong)

def hysteresis(im, weak, strong=255):
    """
    Function consist of transforming weak pixel into strong ones if at least 1 pixel around the one being processed is a strong one 
    """
    row, col = im.shape  
    
    for i in range(1, row-1):
        for j in range(1, col-1):
            if (im[i,j] == weak):
                if ((im[i+1, j-1] == strong) or (im[i+1, j] == strong) or (im[i+1, j+1] == strong)
                    or (im[i, j-1] == strong) or (im[i, j+1] == strong)
                    or (im[i-1, j-1] == strong) or (im[i-1, j] == strong) or (im[i-1, j+1] == strong)):
                    im[i, j] = strong
                else:     
                   im[i, j] = 0
    return im

def main():
    print("Running")
    # im = cv.imread("house.jpg", 0)
    im = cv.imread("house.jpg", 0)
    cv.imshow("Original House", im)
    im = im/255.0
    
    # (1) Blue image with Gaussian filter with sigma = 2,8,16
    im_filtered1 = cv.GaussianBlur(im, (0,0), 2)
    im_filtered2 = cv.GaussianBlur(im, (0,0), 8)
    im_filtered3 = cv.GaussianBlur(im, (0,0), 16)

    rows = 1
    cols = 3
    fig1 = plt.figure(figsize=(15, 5))
    
    fig1.add_subplot(rows, cols, 1)
    plt.imshow(np.float64(im_filtered1), cmap="gray") # Less Thick
    plt.title("Gaussian Filtered - sigma=2")
    plt.axis("off")

    fig1.add_subplot(rows, cols, 2)
    plt.imshow(np.float64(im_filtered2), cmap="gray") # Less Thick
    plt.title("Gaussian Filtered - sigma=8")
    plt.axis("off")

    fig1.add_subplot(rows, cols, 3)
    plt.imshow(np.float64(im_filtered3), cmap="gray") # Less Thick
    plt.title("Gaussian Filtered - sigma=16")
    plt.axis("off")

    # (2) Apply Canny edge detectors with the scales you choose to detect edges
    # a/ Show the magnitude and angle of gradiente images ? Correct??
    grad_mag1, angle1 = get_sobel_kernel(im_filtered1)
    grad_mag2, angle2 = get_sobel_kernel(im_filtered2)
    grad_mag3, angle3 = get_sobel_kernel(im_filtered3)

    fig2 = plt.figure(figsize=(15, 5))
    
    fig2.add_subplot(2, cols, 1)
    plt.imshow(np.float64(grad_mag1), cmap="gray") # Less Thick
    plt.title("Gradient Magnitude - sigma=2")
    plt.axis("off")

    fig2.add_subplot(2, cols, 2)
    plt.imshow(np.float64(grad_mag2), cmap="gray") # Less Thick
    plt.title("Gradient Magnitude - sigma=8")
    plt.axis("off")

    fig2.add_subplot(2, cols, 3)
    plt.imshow(np.float64(grad_mag3), cmap="gray") # Less Thick
    plt.title("Gradient Magnitude - sigma=16")
    plt.axis("off")

    fig2.add_subplot(2, cols, 4)
    plt.imshow(np.float64(angle1), cmap="gray") # Less Thick
    plt.title("Angle - sigma=2")
    plt.axis("off")

    fig2.add_subplot(2, cols, 5)
    plt.imshow(np.float64(angle2), cmap="gray") # Less Thick
    plt.title("Angle - sigma=8")
    plt.axis("off")

    fig2.add_subplot(2, cols, 6)
    plt.imshow(np.float64(angle3), cmap="gray") # Less Thick
    plt.title("Angle - sigma=16")
    plt.axis("off")

    # b/ Display the edges before and after non-maximum suppression ?? Aint edge is the magnitude sobel above?
    im_nms1 = non_max_supression(grad_mag1, angle1)
    im_nms2 = non_max_supression(grad_mag2, angle2)
    im_nms3 = non_max_supression(grad_mag3, angle3)

    fig3 = plt.figure(figsize=(15, 5))
    
    fig3.add_subplot(rows, cols, 1)
    plt.imshow(np.float64(im_nms1), cmap="gray") # Less Thick
    plt.title("Non Maximum Suppression - sigma=2")
    plt.axis("off")

    fig3.add_subplot(rows, cols, 2)
    plt.imshow(np.float64(im_nms2), cmap="gray") # Less Thick
    plt.title("Non Maximum Suppression - sigma=8")
    plt.axis("off")

    fig3.add_subplot(rows, cols, 3)
    plt.imshow(np.float64(im_nms3), cmap="gray") # Less Thick
    plt.title("Non Maximum Suppression - sigma=16")
    plt.axis("off")

    # c/ Display the final edge maps after edge linking/double-thresholding technique
    im_thres1, weak1, strong1 = double_threshold(im_nms1, ltr=0.07, htr=0.19)
    print(f"TESTING: WEAK {weak1}")
    im_final1 = hysteresis(im_thres1, weak1, strong1)

    im_thres2, weak2, strong2 = double_threshold(im_nms2, ltr=0.07, htr=0.19) #0.07 0.19
    print(f"TESTING: WEAK {weak2}")
    im_final2 = hysteresis(im_thres2, weak2, strong2)

    im_thres3, weak3, strong3 = double_threshold(im_nms3, ltr=0.02, htr=0.15)
    print(f"TESTING: WEAK {weak3}")
    im_final3 = hysteresis(im_thres3, weak3, strong3)

    fig4 = plt.figure(figsize=(15, 5))
    
    fig4.add_subplot(rows, cols, 1)
    plt.imshow(np.float64(im_final1), cmap="gray") # Less Thick
    plt.title("Final Edge Map - sigma=2")
    plt.axis("off")

    fig4.add_subplot(rows, cols, 2)
    plt.imshow(np.float64(im_final2), cmap="gray") # Less Thick
    plt.title("Final Edge Map - sigma=8")
    plt.axis("off")

    fig4.add_subplot(rows, cols, 3)
    plt.imshow(np.float64(im_final3), cmap="gray") # Less Thick
    plt.title("Final Edge Map - sigma=16")
    plt.axis("off")

    # (3): Combine the multiscale edge maps to generate the final edge map? => Combine all edge of the 3 finals one? // average image => Not good. 
    fig5 = plt.figure(figsize=(15, 5))
    blend_image = im_final1 + im_final2 + im_final3
    plt.imshow(np.float64(blend_image), cmap="gray") # Less Thick
    plt.title("Blended Final Image Sum")
    plt.axis("off")

    # fig6 = plt.figure(figsize=(15, 5))
    # blend_image2 = (im_final1 + im_final2 + im_final3)/3
    # plt.imshow(np.float64(blend_image2), cmap="gray") # Less Thick
    # plt.title("Blended Final Image Average")
    # plt.axis("off")

    plt.show()
    cv.waitKey(0)
    cv.destroyAllWindows() 

if __name__ == "__main__":
    main()