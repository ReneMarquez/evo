__author__ = 'Rene'

import os
from pylab import *
import matplotlib.pyplot as plt
import pandas as pd

path="C:\Users\Rene\Desktop\experimentos-2/nuevosconfig\eval-griewank-homo"
fig, ax = plt.subplots()

files=[]
for counter, filename in enumerate(os.listdir(path)):
    file = pd.read_excel(("%s/%s" % (path,filename)))
    files.append(file)

# lista=[]
# for i,a in enumerate(files):
#     lista.append((a[i]['Y']))

# for i in files:
#     bp= i.boxplot(by='Y',patch_artist=True)
#box= plt.b'oxplot(files,0,'gD',patch_artist=True)

box= plt.boxplot(files,patch_artist=True)

#plt.xticks([1,2,3,4,5,6],['                       6 workers','','           ','','     12 workers     ','','               '])

plt.xticks([1,2,3],[' 2 workers','6 workers','12 workers ','','     '])
# plt.scatter(files[0]['X'],files[0]['Y'],color="blue")
# plt.scatter(files[1]['X'], files[1]['Y'],color="yellow")
# plt.scatter(files[2]['X'], files[2]['Y'],color='red')
# plt.plot(files[0]['X'],files[0]['Y'])
# plt.plot(files[1]['X'],files[1]['Y'],color='yellow')
# plt.plot(files[2]['X'],files[2]['Y'])
# file.plot(x='X', y='Y')
# file.scatter(ax=ax, positions=[1], notch=True)
colors = ['cyan', 'lightblue','blue', 'cyan', 'lightblue','blue', 'cyan', 'lightblue','blue','cyan','lightblue']
for patch, color in zip(box['boxes'], colors):
     patch.set_facecolor(color)
#Promedio
#ax.set_ylabel("Tiempo /segundos")
# ax.set_xlabel('Experimentos (Menor a mayor)')
ax.set_ylabel('No. de Evaluaciones')
#Evaluaciones
#ax.set_ylabel("No. de Evaluaciones")
ax.set_xlabel('No. de workers')

start, end = ax.get_ylim()
ax.yaxis.set_ticks(np.arange(0, end,10000))
# ax.set_xticks(range(5))
# ax.set_xticklabels(range(5))
# plt.figtext(0.70, 0.7, ' Heterogeneo' ,
#            backgroundcolor='cyan', color='black', weight='roman',
#            size='small')
# plt.figtext(0.70, 0.66, 'Mejor Homogeneo',
# backgroundcolor='lightblue',
#            color='black', weight='roman', size='small')
# plt.figtext(0.70, 0.62, 'Promedio Homogeneo',
# backgroundcolor='blue',
#            color='black', weight='roman', size='small')
# plt.figtext(0.75, 0.22, '6 workers',
# backgroundcolor='red',
#            color='black', weight='roman', size='small')
plt.show()