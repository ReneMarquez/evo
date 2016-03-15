__author__ = 'Rene'
from pylab import *
import itertools, operator
import time
import matplotlib.pyplot as plt
import os
# w12_file = open("C:\Users\Rene\Desktop\experientos\datai-3ec611df\data\one_griewank-w12-100-p1024-1415322186.dat")

#w12_records = [ map(float,line.split(",")[:-2]) for line in w12_file if len(line.split(",")) > 3 ]
# path="C:\Users\Rene\Desktop\experientos\datai-7a081a97\data"
# for filename in os.listdir(path):
#     w12_file = open("C:\Users\Rene\Desktop\experientos\datai-7a081a97\data\"" + str(filename))
#     w12_records = [line.split(",") for line in w12_file if len(line.split(",")) == 3]
#     y=tuple(x[1] for x in w12_records)
#     x=range(0,len(w12_records))
#     plt.plot(x,y)
#     plt.ylabel('Tiempo Segundos')
#     plt.xlabel('Experimento')
#     plt.show()
# work4=[250.81,248.99,251.87,300.13,253.51,254.35,253.41,300.34,252.52,296.26,250.81,248.99,251.87,300.13,253.51,254.35,253.41,300.34,252.52,296.63,294.48,254.08,249.48,254.56,288.8,255.96,249.32,281.78,286.45,243.98]
# work8=[38.37,113.9,45.91,146.76,129.4,130.54,81.82,126.18,130.81,147.79,148.55,129.21,130.84,149.28,147.81,113.37,124.58,131.01,131.15,117.92,67.45,77.77,117.6,78.43,132.41,67.46,158.39,132.41,87.54,112.65]
# work16=[51.1,40.19,49.07,32.49,29.75,51.77,50.37,156.9,33.06,28.43,28.01,85.23,30.39,53.54,33.63,67.94,27.03,46.33,34.61,41.08,27.35,27.14,39.19,40.56,132.17,28.17,34.15,27.71,46.69,48.37]
# work4=[14.47,22.8,18.59,14.69,18.35,12.51,17,16.51,11.96,10.47,14.61,18.65,14.5,10.27,14.38,12.6,16.9,17.07,18.65,11.97,16.9,16.31,12.47,14.49,18.68,10.38,10.54,12.32,15.66,6.32]
# work8=[8.49,8.83,8.62,8.43,8.72,9.97,8.47,8.81,10.76,6.72,8.46,8.33,5.02,8.34,6.68,8.39,12.58,8.62,8.73,8.33,8.38,8.57,10.54,8.41,8.54,8.39,10.44,8.32,8.55,8.42]
# work16=[5.22,6.61,8.72,5.33,9.01,5.11,9.03,8.07,5.43,9.51,8.8,4.95,9.17,5.62,8.72,8.81,8.95,9.95,5.03,9.13,8.75,9.15,4.97,9.12,8.71,5.27,4.9,9.16,9.37,4.91]
work2=[13753,15981,16492,17986,18213,18588,19152,19187,19271,19654,19670,19760,19767,19921,20459,21445,21961,22799,23558,23754,25936,29542,34780,46400,74434]
work22=[17.23,18.46,9.47,16.2,13.66,18.29,12.99,8.3,18.45,18.31,7.48,15.49,18.32,6.51,9.31,18.68,24.11,18.54,18.35,18.46,18.24,10.09,18.14,18.07,18.03,18.52,18.29,18.47,18.46,18.43]
work222=[18.54,18.12,14.5,14.66,14.43,14.56,14.54,8.74,14.49,14.29,14.62,14.67,14.68,14.49,14.4,14.69,18.16,14.55,14.28,14.75,23.25,14.53,14.55,14.54,14.7,14.74,14.74,14.36,14.6,18.99]
work4=[4,7.35,5.71,4.63,3.74,4.48,3.93,7.18,5.22,3.89,6.59,4.29,4.16,7.8,3.89,5.76,7.14,5.76,6.19,3.76,4.12,4.23,3.54,8.81,5.35,5.92,3.97,4.62,8.85,8.52]
work44=[19.92,14.67,4.64,23.62,10.11,24.6,22.13,28.76,21.2,9.85,26.3,5.25,10.16,11.86,8.77,13,19.98,9.76,14,8.86,6.19,10.45,15.42,9.51,12.31,4.78,5.59,17.19,4.08,26.19]
work444=[10.43,12.87,9.54,10.88,7.12,6.62,13.41,21.02,13.34,14.14,6.03,17.04,8.15,4.86,11.21,25.56,9.32,13.67,21.46,11.85,24.4,19.32,25.5,16.86,28.52,13.4,17.73,8.97,23.69,25.7]
work6=[4.53,4.39,4.32,4.38,4.73,4.57,3.76,4.6,5.04,4.28,6.73,4.35,5.7,5.12,4.19,4.78,4.59,4.48,3.92,4.2,4.56,4.26,4.12,3.64,4.39,4.47,5.32,4.28,4.28,4.2]
work66=[5.25,13.15,15.2,9.24,11.55,13.73,5.1,4.45,7.7,6.21,5.3,5.02,5.87,10.92,7.39,7.01,5.16,5.65,5.56,9.66,5.83,9.65,4.53,5,7.38,4.79,4.73,4.46,10.99,4.63]
work666=[4.84,9.6,4.8,19.13,5.23,9.28,11.58,6.34,16.11,5.61,7.91,6.17,5.46,4.8,17.56,5,9.98,12.24,12.37,5.01,5.41,4.63,10.84,10.29,10.37,12.74,4.48,5.85,5.35,5.29]
workred=[14.26,5.93,5.11,5.10,4.73,13.42,8.60,4.80,5.06,5.23,10.98,5.34,4.54,5.46,4.51,5.04,12.17,4.55,10.11,18.36,7.12,8.29,5.24,7.68,4.97,7.20,8.03,8.12,4.56,4.52]
work1=[5.24,5.95,5.95,5.72,5.98,5.53,5.74,4.49,5.85,6.04,5.76,5.18,6.14,4.89,5.33,6.07,6.04,5.03,4.99,6.13,5.86,5.68,5.69,5.61,5.47,5.86,5.00,5.26,6.89,5.26]
work12=[6.17,6.22,7.51,5.78,6.00,6.28,5.83,6.27,6.28,6.32,6.14,6.23,6.34,6.17,6.09,5.67,5.86,5.81,6.41,5.55,6.04,6.31,6.05,15.38,7.03,6.25,6.58,6.33,6.25,6.84]
work122=[9.15,6.17,7.21,6.01,6.05,5.55,6.17,6.43,5.87,5.59,6.14,5.55,5.56,7.16,5.58,5.82,5.54,6.13,6.24,8.62,14.07,6.8,6.06,6.05,5.8,5.68,5.99,8.39,5.92,5.99]
work1222=[6.21,5.75,6.80,7.23,6.09,5.86,7.19,6.04,5.99,6.52,5.43,6.02,6.17,13.27,6.11,6.13,6.03,6.00,6.00,5.83,6.09,6.42,6.78,6.09,6.26,7.17,6.04,5.90,7.27,6.18]

# data=concatenate((work4,work8,work16),0)
# data1=concatenate((work2,work1),0)
data=[work2,work22,work222,work4,work44,work444,work6,work66,work666,workred,work1,work12,work122,work1222]
box= plt.boxplot(data,0,'gD',patch_artist=True)
colors = ['cyan', 'lightblue', 'lightgreen', 'cyan', 'lightblue', 'lightgreen','cyan', 'lightblue', 'lightgreen','red','cyan','lightblue', 'lightgreen','red']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
#ax1.set_ylabel('Tiempo /segundos')
hola=plt.gca()
hola.axes.get_xaxis().set_visible(False)
hola.set_title('Comparacion')
hola.set_ylabel("Tiempo /segundos")
hola.set_xlabel('Distribution')

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