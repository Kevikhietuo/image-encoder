#CUSTOM FILES
import encoder
import decoder

#LIBRARIES
import cv2

def starter():
    #ENTER YOUR MESSAGE BELOW
    msg = 'you better work or else'

    #UPLOAD YOUR IMAGE TO ENCODE MESSAGE
    img = cv2.imread('288by288.png')

    encoded_img, coordinates = encoder.encode(img, msg)

    #saving your encoded image
    cv2.imwrite('trial.png', encoded_img)

    decoded_msg = decoder.decode(encoded_img, len(msg), coordinates)
    
    print(decoded_msg)

    return 0