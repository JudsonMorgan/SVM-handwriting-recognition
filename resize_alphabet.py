#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

import numpy as np
import matplotlib.pyplot as plt

from PIL import Image

from numba import jit

# height - sumuje po  rzedach (daje nam które rzedy)
# width - sumuje po kolumnach (daje nam które kolumn


@jit
def reshape_function(im_array=None, filename=None):
    height_arr = np.any(np.where(im_array == 0, True, False), axis=1)
    width_arr = np.any(np.where(im_array == 0, True, False), axis=0)

    height = np.argwhere(height_arr)
    width = np.argwhere(width_arr)

    left = width[0, 0]
    right = width[-1, 0]
    up = height[0, 0]
    down = height[-1, 0]
    if right - left > down - up:
        if left > len(width_arr) - right:
            left = len(width_arr) - right
        else:
            right = len(width_arr) - left
        up = left
        down = right
    else:
        if up > len(height_arr) - down:
            up = len(height_arr) - down
        else:
            down = len(height_arr) - up
        left = up
        right = down

    # left, upper, right, lower)
    # array to change
    im_strip = im_array[up:down + 1, left:right + 1]
    im = Image.fromarray(im_strip)

    #im.save(filename[:-4] + '.jpeg', "JPEG")

    im.resize((8, 8), Image.ANTIALIAS).save(filename[:-4] + '.jpeg', "JPEG")


folder_name = 'by_class'

list_folders_1 = os.listdir(folder_name)

for folder_1 in list_folders_1:
    list_folders_2 = [name for name in os.listdir(folder_name + "/" + folder_1) if os.path.isdir(folder_name + "/" + folder_1 + "/" + name)]
    path_to_save = folder_name + "/" + folder_1 + "/changed"

    try:
        os.mkdir(path_to_save)
    except:
        pass

    for folder_2 in list_folders_2:
        list_files_3 = [name for name in os.listdir(folder_name + "/" + folder_1 + "/" + folder_2) if os.path.isfile(folder_name + "/" + folder_1 + "/" + folder_2 + "/" + name)]
        print(folder_name + "/" + folder_1 + "/" + folder_2)
        for files_3 in list_files_3:
            patch_file = folder_name + "/" + folder_1 + "/" + folder_2 + "/" + files_3
            im_array = np.asarray(Image.open(patch_file).convert('L'))
            try:
                reshape_function(im_array, path_to_save + "/" + files_3)
            except Exception as ex:
                print(ex)
    # print(patch_file)
    #plt.imshow(im_array, cmap='gray', vmin=0, vmax=255)
    # plt.colorbar()
    # plt.show()
