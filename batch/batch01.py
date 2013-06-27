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
txt_files = []
for f in all_files:
    if f[-3:] == 'txt':
        txt_files.append( f )
# These constructs are called 'List Comprehensions' 
# They are more compact versions of the above code, and are actually more
# highly optimized than the for loops.
# See: http://docs.python.org/2/tutorial/datastructures.html#list-comprehensions
# Or: txt_files = [i for i in all_files if i[-3:] == 'txt']
# Or: txt_files = [i for i in os.listdir('.') if i[-3:] == 'txt']

for txt in txt_files:
    wn, ab = file_proc(txt)
    plt.plot(wn, ab, label=txt)

plt.xlim(500, 770)
plt.ylim(-0.01, 0.18)

plt.legend()
plt.show()
