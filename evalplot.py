__author__ = 'Rene'
import os
from itertools import groupby
from operator import itemgetter
from pandas import DataFrame
from pandas import ExcelWriter
import os
from pylab import *
import matplotlib.pyplot as plt
import pandas as pd
import operator

path="C:\Users\Rene\Desktop\experimentos-2/nuevosconfig\data-griewank-12work-besthomo"
fig,ax = plt.subplots()
param=[]
# for counter, filename in enumerate(os.listdir(path)):
#     w12_file = open("%s/%s" % (path,filename))
#     parametros = [line.split(",") for counter, line in enumerate(w12_file) if counter == 1]
#     param.append((parametros[0][12],parametros[0][13]))

prom=[]
total=[]
max1=[]
todos=[]
evaluaciones=[]
for counter, filename in enumerate(os.listdir(path)):
    w12_file = open("%s/%s" % (path,filename))
    w12_records = [line.split(",") for line in w12_file if len(line.split(",")) > 3]
    ho=[list(g) for k,g in groupby(w12_records, key=itemgetter(0))]
    hmm=ho.sort(key=itemgetter(int(1)))
    #hmm= [list(m) for i,m in groupby(ho,key=itemgetter(float(1)))]
    #ho1=[list(g) for k,g in groupby(ho, key=itemgetter(1,1))]
    #max1=[]
    lista2=[]
    for y in ho:
        eval1=[]
        hmm = [list(m) for i,m in groupby(y,key=itemgetter(int(1)))]

        for o,b in enumerate(hmm):
            #local.append(int(b[o][9]))
            local=[]
            for n,x in enumerate(b):
                local.append(int(x[9]))
            todos.append(sum(local))
            maximo=max(local)
            eval1.append(maximo)
            del local
        #lista2=[]
        m1=max(eval1)
        prom.append(sum(todos))
        del todos[:]
        lista2.append(m1)
        if len(prom) == 1:
            #suma=sum(lista2)/float(len(lista2))
            #evaluaciones.append(sum(prom)/float(len(prom)))
            for i in prom:
                evaluaciones.append(i)
            #total.append(suma)
            #lista2.append(suma)
            #max1.append(lista2)
            #del eval1
            del lista2
            del prom[:]
        else:
            pass
        #del eval1
    l=[]

#max1.sort(key=operator.itemgetter(5))
si=sorted(evaluaciones, key=float)
so=sorted(total,key=float)
#total.sort(key=operator.itemgetter(5))
ax.set_title('Promedio de evaluaciones por configuracion.')
ax.set_ylabel("Numero de Evaluaciones")
ax.set_xlabel('Experimentos')
#ax.xaxis.set_ticks()
#ax.yaxis.set_ticks((0,5000),5000)
#fig=plt.figure(1,figsize=(9,6))
# ax=fig.add_subplot(111)
# bp=ax.boxplot(max1)
#ax1 = plt.subplots()
#list(range(0, len(total)))
#plt.scatter(list(range(0, len(total))),si)
#plt.plot(list(range(0, len(total))),si)
#plt.ylim([0,200000])
#ax.plot(list(range(0, len(total))),si)
ax.plot(list(range(0,len(evaluaciones))),si)
plt.scatter(list(range(0, len(evaluaciones))),si)
print si
#df=DataFrame({'X':x,'Y':y} for x, y in enumerate(si))
#df=DataFrame({'Y':y} for y in si)
df=DataFrame({'Y':y} for y in evaluaciones)
df.to_excel(("%s/%s" % (path,'evaluaciones.xlsx')), sheet_name='sheet1', index=False)
start, end = ax.get_ylim()
ax.yaxis.set_ticks(np.arange(0, end, 15000))
# box= plt.boxplot(total,0,'gD',patch_artist=True)
# hola=plt.gca()
# ax.axes.get_xaxis().set_visible(False)
# ax.set_title('Comparacion')
# ax.set_ylabel("Tiempo /segundos")
# ax.set_xlabel('Distribution')
#show()
plt.show()
