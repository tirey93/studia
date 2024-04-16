import matplotlib.pyplot as plt
import matplotlib.image as mping
from skimage import io
from skimage.transform import resize, rescale
from skimage.color import rgb2gray
from PIL import Image
import numpy as np

import numpy

lenaPath = 'C:\\Users\\damia\\Pictures\\dane obrazowe-20240303\\input1\\lena.png'
dogPath = 'C:\\Users\\damia\\Pictures\\dane obrazowe-20240303\\input1\\dog_1.jpg'
# %matplotlib inline

def z1():
    img = io.imread(lenaPath)
    # img = mptimg.imread(lenaPath)
    print(img.shape)
    img = rgb2gray(img)

    # img = resize(img, (2 * img.shape[0], 2 * img.shape[1]), anti_aliasing=True)
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.imshow(img, cmap='gray')  # constrained_layout=True)
    plt.axis('off')
    plt.show()


numpy.set_printoptions(suppress=True, linewidth=400)

def extendShorterSide(array):
    max_size = max(array.shape[0], array.shape[1])
    min_size = min(array.shape[0], array.shape[1])
    empty = np.zeros((max_size, max_size))

    if array.shape[0] < array.shape[1]:
        empty[:min_size, :] = array
    elif array.shape[0] > array.shape[1]:
        empty[:, :min_size] = array
    else:
        empty = array
    return empty


def trimLongerSide(array):
    y = array.shape[0]
    x = array.shape[1]
    shorter = x if x < y else y
    offset_x = (x - shorter) // 2 if y == shorter else 0
    offset_y = (y - shorter) // 2 if x == shorter else 0
    return array[1 + offset_y:offset_y + shorter + 1, 1 + offset_x:offset_x + shorter + 1]

def cutSquareFromArray(square_dim, array):
    start_x = (array.shape[0] - square_dim) // 2
    start_y = (array.shape[1] - square_dim) // 2

    array[start_x:start_x + square_dim, start_y:start_y + square_dim] = 0
    return array

def zad1():
    array = np.random.randint(0, 100, size=(9, 4))
    print(array)
    print('\n')

    # lustrzanego odbicia obrazu w poziomie
    print(array[::-1])
    print('\n')

    # lustrzanego odbicia obrazu w pionie
    print(array[..., ::-1])
    print('\n')

    # obrotu obrazu o 90°
    print(numpy.rot90(array, k=1))
    print('\n')

    #w prawo oraz 90° w lewo
    print(numpy.rot90(array, k=3))
    print('\n')

    # obrót obrazu o 180°
    print(numpy.rot90(array, k=2))
    print('\n')

    # rozszerzenia macierzy do kwadratu MxM (jeżeli M>N) - kolumny po lewej i prawej stronie są wyzerowane
    print(extendShorterSide(array))
    print('\n')

    # wycięcia z macierzy kwadratu NxN (jeżeli M>N) - wycinamy środkową część macierzy
    print(cutSquareFromArray(3, array))
    print('\n')


def zad2_1():
    fig, ax = plt.subplots()
    img = Image.open(lenaPath).convert("L")
    plt.imshow(img, cmap=plt.cm.gray)

    plt.axis('off')
    plt.show()

def zad2_2():
    background = numpy.zeros((640, 480, 3), dtype=numpy.uint8)
    background[:,:,0] = 0
    background[:,:,1] = 0
    background[:,:,2] = 0

    img = io.imread(lenaPath)

    start_x = (background.shape[0] - img.shape[0]) // 2
    start_y = (background.shape[1] - img.shape[1]) // 2
    background[start_x:start_x + img.shape[0], start_y:start_y + img.shape[1]] = img

    fig, ax = plt.subplots()
    ax.imshow(background, cmap='gray')

    plt.axis('off')
    plt.show()
def zad2_3():
    background = numpy.zeros((640, 480, 3), dtype=numpy.uint8)
    background[:,:,0] = 0
    background[:,:,1] = 0
    background[:,:,2] = 0

    img = io.imread(lenaPath)

    start_x = (background.shape[0] - img.shape[0]) // 2
    start_y = (background.shape[1] - img.shape[1]) // 2
    background[start_x:start_x + img.shape[0], start_y:start_y + img.shape[1]] = img
    fig, ax = plt.subplots(3, 3, figsize=(5, 5), constrained_layout=True)


    # lustrzanego odbicia obrazu w poziomie
    ax[0][0].imshow(np.fliplr(background), cmap='gray')
    print('\n')

    # lustrzanego odbicia obrazu w pionie
    ax[0][1].imshow(np.flipud(background), cmap='gray')

    # obrotu obrazu o 90°
    ax[0][2].imshow(numpy.rot90(background, k=1), cmap='gray')

    # w prawo oraz 90° w lewo
    ax[1][0].imshow(numpy.rot90(background, k=3), cmap='gray')

    # obrót obrazu o 180°
    ax[1][1].imshow(numpy.rot90(background, k=2), cmap='gray')
    print('\n')

    # rozszerzenia macierzy do kwadratu MxM (jeżeli M>N) - kolumny po lewej i prawej stronie są wyzerowane
    ax[1][2].imshow(extendShorterSide_3d(background), cmap='gray')
    print('\n')

    # wycięcia z macierzy kwadratu NxN (jeżeli M>N) - wycinamy środkową część macierzy
    ax[2][0].imshow(cutSquareFromArray(50, background), cmap='gray')
    print('\n')

    plt.axis('off')
    plt.show()


def zad3():
    img = io.imread(dogPath)
    img = trimLongerSide(img)
    fig, ax = plt.subplots()
    ax.imshow(img)

    plt.axis('off')
    plt.show()
def createSubArraysFromArray(array, size):
    raSize = int(array.shape[0] / size)
    result = np.empty(shape=(size, size, raSize, raSize, 3), dtype=int)
    for i in range(size):
        for j in range(size):
            a1 = array[i * raSize:i * raSize + raSize, j * raSize:j * raSize + raSize]
            result[i][j] = a1
    return result


def recreateFullArrayFromSubArrays(subArrays):
    rSize = subArrays.shape[0] * subArrays.shape[2]
    result = np.zeros(shape=(rSize, rSize, 3), dtype=int)
    size = subArrays.shape[0]
    raSize = int(rSize / size)

    for i in range(size):
        for j in range(size):
            result[i * raSize:i * raSize + raSize, j * raSize:j * raSize + raSize] = subArrays[i][j]
    return result
def zad3(size):
    img = io.imread(dogPath)
    img = trimLongerSide(img)

    subArrays = createSubArraysFromArray(img, size)

    for i in range(subArrays.shape[0]):
        np.random.shuffle(subArrays[i])
    np.random.shuffle(subArrays)

    img2 = recreateFullArrayFromSubArrays(subArrays)

    fig, ax = plt.subplots()
    ax.imshow(img2)
    plt.axis('off')
    plt.show()
def extendShorterSide_3d(array):
    max_size = max(array.shape[0], array.shape[1])
    min_size = min(array.shape[0], array.shape[1])
    empty = np.zeros((max_size, max_size, 3), dtype=int)

    if array.shape[0] < array.shape[1]:
        empty[:min_size, :] = array
    elif array.shape[0] > array.shape[1]:
        empty[:, :min_size] = array
    else:
        empty = array
    return empty


zad1()
zad2_1()
zad2_2()
zad2_3()
zad3(3)











