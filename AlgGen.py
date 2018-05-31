import random
from operator import itemgetter
import routes
crossoverProb = 0.5
mutationProb = 0.5


# the crossover here, takes two chromos
# then build a child
# the process of crossover is done by fill the child with the motherchromo when it is between the 2 random values
# if it isnt, go check the oposite and fill
#
# after this, the child isnt complete, so we grab on the fatherCromo and fill the missing child`s missing spaces with father cromo
def Crossover(motherCromo, fatherCromo, citiestotal):

    # a = random.randint(0, citiestotal-1)
    # b = random.randint(0, citiestotal-1)

    rands = random.sample(range(0, citiestotal-1), 2)
    a = rands[0]
    b = rands[1]
    rands.clear()

    if a > b:
        a, b = b, a

    child = []
    child.insert(0, motherCromo[0])
    for i in range(1, citiestotal):
        child.append(999999)

    child.append(motherCromo[citiestotal])



    for i in range(1, citiestotal):
        if (i > a and i < b):
            child[i] = motherCromo[i]
        elif i == b:
            break

    for i in range(1, citiestotal):
            for j in range(1, citiestotal):
                if (fatherCromo[i] not in child):
                    if (child[j] == 999999):
                        child[j] = fatherCromo[i]
                        break

    return child

# go on chromo and swaps to genes until the end
def randomMutation(cromo, citiesTotal, Pmutation):

    for i in range(1, citiesTotal-1):
        if random.random() < Pmutation:
            val = i
            while val == i:
                val = random.randint(1, citiesTotal - 2)
            cromo[i], cromo[val] = cromo[val], cromo[i]

    return cromo

# this method is based on roullete pick, so we have the probabilities of each indiviual, and then the propabilitie of one
# indivual being selected its equal to his fitness
def proporcionalSelection(population, prob_array, popsize):
    rand = random.random()
    i = 0
    s = prob_array[0]
    while s < rand:
        if (i + 1) == popsize:
            break
        i = i + 1
        s = s + prob_array[i]


    return population[i]

 # receives a population and return the best indivual
def elitism(population, citiesTotal):
    population.sort(key=itemgetter(citiesTotal + 1))
    return population[0]


def init_population(alphabeticRoute, citiestotal, distances, popsize, start_end_point):
    population = []
    for i in range(0, popsize):
        aRoute = random.sample(alphabeticRoute[1:citiestotal], citiestotal - 1)
        #print(aRoute)
        aRoute.insert(0, start_end_point)
        aRoute.append(start_end_point)
        a = routes.getFitness(aRoute, distances)
        save = aRoute
        save.append(a)
        population.append(save)
        del aRoute

    return population




# the best of the last generation, always goes to the new one,
# its also calculated the probability for each indivual to do the proporcional selection
# finally every new child is mutated
def evolvePopulation(population, distances, citiestotal, first, nGenerations):
    #calculate fitness for every indivual in population
    new_pop = []
    popsize = len(population)
    if not first:
        for i in range(1, popsize): # starts at 1 because the first one alredy comes with fitness
            fit = routes.getFitness(population[i], distances)
            population[i].append(fit)

    # only the best of each gen goes directly to next gen
    elit_cromo = elitism(population, citiestotal)
    new_pop.append(elit_cromo)

    sum_aptd = 0  # sum of all fitnesses
    prob_array = []  # array to store the probabilities
    for i in population:
        sum_aptd = sum_aptd + i[citiestotal + 1]

    for i in population:
        prob = i[citiestotal + 1] / sum_aptd
        prob_array.append(prob)


    for i in range(1, popsize):
            parent1 = proporcionalSelection(population, prob_array, popsize)
            parent2 = proporcionalSelection(population, prob_array, popsize)

            randCross = random.random()
            if randCross < crossoverProb:
                child = Crossover(parent1, parent2, citiestotal)
                new_pop.append(child)
            else:
                if randCross > 0.5:
                    newChild = parent1[:-1]
                    new_pop.append(newChild)
                else:
                    newChild = parent2[:-1]
                    new_pop.append(newChild)

    global mutationProb

    if(i > int(nGenerations*0.3) and i <= int(nGenerations*0.5)):
        mutationProb = 0.4
    elif(i > int(nGenerations*0.5) and i <= int(nGenerations*0.7)):
        mutationProb = 0.3
    elif (i > int(nGenerations * 0.7) and i <= int(nGenerations * 0.9)):
        mutationProb = 0.2
    elif (i > int(nGenerations * 0.9)):
        mutationProb = 0.1

    for i in range(1, len(new_pop)):
        cromoMutation = randomMutation(new_pop[i], citiestotal, mutationProb)
        new_pop[i] = cromoMutation

    return new_pop

