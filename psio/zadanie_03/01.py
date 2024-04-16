import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from skimage import io
from skimage.transform import resize, rescale
from skimage.color import rgb2gray
from skimage.filters import try_all_threshold, threshold_otsu, threshold_yen
from skimage.morphology import disk, ball
from skimage.filters.rank import maximum

nrows = 2
ncols = 2
img = io.imread('gears1.png')
img = np.array(rgb2gray(img) * 255, dtype=int)

# fig, ax = try_all_threshold(img, figsize=(10, 8), verbose=False)
thr_otsu = threshold_otsu(img)
thr_yen = threshold_yen(img)

fig, ax = plt.subplots(nrows, ncols, figsize=(5, 5), constrained_layout=True)
img_seg_otsu = (img > thr_otsu) * 1
hist_otsu, edges = np.histogram(img, 256)
print(np.shape(hist_otsu))
img_seg_yen = (img > thr_yen) * 1
hist_yen, edges = np.histogram(img, 256)

ax[0][0].imshow(img_seg_otsu,cmap='gray')
ax[0][1].plot([thr_otsu, thr_otsu], [0, max(hist_otsu)], 'red', lw=2)
ax[0][1].plot(hist_otsu)

ax[1][0].imshow(img_seg_yen,cmap='gray')
ax[1][1].plot([thr_yen, thr_yen], [0, max(hist_yen)], 'red', lw=2)
ax[1][1].plot(hist_otsu)


plt.show()
