import numpy as np
import matplotlib.pylab as plt

data_file = open('nmr_data.txt')

intensity = []

for line in data_file:
    if 'LEFT' in line:
        sp = line.split()
        left = float(sp[3])
        right = float(sp[-2])

    elif 'SIZE' in line:
        sp = line.split()
        size = int(sp[3])

    elif line[0] == '#': 
        continue

    else: 
        intensity.append( line )

ppm = np.linspace(left, right, size)
intensity = np.array(intensity, dtype=float)

# Create a new plot
plt.figure() 

# This is going to use Matplotlib's object-oriented approach to plotting,
# which is much more powerful, but also more difficult, than the pyplot
# approach. This method allows us to shut off some of the lines around the
# outside of the plot. The Matplotlib documentation has lots of info on this
# subject. Start: http://matplotlib.org/users/artists.html
# However, running in IPython interactive mode can help a lot here so that you
# can inspect object attributes as the are being created. Many of the 'pyplot'
# functions are wrappers around the object oriented interface, so you can get
# a feel for this style by looking at the pyplot source code. In IPython, you
# can follow the name of a function with two question marks (??) to get the
# source for that function.

# Create axes (box for plotting), which is a subset of the figure
ax1 = plt.axes() 
ax1.plot(ppm, intensity, '-')

# Spines are the axes boundries. Shut them off at certain locations.
for loc in ['left', 'right', 'top']:
    ax1.spines[loc].set_color('none')

# Turn off ticks where there is no spine
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('none')

# Turn off y tick labels, must use an empty list to force no labels
ax1.set_yticks( [] )

# A lot of the OO commands start with set/get
ax1.set_xlim(8.9, 0.5)
ax1.set_ylim(-1.0e6, 6e7)
ax1.set_xlabel('ppm')

# Let's make an inset to this figure as well
ax2 = plt.axes([0.2, 0.5, 0.4, 0.4])
ax2.plot(ppm, intensity, '-')

# This stuff is the same as above, but only for the second axes
# Because this is exactly the same as above, it would have been better to
# rewrite this as a function, so that we don't have to make multiple changes
# to the same code later.
for loc in ['left', 'right', 'top']:
    ax2.spines[loc].set_color('none')
ax2.xaxis.set_ticks_position('bottom')
ax2.yaxis.set_ticks_position('none')
ax2.set_yticks( [] )
ax2.set_xlim(8.7, 6.6)
ax2.set_ylim(-1.0e5, 0.5e7)

plt.show()

