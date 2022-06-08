from email import message
import cv2

"""
k   e   v   i   k   h   i   e   t   u   o
11  5   22  9   11  8   9   5   20  21  15
"""

def encode(img, msg):
    #imgY = height, imgX = width, imgChannel = channel
    imgY, imgX, imgChannel = img.shape
    for i in range(0, len(msg)):
        img[15][i][0] = 0
    

    return img