import os
import sys

import numpy as np
import matplotlib.pyplot as plt

x, y = [], []
x_pt, y_pt = [], []
for file in txt_files:
    with open('dataset/' + file) as f:
        end = os.stat('dataset/' + file).st_size
        indexes = np.random.choice(end, 1100, replace=False)
        for i in indexes[0:1000]:
            f.seek(i)
            line = f.readline()
            x.append(np.fromstring(line, sep=' '))
        y.append([file[:2]] * 1000)
        for i in indexes[10000:]:
            f.seek(i)
            x_pt.append(np.fromstring(f.readline()))
        y_pt.append([file[:2]] * 100)
