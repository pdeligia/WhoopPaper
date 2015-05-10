OUTPUT='yieldmr_vs_yieldall.pdf'
# OUTPUT='yieldepp_vs_yieldall.pdf'
XLABEL='Analysis time (in seconds) using Whoop+Corral (Yield-MR)'
# XLABEL='Analysis time (in seconds) using Whoop+Corral (Yield-EPP)'
YLABEL='Analysis time (in seconds) using Corral (Yield-ALL)'
TIMEOUT=36000

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

# setup a figure
pp = PdfPages(OUTPUT)
fig, ax = plt.subplots(figsize=(6,6))

# plot the data (csb = 2)
ax.scatter(x0, y0, s=80, color='b', zorder = 10, marker='$2$', label='csb = 2')
# plot the data (csb = 5)
ax.scatter(x1, y1, s=80, color='g', zorder = 10, marker='$5$', label='csb = 5')
# plot the data (csb = 9)
ax.scatter(x2, y2, s=80, color='r', zorder = 10, marker='$9$', label='csb = 9')

# plot the data (csb = 2)
# ax.scatter(z0, y0, s=80, color='b', zorder = 10, marker='$2$', label='csb = 2')
# plot the data (csb = 5)
# ax.scatter(z1, y1, s=80, color='g', zorder = 10, marker='$5$', label='csb = 5')
# plot the data (csb = 9)
# ax.scatter(z2, y2, s=80, color='r', zorder = 10, marker='$9$', label='csb = 9')

# plot y=x line
xyline = np.logspace(math.log(0.0085,10), math.log(40000,10))
ax.plot(xyline, xyline, 'k--')

x2sp = np.logspace(math.log(0.00425,10), math.log(20500,10))
y2sp = np.logspace(math.log(0.0085,10), math.log(40000,10))
ax.plot(x2sp, y2sp, 'c-.', label='2x speedup')

x5sp = np.logspace(math.log(0.0017,10), math.log(8200,10))
y5sp = np.logspace(math.log(0.0085,10), math.log(41000,10))
ax.plot(x5sp, y5sp, 'y-.', label='5x speedup')

x10sp = np.logspace(math.log(0.00085,10), math.log(4100,10))
y10sp = np.logspace(math.log(0.0085,10), math.log(41000,10))
ax.plot(x10sp, y10sp, 'm-.', label='10x speedup')

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
  if x == TIMEOUT: return "TO"
  else: return "%g" % x
plt.yticks(locs, map(ylabel, locs), fontsize=14)

# add labels, legend and make it nicer
ax.set_xlabel(XLABEL)
ax.set_ylabel(YLABEL)
ax.set_xlim(5, TIMEOUT + 5000)
ax.set_ylim(5, TIMEOUT + 5000)
ax.legend(loc=4, prop={'size':12})

# done!
pp.savefig(fig, bbox_inches='tight')
pp.close()
