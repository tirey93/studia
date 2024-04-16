import collections

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy
import numpy as np
import skimage
from skimage import io
from skimage.transform import resize, rescale
from skimage.color import rgb2gray

img = skimage.data.camera()
hist, edges = np.histogram(img, 256)
fig, ax = plt.subplots(2, 3, figsize=(10, 5), constrained_layout=True)
ax[0][0].imshow(img, cmap="gray")
ax[0][1].plot(hist)
# print(hist)

img2 = img//32
his = np.zeros(8, dtype=np.uint64)
# print(np.unique(img2.flatten(), return_counts=True))
val,cnt = np.unique(img2.flatten(), return_counts=True)

his[val]=cnt
ax[1][0].bar(val, his)

ax[1][1].bar(val, numpy.cumsum(his))

img2 = img//32
his = np.zeros(8, dtype=np.uint64)
dct =collections.Counter(img2.flatten())
val=[*dct.keys()]
cnt=[*dct.values()]
his[val]=cnt
ax[0][2].bar(val, his)

plt.show()
