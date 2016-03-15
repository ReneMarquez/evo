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
                local.append(float(x[3]))
            #maximo=max(local)
            eval1.append(local)
            del local
        #lista2=[]
        #m1=max(eval1)
        #lista2.append(m1)
        l1=[]
        m1=[]
        for elemento in eval1:
            suma=sum(elemento)/float(len(elemento))
            minimo=min(elemento)
            m1.append(minimo)
            l1.append(suma)
        num=0
        promedio=sum(l1)/len(l1)
        #lista2.append(promedio)
        tiempo.append(promedio)
        total.append(min(m1))
    del lista2
        # if len(lista2) == 5:
        #     suma=sum(lista2)/float(len(lista2))
        #     total.append(suma)
        #     lista2.append(suma)
        #     max1.append(lista2)
        #     del eval1
        #     del lista2
        # else:
        #     pass
        #del eval1
    l=[]
print tiempo
df=DataFrame({'X':x,'Y':y} for x, y in enumerate(tiempo))
df['Z']=total
# df1=DataFrame({'Z':z} for z in total)
# df=df.append(df1,ignore_index=False,)
df.to_excel(("%s/%s" % (path,'promedio.xlsx')), sheet_name='sheet1', index=False)
