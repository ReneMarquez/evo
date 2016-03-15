__author__ = 'Rene'
import os
from pandas import DataFrame
from pandas import ExcelWriter

path="C:\Users\Rene\Desktop\experimentos-2/nuevosconfig\data-griewank-12work-besthomo"
param=[]
for counter, filename in enumerate(os.listdir(path)):
    w12_file = open("%s/%s" % (path,filename))
    parametros = [line.split(",") for counter, line in enumerate(w12_file) if counter == 1]
    param.append((parametros[0][12],parametros[0][13]))

tiempo=[]
total=[]
for counter, filename in enumerate(os.listdir(path)):
    w12_file = open("%s/%s" % (path,filename))
    w12_records = [line.split(",") for line in w12_file if len(line.split(",")) == 3]
    l=[]
    promedio=0
    for x in w12_records:
        promedio=promedio + float(x[1])
        l.append((counter,x[1],param[counter]))
        tiempo.append(x[1])
        # if len(l)==5:
        #     promedio=promedio/5
        #     print l,promedio
        #     total.append(promedio)
        #     tiempo.append(promedio)
        #     del l
        # else:
        #     pass

#writer = ExcelWriter(path)
# for n in len(total):
#     n = DataFrame({'ok':df1[n]} for n,df1 in enumerate(total))
# for n, df1 in enumerate(total):
#     df=DataFrame({'ok':df1[n]} for df1 in total)
#     #df1.to_excel(writer, 'sheet1')
# writer.save()

#x=list[range(1,len(total))]
df=DataFrame({'X':x,'Y':y} for x, y in enumerate(tiempo))
df.to_excel(("%s/%s" % (path,'promedio.xlsx')), sheet_name='sheet1', index=False)
