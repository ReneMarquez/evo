__author__ = 'Rene'
import redis
import itertools
import math
from collections import Counter
from scipy.spatial import distance
import matplotlib.pyplot as plt
from pylab import *

HOST="52.0.98.203"
PORT=6379

r = redis.Redis(host=HOST, port=PORT)
fig,ax = plt.subplots()
pop=[]
for log in range(30):
    set1 = r.smembers("log:" + str(log*10))
    if len(set1)==0:
        pass
    else:
        pop.append(set1)

#key=r.keys("log:10")
fit_list=[]
cromosomas=[]
poblist=[]
for a in pop:
    pob=r.mget(a)
    poblist.append(pob)
    set_list1=[]
    crom=[]
    for ind1 in pob:
        if ind1==None:
            pass
        else:
            fitness1 = ind1.split(":")
            hello=fitness1[6].split("[")
            h1=hello[1].split("]")
            h2=h1[0].split(',')
            crom.append([float(i) for i in h2])
        # mm1=fitness1[2].split("}")
        # set_list1.append(float(mm1[0]))
    # fit_list.append(set_list1)
    cromosomas.append(crom)
    del crom
    #del set_list1

#     del set_list1

# fit_list=[]
# for s in pop:
#     set_list=[]
#     for individual in s:
#         ind = r.get(individual)
#         fitness = ind.split(":")
#         mm=fitness[2].split("}")
#         set_list.append(float(mm[0]))
#     fit_list.append(set_list)
#     del set_list
def hamming_distance(s1, s2):
    #Return the Hamming distance between equal-length sequences
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

def diversity(pop):
    return sum([hamming_distance(ind1,ind2) for ind1,ind2 in itertools.combinations(pop,2)])

lista=[]
def euclidiana(s1,s2):
    dist=distance.euclidean(s1,s2)
    lista.append(dist)
    return dist

def eucl_pop(pop):
    return sum([euclidiana(ind1,ind2) for ind1,ind2 in itertools.combinations(pop,2)])

fit_list
# distancia=[]
# for poblacion in cromosomas:
#     distancia.append(diversity(poblacion))

dist_euclidiana=[]
generaciones=[]
no_workers=6
gen=0
#dist_euclidiana.append(eucl_pop(cromosomas[0]))
for cont, pobl in enumerate(cromosomas):
    gen=gen + 100*no_workers
    if not pobl:
        pass
    else:
        generaciones.append(gen)
        dist_euclidiana.append(eucl_pop(pobl))
# pop2=cromosomas[0]
# div=diversity(pop2)

ax.set_title('Distancia euclidiana/poblaciones durante evolucion')
ax.set_ylabel("Distancia Euclidiana")
ax.set_xlabel('Generaciones Totales')

ax.plot(generaciones,dist_euclidiana)
plt.scatter(generaciones,dist_euclidiana)
start, end = ax.get_ylim()
#ax.yaxis.set_ticks(np.arange(start, end, 1000000))
plt.axis([0,30000,0,end])
plt.show()
print dist_euclidiana