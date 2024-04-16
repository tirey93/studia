import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from skimage import io
from skimage.transform import resize, rescale
from skimage.color import rgb2gray
from skimage.filters import try_all_threshold, threshold_mean, threshold_minimum
from skimage.morphology import disk, ball
from skimage.filters.rank import maximum

img = io.imread('blood_smear.jpg')
img = np.array(rgb2gray(img) * 255, dtype=int)


fig, ax = plt.subplots(figsize=(5, 5), constrained_layout=True)

thr_mean = threshold_mean(img)
thr_min = threshold_minimum(img)
img_seg_mean = (img <= thr_mean) * 1
img_seg_min = (img <= thr_min) * 1


img2 = np.ones((np.shape(img)[0], np.shape(img)[1], 3))
img2[img_seg_mean == 1] = [1, 0, 0]
img2[img_seg_min == 1] = [0, 0, 1]

ax.imshow(img2)
plt.show()


