import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage import io
from skimage.transform import resize, rescale
from skimage.color import rgb2gray

img = io.imread('C:\\Users\\damia\\Pictures\\dane obrazowe-20240303\\input1\\lena.png')
print(img.shape)

fig, ax = plt.subplots(figsize=(5, 5))
ax.imshow(img,cmap='gray')
plt.axis('off')
plt.show()
