import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from skimage import io
from skimage.transform import resize, rescale
from skimage.color import rgb2gray
from skimage.filters import try_all_threshold, threshold_otsu
from skimage.morphology import disk, ball
from skimage.filters.rank import maximum

img = io.imread('airbus.png')

def getMaxDist(img, av):
    maxDist = 0.
    for y in range(np.shape(img)[0]):
        for x in range(np.shape(img)[1]):
            cand = np.linalg.norm(img[y, x] - av)
            if cand > maxDist:
                # print(f"[{y},{x}] = {niebo[y, x]}, cand = {cand}")
                maxDist = cand
    return maxDist

fig, ax = plt.subplots(figsize=(5, 5), constrained_layout=True)
print(np.shape(img))
niebo = img[255:np.shape(img)[0], 0:np.shape(img)[1]]
r_av = np.average(niebo[:,:,0])
g_av = np.average(niebo[:,:,1])
b_av = np.average(niebo[:,:,2])
av = np.array([r_av,g_av,b_av])

# print(getMaxDist(niebo, av))

maxDist = getMaxDist(niebo, av)

newImg = np.zeros((np.shape(img)[0], np.shape(img)[1], 3))
for y in range(np.shape(img)[0]):
    for x in range(np.shape(img)[1]):
        dist = np.linalg.norm(img[y, x] - av)
        if dist > maxDist:
            newImg[y,x] = 1
ax.imshow(newImg)

plt.show()
