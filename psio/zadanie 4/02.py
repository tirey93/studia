import matplotlib.pyplot as plt
import numpy as np
from skimage import io, filters, feature, segmentation, morphology, measure
from skimage.color import rgb2gray
from skimage.transform import resize


img = io.imread('bolts.jpg')
img = resize(img, (img.shape[0] // 3, img.shape[1] // 3))
img = rgb2gray(img)

img = filters.gaussian(img)
img = filters.gaussian(img)
img = filters.gaussian(img)
img = feature.canny(img)
img = segmentation.clear_border(img, buffer_size=10)
img = morphology.closing(img,footprint=np.ones((18, 18)))

labels = measure.label(img)

fig,ax = plt.subplots(figsize =(5,5), constrained_layout=True)

ax.imshow(labels, cmap="tab20c")
plt.show()
