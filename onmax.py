__author__ = 'Rene'

__author__ = 'PC'

import random
import time
import array
import simplejson
from random import randrange
from deap import base
from deap import creator
from deap import tools
from deap import benchmarks
import jsonrpclib
from celery import Celery

app = Celery('onmax', backend='redis://localhost', broker='redis://localhost')

app.conf.CELERY_TASK_SERIALIZER = 'json'
app.conf.CELERY_RESULT_SERIALIZER = 'json'
app.conf.CELERY_ACCEPT_CONTENT = ['json','yaml']
app.conf.CELERY_RESULT_BACKEND = 'redis'
app.conf.CELERY_IGNORE_RESULT = False

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)
#creator.create("Individual", array.array, typecode='d', fitness=creator.FitnessMin)

def esfera(individual):
    return sum(individual),


def ToolBox(config):
    toolbox = base.Toolbox()
    toolbox.register("attr_bool", random.randint, 0, 1)
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, config["CHROMOSOME_LENGTH"])
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("select", tools.selTournament, tournsize=3)
    toolbox.register("evaluate", esfera)
    return toolbox

@app.task(ignore_result=False)
def initialize(config):
    pop = ToolBox(config).population(n=config["POPULATION_SIZE"])
    server = jsonrpclib.Server(config["SERVER"])
    server.initialize(None)

    sample = [{"chromosome":ind[:], "id":None, "fitness":{"DefaultContext":0.0}} for ind in pop]
    init_pop = {'sample_id': 'None' , 'sample':   sample}

    server.putSample(init_pop)


def get_sample(config):
    for attempts in range(3):
        try:
            server = jsonrpclib.Server(config["SERVER"])
            sample = server.getSample(config["SAMPLE_SIZE"])
            return sample
        except jsonrpclib.ProtocolError as err:
            print "Error %s" % err

def put_sample(config,sample):
    for attempts in range(3):
        try:
            server = jsonrpclib.Server(config["SERVER"])
            server.putSample(sample)
            break
        except jsonrpclib.ProtocolError as err:
            print "Error %s" % err

@app.task
def evolve(sample_num, config):
    #random.seed(64)

    toolbox = ToolBox(config)

    start= time.time()
    evospace_sample = get_sample(config)
    tGetSample= time.time()-start

    startEvol = time.time()
    pop = [ creator.Individual( cs['chromosome']) for cs in evospace_sample['sample']]

    # Evaluate the entire population
    fitnesses = map(toolbox.evaluate, pop)
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit
    sample_id = evospace_sample['sample_id']

    total_evals = len(pop)
    best_first   = None
    best_individual = None
    # Begin the evolution

    for g in range(config["WORKER_GENERATIONS"]):
        print("-- Generation %i --" % g)
        if best_individual:
            pop[0] = best_individual
        # Select the next generation individuals
        offspring = toolbox.select(pop, len(pop))
        # Clone the selected individuals
        offspring = map(toolbox.clone, offspring)

        # Apply crossover and mutation on the offspring
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < config["CXPB"]:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:
            if random.random() < config["MUTPB"]:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        # Evaluate the individuals with an invalid fitness
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        total_evals+=len(invalid_ind)
        #print "  Evaluated %i individuals" % len(invalid_ind),

        # The population is entirely replaced by the offspring
        pop[:] = offspring

        # Gather all the fitnesses in one list and print the stats
        fits = [ind.fitness.values[0] for ind in pop]

        #length = len(pop)


        #mean = sum(fits) / length
        #sum2 = sum(x*x for x in fits)
        #std = abs(sum2 / length - mean**2)**0.5

        best = max(fits)
        if not best_first:
            best_first = best

        best_individual = tools.selBest(pop, 1)[0]
        if best ==  config["CHROMOSOME_LENGTH"]:
            #print best_individual
            break
        #
        #
        #     #print  "  Min %s" % min(fits) + "  Max %s" % max(fits)+ "  Avg %s" % mean + "  Std %s" % std

    #print "-- End of (successful) evolution --"
        print("  Min %s" % min(fits))
        print("  Max %s" % max(fits))


    sample = [ {"chromosome":ind[:],"id":None,
                "fitness":{"DefaultContext":ind.fitness.values[0]} }
               for ind in pop]
    evospace_sample['sample'] = sample
    tEvol = time.time()-startEvol


    startPutback =  time.time()
    if random.random() < config["RETURN_RATE"]:
        put_sample(config, evospace_sample)
        was_returned= "RETURNED"
    else:
         was_returned= "LOST"
    tPutBack = time.time() - startPutback

    return best ==  config["CHROMOSOME_LENGTH"], \
           [config["CHROMOSOME_LENGTH"],best, sample_num, round(time.time() - start, 2),
            round(tGetSample,2) , round( tEvol,2), round(tPutBack, 2), total_evals, best_first,was_returned,
             config["MUTPB"], config["CXPB"], config["SAMPLE_SIZE"],config["WORKER_GENERATIONS"],sample_id]

