"""
Author: Minh T. Nguyen
2/3/2021

Image shear function with the shearing factor
"""
import cv2 as cv
import numpy as np

# background is black
def imageShear4e(f, sv, sh):
    h, w = f.shape[:2]
    transMat = np.array([[1, sv, 0], [sh, 1, 0]])
    out_img = np.zeros(f.shape, dtype="uint8")
    for m in range(h):
        for n in range(w):
            origin_pos_x = n
            origin_pos_y = m
            origin_pos_xy = np.array([origin_pos_x, origin_pos_y, 1])

            new_pos_xy = np.dot(transMat, origin_pos_xy)
            new_pos_x = int(new_pos_xy[0])
            new_pos_y = int(new_pos_xy[1])

            if 0 < new_pos_x < w and 0 < new_pos_y < h:
                out_img[new_pos_y, new_pos_x] = f[m, n]
    return out_img


def main():
    # Read in the image of the girl
    img = cv.imread("girl.tif")

    # Just show out the original
    cv.imshow("Original", img)

    # Create a shear image with black background
    out_img_sheared1 = imageShear4e(img, 0.5, 0)
    cv.imshow("Shear Image (sv, sh) = (0.5, 0)", out_img_sheared1)

    # Create a shear image with black background
    out_img_sheared2 = imageShear4e(img, 0, -0.75)
    cv.imshow("Shear Image (sv, sh) = (0, -0.75)", out_img_sheared2)

    # Create a shear image with black background
    out_img_sheared3 = imageShear4e(img, 0.5, -0.75)
    cv.imshow("Shear Image (sv, sh) = (0.5, -0.75)", out_img_sheared3)

    cv.waitKey(0)


if __name__ == "__main__":
    main()
