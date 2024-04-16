import numpy as np
import skimage
from matplotlib import pyplot as plt
from skimage import io

img = skimage.data.camera()
hist, edges = np.histogram(img, 256)
fig, ax = plt.subplots(7, 2, figsize=(10, 5), constrained_layout=True)
ax[0][0].imshow(img, cmap="gray")
ax[0][1].plot(hist)
# print(hist)

img2 = skimage.exposure.rescale_intensity(img,(3,225), (0,1))
hist2, edges = np.histogram(img2, 256)
# print(hist2)
ax[1][0].imshow(img2, cmap="gray")
ax[1][1].plot(hist2)

img3 = io.imread('dark_image.png')
hist3, edges = np.histogram(img3, 256)
# print(hist3)
ax[2][0].imshow(img3, cmap="gray")
ax[2][1].plot(hist3)

img4 = skimage.exposure.rescale_intensity(img3,(4,50), (0,1))
hist4, edges = np.histogram(img4, 256)
# print(hist4)
ax[3][0].imshow(img4, cmap="gray")
ax[3][1].plot(hist4)

img5 = skimage.exposure.rescale_intensity(img3,(4,50), (0,1))
img5 = skimage.exposure.adjust_gamma(img5,0.5)
hist5, edges = np.histogram(img5, 256)
# print(hist4)
ax[4][0].imshow(img5, cmap="gray")
ax[4][1].plot(hist5)

#ten jest chyba najlepszy
img6 = skimage.exposure.rescale_intensity(img3,(4,50), (0,1))
img6 = skimage.exposure.adjust_gamma(img6,1.5)
hist6, edges = np.histogram(img6, 256)
# print(hist4)
ax[5][0].imshow(img6, cmap="gray")
ax[5][1].plot(hist6)

img7 = skimage.exposure.adjust_gamma(img3,1.5)
img7 = skimage.exposure.rescale_intensity(img7,(4,50), (0,1))
hist7, edges = np.histogram(img7, 256)
# print(hist4)
ax[6][0].imshow(img7, cmap="gray")
ax[6][1].plot(hist7)

plt.show()