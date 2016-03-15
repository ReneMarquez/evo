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

path="C:\Users\Rene\Desktop\experimentos-2/nuevosconfig\data-esfera-12workers-besthomo"
param=[]
# for counter, filename in enumerate(os.listdir(path)):
#     w12_file = open("%s/%s" % (path,filename))
#     parametros = [line.split(",") for counter, line in enumerate(w12_file) if counter == 1]
#     param.append((parametros[0][12],parametros[0][13]))

tiempo=[]
total=[]
max1=[]
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
            maximo=max(local)
            eval1.append(maximo)
            del local
        #lista2=[]
        m1=max(eval1)
        lista2.append(m1)
        if len(lista2) == 5:
            suma=sum(lista2)/float(len(lista2))
            total.append(suma)
            lista2.append(suma)
            max1.append(lista2)
            del eval1
            del lista2
        else:
            pass
        #del eval1
    l=[]

#print max1
max1.sort(key=operator.itemgetter(5))
fig=plt.figure(1,figsize=(9,6))
ax=fig.add_subplot(111)
bp=ax.boxplot(max1)
#ax1 = plt.subplots()
#list(range(0, len(total)))
plt.plot(total,list(range(0, len(total))))
# box= plt.boxplot(total,0,'gD',patch_artist=True)
# hola=plt.gca()
ax.axes.get_xaxis().set_visible(False)
ax.set_title('Comparacion')
ax.set_ylabel("Tiempo /segundos")
ax.set_xlabel('Distribution')
#show()
plt.show()
    # promedio=0
    # for x in w12_records:
    #     promedio=promedio + float(x[1])
    #     l.append((counter,x[1],param[counter]))
    #     tiempo.append(x[1])
    #     if len(l)==5:
    #         promedio=promedio/5
    #         print l,promedio
    #         tiempo.append(promedio)
    #         tiempo= map(float, tiempo)
    #         total.append(tiempo)
    #         tiempo=[]
    #         #total.append(promedio)
    #         #tiempo.append(promedio)
    #         del l
    #     else:
    #         pass

# total.sort(key=operator.itemgetter(5))
# #writer = ExcelWriter(path)
# # for n in len(total):
# #     n = DataFrame({'ok':df1[n]} for n,df1 in enumerate(total))
# # for n, df1 in enumerate(total):
# #     df=DataFrame({'ok':df1[n]} for df1 in total)
# #     #df1.to_excel(writer, 'sheet1')
# # writer.save()
#
# #x=list[range(1,len(total))]
# #path="C:\Users\Rene\Desktop\experientos\data-100-2workers\promedio"
# #fig, ax = plt.subplots()
# fig=plt.figure(1,figsize=(9,6))
# ax=fig.add_subplot(111)
# bp=ax.boxplot(total)
# # box= plt.boxplot(total,0,'gD',patch_artist=True)
# # hola=plt.gca()
# ax.axes.get_xaxis().set_visible(False)
# ax.set_title('Comparacion')
# ax.set_ylabel("Tiempo /segundos")
# ax.set_xlabel('Distribution')
# show()
# files=[]
# for counter, filename in enumerate(os.listdir(path)):
#     file = pd.read_excel(("%s/%s" % (path,filename)))
#     files.append(file)

# df=DataFrame({'X':x,'Y':y} for x, y in enumerate(total))
# df.to_excel(("%s/%s" % (path,'promedio.xlsx')), sheet_name='sheet1', index=False)