@app.task(ignore_result=False)
def work(params):
    worker_id = params[0]
    config = params[1]
    results = []
    for sample_num in range(config["MAX_SAMPLES"]):
        server = jsonrpclib.Server(config["SERVER"]) #Create every time to prevent timeouts
        if int(server.found(None)):
            break
        else:
            gen_data = evolve(sample_num, config)
            if gen_data[0]:
                server.found_it(None)
                print "FOUND"
            results.append([worker_id] + gen_data[1])
            #print [worker_id] + gen_data[1]
    return results


def main():
    #random.seed(64)
    # nopop=range(10,200,20)
    # nopop=nopop[randrange(len(nopop))]
    # pop = toolbox.population(nopop[randrange(len(nopop))])
    nopop=random.randint(10,299)
    pop=toolbox.population(nopop)
    CXPB=round(random.uniform(0,1),1)
    # CXPB=CXPB[randrange(len(CXPB))]
    MUTPB=round(random.uniform(0,1),1)
    NGEN = 500

    print("Start of evolution")

    # Evaluate the entire population
    fitnesses = list(map(toolbox.evaluate, pop))
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit

    print("  Evaluated %i individuals" % len(pop))

    # Begin the evolution
    start = time.time()
    minval=[]
    maxval=[]
    config=[]
    for i in range(10):
        for g in range(NGEN):
            print("-- Generation %i --" % g)

        # Select the next generation individuals
            offspring = toolbox.select(pop, len(pop))
        # Clone the selected individuals
            offspring = list(map(toolbox.clone, offspring))

        # Apply crossover and mutation on the offspring
            for child1, child2 in zip(offspring[::2], offspring[1::2]):
                if random.random() < CXPB:
                    toolbox.mate(child1, child2)
                    del child1.fitness.values
                    del child2.fitness.values

            for mutant in offspring:
                if random.random() < MUTPB:
                    toolbox.mutate(mutant)
                    del mutant.fitness.values

        # Evaluate the individuals with an invalid fitness
            invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
            fitnesses = map(toolbox.evaluate, invalid_ind)
            for ind, fit in zip(invalid_ind, fitnesses):
                ind.fitness.values = fit

            print("  Evaluated %i individuals" % len(invalid_ind))

        # The population is entirely replaced by the offspring
            pop[:] = offspring

        # Gather all the fitnesses in one list and print the stats
            fits = [ind.fitness.values[0] for ind in pop]

            length = len(pop)
            mean = sum(fits) / length
            sum2 = sum(x*x for x in fits)
            std = abs(sum2 / length - mean**2)**0.5

            print("  Min %s" % min(fits))
            print("  Max %s" % max(fits))
            print("  Avg %s" % mean)
            print("  Std %s" % std)


            minval.append([min(fits),tools.selWorst(pop,1)])
            maxval.append([max(fits),tools.selBest(pop,1)[0]])

            if max(fits) == 128:
                print "Total:", time.time()-start
                print tools.selBest(pop, 1)[0]
                return


            if min(fits) == 0:
                config.append([CXPB, MUTPB, nopop, time.time()-start])
                break
        pop=[]

    print("-- End of (successful) evolution --")
    print "Total:", time.time()-start
    best_ind = tools.selBest(pop, 1)[0]
    print("Best individual is %s, %s" % (best_ind, best_ind.fitness.values))
    print min(minval)
    # config=[CXPB,MUTPB,time.time()-start]
    # f=open("config"+str(nopop)+".txt",'w')
    f=open("config13.txt",'w')
    # for el in range(len(config)):
    #     simplejson.dump(config[el],f)
    #     simplejson.dump('/n' ,f)
    # f.close()
    for el in config:
        f.write("%s\n" % el)


if __name__ == "__main__":
    pass