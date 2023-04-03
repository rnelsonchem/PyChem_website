import numpy as np
import matplotlib.pyplot as plt

wn, ab = [], []

data_file = open('uv_data.txt')

for line in data_file:
    sp = line.split(',')
    wn.append( sp[0] )
    ab.append( sp[1] )

data_file.close()

wn = np.array(wn, dtype=float)
ab = np.array(ab, dtype=float)

plt.plot(wn, ab)
plt.xlim(500,750)
plt.ylim(-0.01, 0.05)

plt.show()