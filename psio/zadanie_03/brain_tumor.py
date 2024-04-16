import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import skimage.morphology
from skimage import io
from skimage.filters import try_all_threshold
from skimage.transform import resize, rescale
from skimage.color import rgb2gray

img = io.imread('brain_tumor.bmp')
# print(img.shape)

fig, ax = plt.subplots(2,2,figsize=(5, 5))
thr = 170
img_seg = img > thr
img3 = skimage.morphology.remove_small_objects(img_seg, 600, connectivity=2)
cont = skimage.measure.find_contours(img3)
print(cont[0])
ax[0][0].imshow(img,cmap='gray')
ax[0][1].imshow(img_seg,cmap='gray')
ax[1][1].imshow(img3,cmap='gray')
plt.axis('off')
plt.show()
