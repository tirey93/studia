import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from skimage import io
from skimage.transform import resize, rescale
from skimage.color import rgb2gray
from skimage.filters import try_all_threshold, threshold_mean
from skimage.morphology import disk, ball
from skimage.filters.rank import maximum


img = io.imread('printed_text.png')
img = np.array(rgb2gray(img) * 255, dtype=np.uint8)


fig, ax = plt.subplots(figsize=(5, 5), constrained_layout=True)

tlo = maximum(img, disk(12))
obraz2 = tlo - img
#fig, ax = try_all_threshold(obraz2, figsize=(10, 8), verbose=False)

thr_mean = threshold_mean(obraz2)
img_seg_mean = (obraz2 > thr_mean) * 1

ax.imshow(img_seg_mean,cmap='gray')
plt.show()














