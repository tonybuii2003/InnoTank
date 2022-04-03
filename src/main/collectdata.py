# The dataset needed can be downloaded at: http://web.cecs.pdx.edu/~singh/rcyc-web/dataset.html
# Originally intended for designing a TensorFlow Keras supervised ML model

import os
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

def unpickle(file):
    with open(file, 'rb') as fo:
        data = np.load(file)
    x, y = data['x'], data['y']
    return x, y

try:
    os.mkdir('/recycled_32/bottle_train')
    os.mkdir('/recycled_32/bottle_test')
except OSError:
    pass

train_dir = "/recycled_32/bottle_train/"
test_dir = "/recycled_32/bottle_test/"

imgs, labels = unpickle("/recycled_32/recycled_32_train.npz")

imgs = imgs[-2000:]
labels = labels[-2000:]

newimg = np.zeros((32, 32, 3), dtype=np.uint8)

for i in range(0, 2000):
    newimg = np.moveaxis(imgs[i], 0, 2)
    img = Image.fromarray(newimg, 'RGB')
    if i < 1799:
        img.save(train_dir + str(i) + '.png')
    else:
        img.save(test_dir + str(i) + '.png')
