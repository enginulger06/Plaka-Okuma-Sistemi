import cv2
import numpy as np
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
#s=pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
'''image=Image.open("img/im.png") # the second one
img_gray = cv2.cvtColor(np.asarray(image), cv2.COLOR_BGR2GRAY) #there is a problem here

th, bw = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
edges = cv2.Canny(img_gray, th/2, th)


cv2.imwrite("img/cropped.jpg", edges)'''
'''
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')
im.save('resimler/temp2.jpg')
'''

#text = pytesseract.image_to_string(gray_image)
#print("asd",text)

#Linux window/threading setup code.
cv2.startWindowThread()
cv2.namedWindow("Original")
cv2.namedWindow("Sharpen")

#Load source / input image as grayscale, also works on color images...
imgIn = cv2.imread("img/im.png", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Original", imgIn)


#Create the identity filter, but with the 1 shifted to the right!
kernel = np.zeros( (9,9), np.float32)
kernel[4,4] = 2.0   #Identity, times two!

#Create a box filter:
boxFilter = np.ones( (9,9), np.float32) / 81.0

#Subtract the two:
kernel = kernel - boxFilter


#Note that we are subject to overflow and underflow here...but I believe that
# filter2D clips top and bottom ranges on the output, plus you'd need a
# very bright or very dark pixel surrounded by the opposite type.

custom = cv2.filter2D(imgIn, -1, kernel)
cv2.imshow("Sharpen", custom)
cv2.imwrite("img/cropped.png", custom)

cv2.waitKey(0)