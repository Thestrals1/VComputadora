import cv2
import numpy as np
from matplotlib import pyplot as plt
 
img = cv2.imread("a.jpg")
blur = cv2.GaussianBlur(img,(5,5),0)
plt.subplot(121),plt.imshow(img),plt.title("Orignal")
plt.subplot(122),plt.imshow(blur),plt.title("Blurred")
plt.show()