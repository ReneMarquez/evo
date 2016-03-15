__author__ = 'Rene'

import os
from pylab import *
import matplotlib.pyplot as plt
import pandas as pd

path="C:\Users\Rene\Desktop\experientos\data-ONEMAX-24WRandom\info"
fig, ax = plt.subplots()

files=[]
for counter, filename in enumerate(os.listdir(path)):
    file = pd.read_excel(("%s/%s" % (path,filename)))
    files.append(file)

plt.scatter(files[0]['X'],files[0]['Y'],color="blue")
#3plt.scatter(files[1]['X'], files[1]['Y'],color="yellow")
# plt.scatter(files[2]['X'], files[2]['Y'],color='red')
# plt.scatter(files[3]['X'], files[3]['Y'],color='orange')
plt.plot(files[0]['X'],files[0]['Y'])
#plt.plot(files[1]['X'],files[1]['Y'],color='yellow')
# plt.plot(files[2]['X'],files[2]['Y'],color='red')
# plt.plot(files[3]['X'],files[3]['Y'],color='orange')
#file.plot(x='X', y='Y')
#file.scatter(ax=ax, positions=[1], notch=True)
ax.set_ylabel("Tiempo /segundos")
ax.set_xlabel('Experimentos (Menor a mayor)')
start, end = ax.get_ylim()
ax.yaxis.set_ticks(np.arange(0, 50, 5))
#ax.set_xticks(range(5))
#ax.set_xticklabels(range(5))
# plt.figtext(0.75, 0.5, ' RPSS' ,
#            backgroundcolor='blue', color='black', weight='roman',
#            size='small')
# plt.figtext(0.75, 0.26, '4 workers',
# backgroundcolor='red',
#            color='black', weight='roman', size='small')
# plt.figtext(0.75, 0.22, '6 workers',
# backgroundcolor='orange',
#            color='black', weight='roman', size='small')
# plt.figtext(0.75, 0.26, 'Segmentado',
# backgroundcolor='yellow',
#            color='black', weight='roman', size='small')
plt.show()