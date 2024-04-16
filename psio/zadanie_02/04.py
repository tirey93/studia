import matplotlib.pyplot as plt
import numpy as np
import skimage
def fun(x, a):
    y = round(a*x - (a*128) + 128)
    if y <= 0:
        y = 0
    if y >= 255:
        y = 255
    return y

img = skimage.data.moon()
# print(img)
hist, edges = np.histogram(img, 256)
fig, ax = plt.subplots(4, 2, figsize=(10, 5), constrained_layout=True)
ax[0][0].imshow(img, cmap="gray")
ax[0][1].plot(hist)

x=np.arange(256)

lut1=np.zeros((256,), dtype=np.uint8)
lut1 = np.array([fun(x, 1) for x in range(256, )])
img1=lut1[img]
# print(img2)
his1,edges = np.histogram(img1, 256)
ax[1][0].imshow(img1, cmap="gray")
ax[1][1].bar(x,his1)

lut2=np.zeros((256,), dtype=np.uint8)
lut2 = np.array([fun(x, 0.5) for x in range(256, )])
img2=lut2[img]
# print(img2)
his2,edges = np.histogram(img2, 256)
ax[2][0].imshow(img2, cmap="gray")
ax[2][1].bar(x,his2)

lut3=np.zeros((256,), dtype=np.uint8)
lut3 = np.array([fun(x, 1.5) for x in range(256, )])
img3=lut3[img]
# print(img2)
his3,edges = np.histogram(img3, 256)
ax[3][0].imshow(img3, cmap="gray")
ax[3][1].bar(x,his3)


plt.show()
