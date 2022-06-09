import encoder
import decoder
import cv2
from matplotlib import pyplot as plt
 

if __name__ == "__main__":
    msg = 'please work'
    img = cv2.imread('288by288.png')
    encoded_img, coordinates = encoder.encode(img, msg)

    cv2.imwrite('trial.png', encoded_img)

    decoded_msg = decoder.decode(encoded_img, len(msg), coordinates)
    
    print(decoded_msg)