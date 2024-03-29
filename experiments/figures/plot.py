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

x0 = [13.5, 41.3, 15.7, 3.1, 13.5, 14.5, 41.6, 40.7, 99.2, 95.5, 21.0, 55.8, 906.0, 15.9, 359.8, 36000]
x1 = [16.9, 79.4, 17.3, 3.1, 66.1, 16.1, 52.9, 295.3, 102.4, 1847.9, 32.0, 1698.6, 36000, 18.5, 5664.5, 36000]
x2 = [49.3, 1358.9, 23.9, 3.1, 689.3, 19.3, 104.6, 8883.0, 107.6, 36000, 278.0, 36000, 36000, 24.3, 36000, 36000]

z0 = [17.7, 79.4, 26.1, 3.1, 14.7, 22.3, 91.2, 62.6, 104.0, 164.9, 44.4, 96.2, 1924.4, 16.1, 474.7, 36000]
z1 = [24.2, 432.4, 31.2, 3.1, 70.0, 25.7, 150.7, 405.7, 105.5, 2309.8, 89.6, 2249.0, 36000, 18.5, 12677.3, 36000]
z2 = [132.1, 22514.1, 55.2, 3.2, 748.0, 33.0, 633.2, 33468.4, 107.1, 36000, 1543.4, 36000, 36000, 24.5, 36000, 36000]

y0 = [33.5, 169.3, 38.1, 11.1, 22.8, 35.0, 182.6, 81.5, 388.0, 271.0, 39.8, 99.6, 1966.5, 12.9, 548.2, 36000]
y1 = [47.0, 595.1, 45.6, 13.8, 130.3, 40.2, 263.7, 419.4, 390.8, 2746.6, 85.0, 2376.8, 36000, 15.2, 14469.0, 36000]
y2 = [197.5, 27337.6, 78.4, 37.3, 1571.7, 51.8, 793.0, 36000, 392.1, 36000, 1539.9, 36000, 36000, 21.4, 36000, 36000]

# setup a figure
pp = PdfPages(OUTPUT)
fig, ax = plt.subplots(figsize=(6.5,6.5))

# plot the data (csb = 2)
ax.scatter(x0, y0, s=60, color='b', zorder = 10, marker='+')
# plot the data (csb = 5)
ax.scatter(x1, y1, s=60, color='g', zorder = 10, marker='o', facecolors='none')
# plot the data (csb = 9)
ax.scatter(x2, y2, s=60, color='r', zorder = 10, marker='x', facecolors='none')

# plot the data (csb = 2)
# ax.scatter(z0, y0, s=60, color='b', zorder = 10, marker='+')
# plot the data (csb = 5)
# ax.scatter(z1, y1, s=60, color='g', zorder = 10, marker='o', facecolors='none')
# plot the data (csb = 9)
# ax.scatter(z2, y2, s=60, color='r', zorder = 10, marker='x', facecolors='none')

# plot y=x line
xyline = np.logspace(math.log(0.0085,10), math.log(40000,10))
ax.plot(xyline, xyline, 'k--')

x2sp = np.logspace(math.log(0.00425,10), math.log(20500,10))
y2sp = np.logspace(math.log(0.0085,10), math.log(40000,10))
ax.plot(x2sp, y2sp, 'c-.', label='2x speedup')

# x5sp = np.logspace(math.log(0.0017,10), math.log(8200,10))
# y5sp = np.logspace(math.log(0.0085,10), math.log(41000,10))
# ax.plot(x5sp, y5sp, 'g-.', label='5x speedup')

x10sp = np.logspace(math.log(0.00085,10), math.log(4100,10))
y10sp = np.logspace(math.log(0.0085,10), math.log(41000,10))
ax.plot(x10sp, y10sp, 'm-.', label='10x speedup')

# x20sp = np.logspace(math.log(0.000425,10), math.log(2050,10))
# y20sp = np.logspace(math.log(0.0085,10), math.log(41000,10))
# ax.plot(x20sp, y20sp, 'y-.', label='20x speedup')

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
ax.set_xlim(2, TIMEOUT + 5000)
ax.set_ylim(2, TIMEOUT + 5000)
ax.legend(loc=4, prop={'size':12})

# done!
pp.savefig(fig, bbox_inches='tight')
pp.close()
