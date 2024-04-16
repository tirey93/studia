import matplotlib.pyplot as plt
import numpy as np
from skimage import io
from skimage.transform import hough_circle, hough_circle_peaks
from skimage.feature import canny
from skimage import color
from skimage.draw import circle_perimeter

img = io.imread('coins.png')
edges = canny(img, sigma=3, low_threshold=10, high_threshold=50)

# Detect two radii
hough_radii = np.arange(20, 35, 2)
hough_res = hough_circle(edges, hough_radii)

# Select the most prominent 3 circles
accums, cx, cy, radii = hough_circle_peaks(hough_res, hough_radii,
                                           total_num_peaks=17)

# Draw them
fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(10, 4))
image = color.gray2rgb(img)

centers = []
for center_y, center_x, radius in zip(cy, cx, radii):
    circy, circx = circle_perimeter(center_y, center_x, radius,
                                    shape=image.shape)
    
    print(f"y: {center_y}, x:{center_x}, r: {radius}")
    if center_y not in [y[0] for y in centers] and center_x not in [x[1] for x in centers]:
        print("not in")
        centers.append((center_y, center_x))
        if radius >= 28:
            image[circy, circx] = (220, 20, 20)
        else:
            image[circy, circx] = (20, 20, 220)

ax.imshow(image, cmap="grey")
plt.show()