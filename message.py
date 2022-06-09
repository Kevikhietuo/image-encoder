#CUSTOM FILES
import encoder
import decoder

#LIBRARIES
import cv2

#GLOBAL VARIABLES
msg = ''

def starter():
    choice = int(input("0) DECODE\n1) ENCODE\n\n -->"))
    if (choice == 1):
        #ENTER YOUR MESSAGE BELOW
        msg = 'this is a trial message'

        #UPLOAD YOUR IMAGE TO ENCODE MESSAGE
        img = cv2.imread('starterImage.jpg')

        encoded_img, coordinates = encoder.encode(img, msg)

        #saving your encoded image
        cv2.imwrite('EncodedImage.jpg', encoded_img)
    
    elif (choice == 0):
        #ENTER YOUR MESSAGE BELOW
        msg = 'this is a trial message'

        #UPLOAD YOUR IMAGE TO ENCODE MESSAGE
        img = cv2.imread('starterImage.jpg')

        encoded_img, coordinates = encoder.encode(img, msg)
        decoded_msg = decoder.decode(encoded_img, len(msg), coordinates)
        print(decoded_msg)
    
    return 0``