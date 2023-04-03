import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sps
# This seeds the random number generator so that it always returns the same
# numbers
np.random.seed(20)

samples = 50
sigma = 0.3

mu1 = 2.15
data1 = mu1 + sigma*np.random.randn( samples )

mu2 = 2.0
data2 = mu2 + sigma*np.random.randn( samples )

t_one = sps.ttest_1samp(data1, 2.0)
t_ind = sps.ttest_ind(data1, data2)
t_rel = sps.ttest_rel(data1, data2)
output = '''From 2.0: {:f}
Comp means: {:f}
Comp diffs: {:f}'''

plt.figtext(0.15, 0.6, output.format(t_one[1], t_ind[1], t_rel[1]) )

plt.hist([data1, data2], bins=20)
plt.xlim(0, 3.5)

plt.show()
