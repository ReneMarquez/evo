__author__ = 'Rene'
from pylab import *
import itertools, operator
import time
import matplotlib.pyplot as plt
import os

data=[]
box= plt.boxplot(data,0,'gD',patch_artist=True)
colors = ['cyan', 'lightblue', 'lightgreen', 'cyan', 'lightblue', 'lightgreen','cyan', 'lightblue', 'lightgreen','red','cyan','lightblue', 'lightgreen','red']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
#ax1.set_ylabel('Tiempo /segundos')
dat=plt.gca()
dat.axes.get_xaxis().set_visible(False)
dat.set_title('Comparacion')
dat.set_ylabel("Tiempo /segundos")
dat.set_xlabel('Distribution')

plt.figtext(0.75, 0.8, ' Homogeneo' ,
           backgroundcolor='cyan', color='black', weight='roman',
           size='small')
plt.figtext(0.75, 0.76, 'RPSS',
backgroundcolor='lightblue',
           color='black', weight='roman', size='small')

plt.figtext(0.75, 0.72, 'Segmentado',
backgroundcolor='lightgreen',
           color='black', weight='roman', size='small')

plt.figtext(0.17, 0.07, ' 2 Workers', color='black', weight='roman',
           size='small')
plt.figtext(0.37, 0.07, ' 4 Workers', color='black', weight='roman',
           size='small')
plt.figtext(0.60, 0.07, ' 6 Workers', color='black', weight='roman',
           size='small')
plt.figtext(0.80, 0.07, ' 12 Workers', color='black', weight='roman',
           size='small')
plt.figtext(0.30, 0.03, ' No. de Workers (Homogeneo/Heterogeneo/Segmentado)', color='black', weight='roman',
           size='medium')
#figure()
show()
# w12_records = [line.split(",") for line in w12_file if len(line.split(",")) == 3]
# y=tuple(x[1] for x in w12_records)
# x=range(0,len(w12_records))
# plt.plot(x,y)
# plt.ylabel('Tiempo Segundos')
# plt.xlabel('Experimento')
# plt.show()
# w12_evaluations = []
# for key, group in itertools.groupby(w12_records, key=operator.itemgetter(0)):
#     w12_evaluations.append( sum([row[9] for row in group]))

#print w12_evaluations