import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage import io
from skimage.transform import resize, rescale
from skimage.color import rgb2gray

img0 = io.imread('C:\\Users\\damia\\Pictures\\dane obrazowe-20240303\\input1\\lena.png')
img = rgb2gray(img0)

fig, ax = plt.subplots(1, 2, figsize=(5, 5), constrained_layout=True)
ax[0].imshow(img, cmap="gray")
ax[1].imshow(img0, cmap="gray")
plt.show()