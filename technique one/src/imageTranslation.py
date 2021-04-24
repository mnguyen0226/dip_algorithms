"""
Author: Minh T. Nguyen
2/3/2021
ECE 4580: Digital Image Processing

TODO 1: Write image translation function taking in grayscale image and shift by dimension
"""
import cv2 as cv
import numpy as np

def imageTranslate4e(f, tx, ty, mode = "black"):
    # get the height and width of the image
    h,w = f.shape[:2]
    transMat = np.array([[1,0,tx],[0,1,ty]])

    if(mode == "black"):
        # The output shape is equal to the input shape
        out_img = np.zeros(f.shape, dtype='uint8')
        for m in range(h):
            for n in range(w):
                origin_pos_x = n
                origin_pos_y = m
                origin_pos_xy = np.array([origin_pos_x, origin_pos_y, 1])

                new_pos_xy = np.dot(transMat, origin_pos_xy)
                new_pos_x = new_pos_xy[0]
                new_pos_y = new_pos_xy[1]
        
                if 0 < new_pos_x < w and 0 < new_pos_y < h:
                    out_img[new_pos_y, new_pos_x] = f[m,n]
        return out_img

    elif(mode == "white"):
        # The output shape is equal to the input shape
        out_img = 255*np.ones(f.shape, dtype='uint8')
        for m in range(h):
            for n in range(w):
                origin_pos_x = n
                origin_pos_y = m
                origin_pos_xy = np.array([origin_pos_x, origin_pos_y, 1])

                new_pos_xy = np.dot(transMat, origin_pos_xy)
                new_pos_x = new_pos_xy[0]
                new_pos_y = new_pos_xy[1]
        
                if 0 < new_pos_x < w and 0 < new_pos_y < h:
                    out_img[new_pos_y, new_pos_x] = f[m,n]
        return out_img

    else:
        print("please choose the right mode black or white")

def main():
    print("Running")
    
    # Read in the image of the girl
    img = cv.imread("girl.tif")
    
    # Just show out the original
    cv.imshow("Original", img)

    # test the function by translate the height in the positive vertical direction half its size and 1/4 of the width
    h, w = img.shape[:2]
    move_x = w
    move_x = int(move_x / 4)
    move_y = h
    move_y = int(move_y / 2)

    # Create a translated image with black background
    out_img_black = imageTranslate4e(img, move_x, move_y)
    cv.imshow("Black Background", out_img_black)

    # Create a translated image with white background
    out_img_white = imageTranslate4e(img, move_x, move_y, "white")
    cv.imshow("White Background", out_img_white)

    cv.waitKey(0)

if __name__ == "__main__":
    main()
