import cv2


def decode(img, length):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_dict = {}
    message = ''

    for i, word in enumerate(alphabet):
        alphabet_dict[i] = word
    
    ctr = 0;
    for i in range (length):
        quantized = img[15][ctr][0]
        message += alphabet_dict[quantized]
        ctr += 1
    
    return message