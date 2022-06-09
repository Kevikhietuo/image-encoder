import cv2


def encode(img, msg):
    encoded_image = img
    #imgY = height, imgX = width, imgChannel = channel
    imgY, imgX, imgChannel = img.shape
    alphabet = "abcdefghijklmnopqrstuvwxyz _-"
    alphabet_dict = {}

    '''
    coordinates list contains:
    Y = y-coordinates
    X = x-coordinates
    C = channels
    '''
    coordinates = []
    buffer_list = []

    for i, word in enumerate(alphabet):
        alphabet_dict[word] = i

    for i in msg:
        buffer_list.append([hash(i) % imgY, hash(chr(ord(i) + 1)) % imgX, hash(i) % 3])
        coordinates.append(buffer_list)
        buffer_list = []
        encoded_image[hash(i) % imgY][hash(chr(ord(i) + 1)) % imgX][hash(i) % 3] = alphabet_dict[i]
    
    return encoded_image, coordinates