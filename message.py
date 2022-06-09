# #CUSTOM FILES
# import encoder
# import decoder

# #LIBRARIES
# import cv2

# #GLOBAL VARIABLES
# msg = ''

# def starter():
#     choice = int(input("0) DECODE\n1) ENCODE\n\n -->"))
#     if (choice == 1):
#         #ENTER YOUR MESSAGE BELOW
#         msg = 'this is a trial message'

#         #UPLOAD YOUR IMAGE TO ENCODE MESSAGE
#         img = cv2.imread('starterImage.jpg')

#         encoded_img, coordinates = encoder.encode(img, msg)

#         #saving your encoded image
#         cv2.imwrite('EncodedImage.jpg', encoded_img)
    
#     elif (choice == 0):
#         #ENTER YOUR MESSAGE BELOW
#         msg = 'this is a trial message'

#         #UPLOAD YOUR IMAGE TO ENCODE MESSAGE
#         img = cv2.imread('starterImage.jpg')

#         encoded_img, coordinates = encoder.encode(img, msg)
#         decoded_msg = decoder.decode(encoded_img, len(msg), coordinates)
#         print(decoded_msg)
    
#     return 0

#CUSTOM FILES
import encoder
import decoder

#LIBRARIES
import os
import cv2
import tkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from cv2 import CAP_PROP_XI_TEST_PATTERN_GENERATOR_SELECTOR

root = Tk()
winWidth, winHeight = 1080, 720
root.geometry("1080x720")
root.resizable(width=True, height=True)


#GLOBAL VARIABLES
msg = ''
global img
# img = Image.open("placeholderImage.jpg")

def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    lbl.config(text = "Provided Input: "+inp)

def openfn():
    filename = filedialog.askopenfilename(title='open')
    return filename

def encodeImg():
    x = openfn()
    img = Image.open(x)
    width, height = img.size
    ratio = width / height
    new_height = 600
    new_width = int(ratio * new_height)
    new_img = img
    new_img = new_img.resize((new_width, new_height), Image.ANTIALIAS)
    new_img = ImageTk.PhotoImage(new_img)
    panel1 = Label(root, image=new_img)
    panel1.image = new_img

# Create label
l1 = Label(root, text = "ENTER YOUR MESSAGE")
l1.grid(row = 0, column = 0)
# TextBox Creation
inputtxt = tkinter.Text(root, height = 3, width = 91)
inputtxt.grid(row = 0, column=1)
# inputtxt.pack()
  
uploadBtn = Button(root, text='ENCODE IMAGE', command=encodeImg, width= 20).grid(row=1, column=0, columnspan= 2)

# Button Creation
printButton = tkinter.Button(root, text = "Print", command = printInput, width= 20)
printButton.grid(row=2, column = 0, columnspan= 2)
  
# Label Creation
lbl = tkinter.Label(root, text = "")

root.mainloop()

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
    
    return 0