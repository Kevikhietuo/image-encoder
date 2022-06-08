from re import I
import cv2
from matplotlib import pyplot as plt


img = cv2.imread('16by16.png')
encoded_image = img

msg = 'kevikhietuo'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

alphabet_dict = {}

for i, word in enumerate(alphabet):
    alphabet_dict[word] = i


ctr = 0;
for i in msg:
    encoded_image[15][ctr][0] = alphabet_dict[i]
    ctr += 1

cv2.imwrite('trial.png', encoded_image)