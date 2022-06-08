import cv2


def decode(img, length):
    alphabet = "abcdefghijklmnopqrstuvwxyz _-"
    imgY, imgX, imgChannel = img.shape
    alphabet_dict = {}
    message = ''

    for i, word in enumerate(alphabet):
        alphabet_dict[i] = word
    
    ctr = 0;
    for i in range (length):
        quantized = img[imgY-1][ctr][0]
        message += alphabet_dict[quantized]
        ctr += 1
    
    return message