import os

import numpy as np
import matplotlib.pyplot as plt

def file_proc(file_name):
    file_object = open(file_name)
    
    wn, ab = [], []

    for line in file_object:
        if line[0] == '"': continue
        sp = line.split(',')
        wn.append( sp[0] )
        ab.append( sp[1] )

    file_object.close()
    
    return np.array(wn, dtype=float), np.array(ab, dtype=float)

all_files = os.listdir('.')

for fl in all_files:
    # Only process '*.txt' files.
    if fl[-3:] == 'txt':
        wn, ab = file_proc(fl)
        plt.plot(wn, ab, label=fl)

plt.xlim(500, 770)
plt.ylim(-0.01, 0.18)

plt.legend()
plt.show()
