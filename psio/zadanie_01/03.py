import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage import io
from skimage.transform import resize, rescale
from skimage.color import rgb2gray
import cv2

img = cv2.imread('C:\\Users\\damia\\Pictures\\dane obrazowe-20240303\\input1\\lena.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.title("pic1")
plt.show()
