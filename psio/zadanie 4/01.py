import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import skimage.measure
from skimage import io
from skimage.transform import resize, rescale
from skimage.color import rgb2gray
from skimage.filters import try_all_threshold, threshold_minimum, threshold_yen
from skimage.morphology import disk, ball
from skimage.filters.rank import maximum

img = io.imread('brain_tumor.png')
img = np.array(rgb2gray(img) * 255, dtype=int)


fig, ax = plt.subplots(figsize=(5, 5), constrained_layout=True)

thr_min = threshold_minimum(img)
img_seg = img > thr_min
labels, num = skimage.measure.label(img_seg, return_num=True)
print(num)

props = skimage.measure.regionprops(labels)
areas = [x.area for x in props]
max_index = np.argmax(areas)
seg_brain = (labels == props[max_index].label)
#select tumor
thr_yen = threshold_yen(img) + 10
img_tum = img > thr_yen
labels_tum, num = skimage.measure.label(img_tum, return_num=True)
print(num)

props_tum = skimage.measure.regionprops(labels_tum)
areas_tum = [x.area for x in props_tum]
max_index_tum = np.argmax(areas_tum)
seg_brain_tum = (labels_tum == props_tum[max_index_tum].label)

seg = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.float32)
seg[:,:,0] = seg_brain
seg[:,:,2] = seg_brain_tum

ax.imshow(seg, cmap='tab20c')

plt.show()
