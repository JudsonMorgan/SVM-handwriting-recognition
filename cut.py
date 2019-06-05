import os
import sys

import numpy as np
import matplotlib.pyplot as plt

from PIL import Image

from numba import jit

im_array = np.asarray(Image.open('svm.png').convert('L'))
last = 0
j = 0
i = 0
while j < im_array.shape[1]:
    line = im_array[:, j]
    while np.sum(line) == 255 * im_array.shape[0]:
        j += 1
        line = im_array[:, j]
        last = j
    print('first', j)
    while np.sum(line) != 255 * im_array.shape[0]:
        j += 1
        line = im_array[:, j]
    print('sec', j)

    k = 0
    last_row = 0
    row = im_array[k, (last - 50): (j + 50)]
    while np.sum(row) == 255 * row.shape[0]:
        k += 1
        row = im_array[k, (last - 50): (j + 50)]
        last_row = k
    print('first', k)
    while np.sum(row) != 255 * row.shape[0]:
        k += 1
        row = im_array[k, (last - 50): (j + 50)]
    print('sec', k)

    middle = (last_row + k) // 2
    how_far = ((j + 50) - (last - 50)) // 2

    im_strip = im_array[(middle - how_far): (middle + how_far), (last - 50): (j + 50)]
    last = j
    im = Image.fromarray(im_strip)
    im.save('converted/' + str(100 + i) + '.jpeg', "JPEG")
    j += 1
    i += 1
