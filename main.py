import encoder
import cv2
from matplotlib import pyplot as plt
 

if __name__ == "__main__":
    msg = 'kevikhietuo'
    img = cv2.imread('16by16.png')
    encoded_img = encoder.encode(img, msg)

    # cv2.imshow("ENCODED IMAGE", encoded_img)
    
    fig = plt.figure(figsize=(10, 7))
    rows = 1
    columns = 2
    
    # Adds a subplot at the 1st position
    fig.add_subplot(rows, columns, 1)
    
    # showing image
    plt.imshow(img)
    plt.axis('off')
    plt.title("First")
    
    # Adds a subplot at the 2nd position
    fig.add_subplot(rows, columns, 2)
    
    # showing image
    plt.imshow(encoded_img)
    plt.axis('off')
    plt.title("Second")

    plt.show()