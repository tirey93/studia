import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy
import numpy as np
import skimage
from skimage import io
from skimage.transform import resize, rescale
from skimage.color import rgb2gray

img = skimage.data.moon()
# print(img)
hist, edges = np.histogram(img, 256)
fig, ax = plt.subplots(2, 2, figsize=(10, 5), constrained_layout=True)
ax[0][0].imshow(img, cmap="gray")
ax[0][1].plot(hist)

x=np.arange(256)
a=80;b=150
lut=np.zeros((256,), dtype=np.uint8)
lut2=np.zeros((256,), dtype=np.uint8)
lut2[a:b] = x[a:b]-a
# print(lut2)
lut[a:b]=255*(x[a:b]-a)//(b-a)
print(lut)
print(np.shape(lut))
lut[:a]=0; lut[b:]=255
# print(lut)
img2=lut[img]
# print(img2)
his2,edges = np.histogram(img2, 256)

ax[1][0].imshow(img2, cmap="gray")
ax[1][1].bar(x,his2)

plt.show()
