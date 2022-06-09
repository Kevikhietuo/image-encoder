import cv2


def decode(img, length, coordinates):
    alphabet = "abcdefghijklmnopqrstuvwxyz _-"
    imgY, imgX, imgChannel = img.shape
    alphabet_dict = {}
    message = ''

    for i, word in enumerate(alphabet):
        alphabet_dict[i] = word
    
    '''
    for i in range(length):
        quantized = img[hash(i) % imgY][hash(chr(ord(i) + 1)) % imgX][hash(i) % 3]
        message += alphabet_dict[quantized]\
    '''
    
    for i in range(len(coordinates)):
        quantized = img[(coordinates[i][0][0])][(coordinates[i][0][1])][(coordinates[i][0][2])]
        message += alphabet_dict[quantized]

    return message