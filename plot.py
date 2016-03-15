__author__ = 'Rene'
import os
from pylab import *
import matplotlib.pyplot as plt
import pandas as pd

path="C:\Users\Rene\Desktop\experimentos-2\config\eval-griewank"
fig, ax = plt.subplots()

files=[]
for counter, filename in enumerate(os.listdir(path)):
    file = pd.read_excel(("%s/%s" % (path,filename)))
    files.append(file)

current = files[0].rename(columns={'Name': '1'})
for i, frame in enumerate(files[1:]):
    current = current.merge(frame,left_index=True, right_index=True, how='outer').rename(columns={'Name': 'tiempo%d' % i})

current.boxplot(ax=ax, positions=[1], notch=True)
ax.set_ylabel("Tiempo /segundos")
ax.set_xlabel('Distribution')
ax.set_xticks(range(5))
ax.set_xticklabels(range(5))
plt.show()