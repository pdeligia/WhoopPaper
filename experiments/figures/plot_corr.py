OUTPUT='correlation.pdf'
XLABEL='Analysis time (in seconds)'
YLABEL='Number of instrumented yields'
TIMEOUT=36000
YIELDS=18000

import numpy as np
import matplotlib.pyplot as plt
import math
import sys

from matplotlib.backends.backend_pdf import PdfPages

plt.rcParams['xtick.minor.size'] = 0
plt.rcParams['ytick.minor.size'] = 0

x0 = [13.5, 41.3, 15.7, 3.1,    14.5, 41.6,    99.2, 95.5, 21.0,              906.0, 15.9]
x1 = [16.9, 79.4, 17.3, 3.1,    16.1, 52.9,    102.4, 1847.9, 32.0,           36000, 18.5]
x2 = [49.3, 1358.9, 23.9, 3.1,  19.3, 104.6,   107.6, 0, 278.0,               36000, 24.3]

z0 = [17.7, 79.4, 26.1, 3.1,   22.3, 91.2,     104.0, 164.9, 44.4,        1924.4, 16.1]
z1 = [24.2, 432.4, 31.2, 3.1,  25.7, 150.7,    105.5, 2309.8, 89.6,       36000, 18.5]
z2 = [132.1, 0, 55.2, 3.2,     33.0, 633.2,    107.1, 0, 1543.4,          36000, 24.5]

y0 = [33.5, 169.3, 38.1, 11.1   , 35.0, 182.6,   388.0, 271.0, 39.8,            1966.5, 12.9]
y1 = [47.0, 595.1, 45.6, 13.8   , 40.2, 263.7,   390.8, 2746.6, 85.0,           36000, 15.2]
y2 = [197.5, 36000, 78.4, 37.3   , 51.8, 793.0,   392.1, 36000, 1539.9,         36000, 21.4]

yx = [29, 167, 22, 0,    129, 286,     812, 805, 601,      1024, 217]

yz = [47, 500, 51, 0,    245, 664,     1143, 996, 732,      1566, 227]

yy = [92, 691, 104, 82,  513, 801,     2058, 1270, 732,      1745, 227]

# setup a figure
pp = PdfPages(OUTPUT)
fig, ax = plt.subplots(figsize=(8,8))

# plot the data (csb = 2)
ax.scatter(x0, yx, s=80, color='b', zorder = 10, marker='$2$', label='csb = 2 (Yield-MR)')
# plot the data (csb = 5)
ax.scatter(x1, yx, s=80, color='b', zorder = 10, marker='$5$', label='csb = 5 (Yield-MR)')
# plot the data (csb = 9)
ax.scatter(x2, yy, s=80, color='b', zorder = 10, marker='$9$', label='csb = 9 (Yield-MR)')

# plot the data (csb = 2)
ax.scatter(z0, yz, s=80, color='g', zorder = 10, marker='$2$', label='csb = 2 (Yield-EPP)')
# plot the data (csb = 5)
ax.scatter(z1, yz, s=80, color='g', zorder = 10, marker='$5$', label='csb = 5 (Yield-EPP)')
# plot the data (csb = 9)
ax.scatter(z2, yy, s=80, color='g', zorder = 10, marker='$9$', label='csb = 9 (Yield-EPP)')

# plot the data (csb = 2)
ax.scatter(y0, yy, s=80, color='r', zorder = 10, marker='$2$', label='csb = 2 (Yield-ALL)')
# plot the data (csb = 5)
ax.scatter(y1, yy, s=80, color='r', zorder = 10, marker='$5$', label='csb = 5 (Yield-ALL)')
# plot the data (csb = 9)
ax.scatter(y2, yy, s=80, color='r', zorder = 10, marker='$9$', label='csb = 9 (Yield-ALL)')

# setup log scales
ax.set_xscale('log')
ax.set_yscale('log')

# label timeout and remove redundant 0.1 from x-axis
locs,labels = plt.xticks()
locs = np.concatenate((locs,[TIMEOUT]))
def xlabel(x):
  if x == TIMEOUT: return "TO"
  elif x == 0.01: return ""
  else: return "%g" % x
plt.xticks(locs, map(xlabel, locs), fontsize=14)
def ylabel(x):
  if x == YIELDS: return "18000"
  else: return "%g" % x
plt.yticks(locs, map(ylabel, locs), fontsize=14)

# add labels, legend and make it nicer
ax.set_xlabel(XLABEL)
ax.set_ylabel(YLABEL)
ax.set_xlim(5, TIMEOUT + 5000)
ax.set_ylim(5, YIELDS)
ax.legend(loc=4, prop={'size':12})

# done!
pp.savefig(fig, bbox_inches='tight')
pp.close()
