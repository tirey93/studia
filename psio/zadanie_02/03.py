import numpy as np
import skimage
from matplotlib import pyplot as plt

img = skimage.data.coffee()
img_r = img[:,:,0]
img_g = img[:,:,1]
img_b = img[:,:,2]
hist_r, edges = np.histogram(img_r, 256)
hist_g, edges = np.histogram(img_g, 256)
hist_b, edges = np.histogram(img_b, 256)
fig, ax = plt.subplots(1, 2)
ax[0].imshow(img, cmap="gray")
ax[1].plot(hist_r)
ax[1].plot(hist_g)
ax[1].plot(hist_b)
plt.show()