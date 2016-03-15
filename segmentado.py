__author__ = 'Rene'

from one_max import initialize, work
import time, yaml
import random


config = yaml.load(open("EvoPar2015/code/conf/conf.yaml"))
experiment = "w%d-%d-p%d" % (dict["NUMBER_OF_WORKERS"], dict["RETURN_RATE"]*100,dict["POPULATION_SIZE"])
experiment_id = experiment + "-%d" % round(time.time(),0)
dic=[]
cruce=0.5/(config["NUMBER_OF_WORKERS"]-1)
mutacion=0.1/(config["NUMBER_OF_WORKERS"]-1)
cx=0.5
mb=0.0
for i in range(dict["NUMBER_OF_WORKERS"]):
        dict1={'NUMBER_OF_WORKERS':config['NUMBER_OF_WORKERS'],'SAMPLE_SIZE':config["SAMPLE_SIZE"],'POPULATION_SIZE':config["POPULATION_SIZE"],'SERVER': 'http://54.164.20.127:5000/evospace','WORKER_TYPE': 'c1','CHROMOSOME_LENGTH': config["CHROMOSOME_LENGTH"],'PEAKS': 512,'WORKER_GENERATIONS': config["WORKER_GENERATIONS"],'MAX_SAMPLES': config["MAX_SAMPLES"],'MUTATION_FLIP_PB': .05,'TOURNAMENT_SIZE': 4,'CXPB':round(cx,3), 'MUTPB':round(mb,3),'RETURN_RATE': 1.00}
        dic.append(dict1)
        cx=cx+cruce
        mb=mb+mutacion

datafile = open("EvoPar2015/code/data/one_max-segmentado"+experiment_id+".dat","a")
conf_out = open("EvoPar2015/code/conf/one_max-segmentado"+experiment_id+".yaml","w")
yaml.dump(config, conf_out)
conf_out.close()

for i in range(config["NUM_EXP"]):
    start = time.time()

    init_job = initialize.delay(config=config)
    while not init_job.ready():
        time.sleep(2)
        print "waiting to initialize"
    print "EvoSpace Initialized"

    tInitialize = time.time()-start
    print i, tInitialize

    params = [(w, dic[w]) for w in range(dict["NUMBER_OF_WORKERS"])]

    jids = map(work.delay, params)
    results_list = []
    while jids:
        #time.sleep(1)
        print "Working"
        for job in jids:
            if job.ready():
                if job.status == 'FAILURE':
                    print job.traceback
                #time.sleep(2)
                r = job.get()
                #print r
                results_list.append(r)
                jids.remove(job)
    #print min(results_list)

    tTotal = time.time()-start
    totals = "%d,%0.2f,%0.2f" % (i, round(tTotal,2), round(tInitialize,2))
    print totals
    datafile.write(totals + '\n')
    for worker_list in results_list:
        for data_list in worker_list:
            datafile.write(str(i) +"," + ",".join(map(str,data_list)) + '\n')