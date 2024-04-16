import matplotlib.pyplot as plt
import numpy as np
from skimage import io
from skimage.color import rgb2gray

img = io.imread('bolts.jpg')
img = np.array(rgb2gray(img) * 255, dtype=int)

fig,ax = plt.subplots(figsize =(5,5), constrained_layout=True)

ax.imshow(img, cmap="grey")
plt.show()
