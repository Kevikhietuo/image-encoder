import encoder
import decoder
import cv2
from matplotlib import pyplot as plt
 

if __name__ == "__main__":
    msg = 'let us see if this is working'
    img = cv2.imread('288by288.png')
    encoded_img = encoder.encode(img, msg)

    # cv2.imwrite('trial.png', encoded_img)

    decoded_msg = decoder.decode(encoded_img, len(msg))
    
    print(decoded_msg)