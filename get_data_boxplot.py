__author__ = 'Rene'
import os
from pandas import DataFrame
from pandas import ExcelWriter
import os
from pylab import *
import matplotlib.pyplot as plt
import pandas as pd
import operator

path="C:\Users\Rene\Desktop\experientos\data-GRIEWANK-100dimensiones-HETE6w"
# param=[]
# for counter, filename in enumerate(os.listdir(path)):
#     w12_file = open("%s/%s" % (path,filename))
#     parametros = [line.split(",") for counter, line in enumerate(w12_file) if counter == 1]
#     param.append((parametros[0][12],parametros[0][13]))

tiempo=[]
total=[]
for counter, filename in enumerate(os.listdir(path)):
    w12_file = open("%s/%s" % (path,filename))
    w12_records = [line.split(",") for line in w12_file if len(line.split(",")) == 3]
    l=[]
    promedio=0
    for x in w12_records:
        promedio=promedio + float(x[1])
        l.append((counter,x[1]))
        tiempo.append(x[1])
        if len(l)==5:
            promedio=promedio/5
            print l,promedio
            tiempo.append(promedio)
            tiempo= map(float, tiempo)
            total.append(tiempo)
            tiempo=[]
            #total.append(promedio)
            #tiempo.append(promedio)
            del l
        else:
            pass

total.sort(key=operator.itemgetter(5))
#writer = ExcelWriter(path)
# for n in len(total):
#     n = DataFrame({'ok':df1[n]} for n,df1 in enumerate(total))
# for n, df1 in enumerate(total):
#     df=DataFrame({'ok':df1[n]} for df1 in total)
#     #df1.to_excel(writer, 'sheet1')
# writer.save()

#x=list[range(1,len(total))]
#path="C:\Users\Rene\Desktop\experientos\data-100-2workers\promedio"
#fig, ax = plt.subplots()
fig=plt.figure(1,figsize=(9,6))
ax=fig.add_subplot(111)
bp=ax.boxplot(total)
# box= plt.boxplot(total,0,'gD',patch_artist=True)
# hola=plt.gca()
ax.axes.get_xaxis().set_visible(False)
ax.set_title('Comparacion')
ax.set_ylabel("Tiempo /segundos")
ax.set_xlabel('Distribution')
start, end = ax.get_ylim()
ax.yaxis.set_ticks(np.arange(0, end, 10))
show()
# files=[]
# for counter, filename in enumerate(os.listdir(path)):
#     file = pd.read_excel(("%s/%s" % (path,filename)))
#     files.append(file)

# df=DataFrame({'X':x,'Y':y} for x, y in enumerate(total))
# df.to_excel(("%s/%s" % (path,'promedio.xlsx')), sheet_name='sheet1', index=False)
