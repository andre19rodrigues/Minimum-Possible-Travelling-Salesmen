import random
from operator import itemgetter
import routes
crossoverProb = 0.5
mutationProb = 0.2

def uniformCrossover(motherCromo, fatherCromo, citiestotal):

    a = random.randint(0, citiestotal-1)
    b = random.randint(0, citiestotal-1)

    child = []
    for i in range(0, citiestotal):
        child.append(999999)

    for i in range(0, citiestotal):
        if (a < b and i > a and i < b):
            child[i] = motherCromo[i]

        elif (a > b and not (i < a and i > b)):
            child[i] = motherCromo[i]


    for i in range(0, citiestotal):
            for j in range(0, citiestotal):
        if (fatherCromo[i] not in child):
                if (child[j] == 999999):
                    child[j] = fatherCromo[i]
                    break

    return child

def randomMutation(cromo, citiesTotal):
    for i in range(0, citiesTotal):
        if random.random() < mutationProb:
            val = i
            while val == i:
                val = random.randint(0, citiesTotal - 1)
                # val = random.randrange(0, cromo_size-1, i)
            cromo[i], cromo[val] = cromo[val], cromo[i]

    return cromo


def proporcionalSelection(population, citiestotal):
    sum_aptd = 0 # sum of all fitnesses
    prob_array = [] # array to store the probabilities
    for i in population:
        sum_aptd = sum_aptd + i[10]

    for i in population:
        prob = i[citiestotal] / sum_aptd
        prob_array.append(prob)

    # roullete pick
    rand = random.random()
    i = 0

    s = prob_array[0]
    while s < rand:
        i = i + 1
        s = s + prob_array[i]

    return population[i]

 # receives a population and the number of individuals to select
 # returns k selected
def elitism(population, citiesTotal):
    population.sort(key=itemgetter(citiesTotal))
    return population[0]

def init_population(alphabeticRoute, citiestotal, distances, popsize):
    population = []
    for i in range(0, popsize):
        aRoute = random.sample(alphabeticRoute, citiestotal)
        a = routes.getFitness(aRoute, distances, citiestotal)
        save = aRoute
        save.append(a)
        population.append(save)
        del aRoute
    
    return population

def evolvePopulation(population, distances, citiestotal, first):
    #calculate fitness for every indivual in population
    new_pop = []
    popsize = len(population)
    if not first:
        for i in range(0, popsize):
            fit = routes.getFitness(population[i], distances, citiestotal)
            if len(population[i])  is not 11:
                population[i].append(fit)
            else:
                population[i][10] = fit

    elit = 1 # only the best of each gen goes directly to next gen
    elit_cromo = elitism(population, citiestotal)
    new_pop.append(elit_cromo)


    for i in range(1, popsize):
        parent1 = proporcionalSelection(population, citiestotal)
        parent2 = proporcionalSelection(population, citiestotal)
        
        child1, child2 = uniformCrossover(parent1, parent2)
        new_pop.append(child1)


    for i in range(0, len(new_pop)):
        cromoMutation = randomMutation(new_pop[i], citiestotal)
        new_pop[i] = cromoMutation



    return new_pop
        










