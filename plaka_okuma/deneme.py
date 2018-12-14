import cv2
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
'''img = cv2.imread("img/12a.png")


def autocrop(image, threshold=0):
    """Crops any edges below or equal to threshold

    Crops blank image to 1x1.

    Returns cropped image.

    """
    if len(image.shape) == 3:
        flatImage = np.max(image, 2)
    else:
        flatImage = image
    assert len(flatImage.shape) == 2

    rows = np.where(np.max(flatImage, 0) > threshold)[0]
    if rows.size:
        cols = np.where(np.max(flatImage, 1) > threshold)[0]
        image = image[cols[0]: cols[-1] + 1, rows[0]: rows[-1] + 1]
    else:
        image = image[:1, :1]

    return image

a= autocrop(img)
cv2.imwrite("img/Im12.png",a)
'''

import numpy as np
import cv2
import matplotlib.pyplot as plt

im2 = cv2.imread('img/im.png')
im = im2.copy()

gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)
ret3,thresh = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

#we ony want the external contours
contours,hierarchy = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#extract the countours with area > 50
squares = [cnt for cnt in contours if cv2.contourArea(cnt) > 50]

#mask array with the same shape as img (but only 1 channel)
mask = np.zeros((im.shape[0], im.shape[1]))
#draw the contours filled with 255 values.
cv2.drawContours(mask,squares,-1,255,-1)

newImage = np.where(mask==255, thresh, 255)

plt.imshow(newImage)
plt.show()

cv2.imwrite("img/crop.png", newImage)