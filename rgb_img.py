import numpy as np
import cv2

def get_b_img(img):
    b_img = np.copy(img)
    b_img[:,:,(1)] = 0
    b_img[:,:,(2)] = 0
    return b_img

def get_g_img(img):
    g_img = np.copy(img)
    g_img[:,:,(0)] = 0
    g_img[:,:,(2)] = 0
    return g_img

def get_r_img(img):
    r_img = np.copy(img)
    r_img[:,:,(0)] = 0
    r_img[:,:,(1)] = 0
    return r_img

img_path = 'giraffe.jpg'
img = cv2.imread(img_path, 1)
img_b = get_b_img(img)
img_g = get_g_img(img)
img_r = get_r_img(img)

cv2.imwrite(f'b_giraffe.jpg', img_b)
cv2.imwrite(f'g_giraffe.jpg', img_g)
cv2.imwrite(f'r_giraffe.jpg', img_r)