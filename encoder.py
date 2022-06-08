import cv2


def encode(img, msg):
    encoded_image = img
    #imgY = height, imgX = width, imgChannel = channel
    imgY, imgX, imgChannel = img.shape
    alphabet = "abcdefghijklmnopqrstuvwxyz _-"
    alphabet_dict = {}

    for i, word in enumerate(alphabet):
        alphabet_dict[word] = i

    ctr = 0;
    for i in msg:
        encoded_image[imgY-1][ctr][0] = alphabet_dict[i]
        ctr += 1

    return encoded_image