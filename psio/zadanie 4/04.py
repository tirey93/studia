import matplotlib.pyplot as plt
import numpy as np
from skimage import io
from skimage.transform import resize
from skimage.color import rgb2gray
from skimage.measure import euler_number, label, regionprops
from skimage.filters import threshold_otsu
from skimage.morphology import closing, square

img_4d = io.imread('planes.png')
img = img_4d[:,:, 0] // 255


labels = label(img)
euler = euler_number(labels)

img2 = 1 - img
labels = label(img2)
properties = regionprops(labels)

fig, ax = plt.subplots(figsize=(10, 6))
ax.imshow(img, cmap='gray')

for prop in properties:
    y0, x0 = prop.bbox[0], prop.bbox[1]
    height, width = prop.bbox[2] - y0, prop.bbox[3] - x0
    print(f"y: {y0}, x:{x0}, area: {prop.area}, euler: {prop.euler_number}")
    if prop.euler_number == 1:
        rect = plt.Rectangle((x0, y0), width, height, fill=False, edgecolor='red', linewidth=2)
        ax.add_patch(rect)

ax.set_axis_off()
plt.show()
