import random
import routes

# This algorithm consists in:
#   --> firstly, select randomly two salesman from the set of all salesman in one chromossome
#   --> secondly, remove one city from the first selected salesman and inserts it in the other salesman selected.
#
#   --> If the salesmen from which a city has been removed have after a higher distance to travel, then mutations are
#       made and the smaller fitness of them is kept. If the lower fitness is less than the maximum distance allowes
#       then we skip to the next case.
#       If the salesman in which a city was inserted have a greater distance to travel after the insertion, then
#       mutations are made and the smallest fitness is kept. If the lower fitness is less than the maximum distance
#       allowed then the crossover was successful.
#
#       The number of mutations made is given by the probability of mutation * 100 * size of salesman route

def Crossover(chromo, sizeCromo, distanceDict, maxKM, mutationProb):
    # select two random chroms from chromo array
    rand = random.randint(0, (sizeCromo - 2))
    val = rand

    if sizeCromo == 2:
        val = 1
    else:
        while val == rand:
            val = random.randint(0, sizeCromo - 2)

    # position selected to add to new chromo
    cromoPos = random.randrange(1, (len(chromo[rand]) - 2))


    cromoRemove = [None] * len(chromo[rand])
    for i in range(0, len(chromo[rand])):
        cromoRemove[i] = chromo[rand][i]
    value = cromoRemove.pop(cromoPos)

    cromoADD = [None] * len(chromo[val])
    for i in range(0, len(chromo[val])):
        cromoADD[i] = chromo[val][i]

    cromoADD.insert(len(cromoADD) - 2, value)

    min = []
    min2 = []
    if len(cromoRemove) == 3: # when the size of the cromoRemove is 3 [AA, AA, 123],
        minMax2 = 99999
        if routes.getFitness(cromoADD[:len(cromoADD)-1], distanceDict) > maxKM:
            for i in range(0, int(mutationProb*100*len(cromoADD))):
                r = randomMutation(cromoADD, mutationProb)
                fit = routes.getFitness(r[:len(r)-1], distanceDict)
                if ((fit <= maxKM) and (fit < minMax2)):
                    minMax2 = fit
                    r[len(r) - 1] = fit
                    min2 = r[:]

            if minMax2 > maxKM:
                return chromo
            else:
                chromo[val] = min2
                chromo.pop(rand)
                return chromo
        else:
            fit = routes.getFitness(cromoADD[:len(cromoADD)-1], distanceDict)
            cromoADD[len(cromoADD)-1] = fit
            chromo[val] = cromoADD
            chromo.pop(rand)
            return chromo

    # CromoRemove size > 3
    else:
        minMax = 99999
        # If the the fitness from the salesman that we removed the city is greater than the max of km possible, then do mutation
        if routes.getFitness(cromoRemove[:len(cromoRemove)-1], distanceDict) > maxKM:
            for i in range(0, int(mutationProb*100*len(cromoRemove))):
                r = randomMutation(cromoRemove, mutationProb)
                fit = routes.getFitness(r[:len(r)-1], distanceDict)
                if ((fit <= maxKM) and (fit < minMax)):
                    minMax = fit
                    r[len(r)-1] = fit
                    min = r[:]
            # if after the mutation it wasnt possible to make the fitness lesser than the maximum possible distance
            # return the chromo untouched
            if minMax > maxKM:
                return chromo

            else:
                minMax2 = 99999
                # if the remotion was possible and the fitness of the other salesman is greather than the max KM do mutation
                if routes.getFitness(cromoADD[:len(cromoADD)-1], distanceDict) > maxKM:
                    for i in range(0, int(mutationProb*100*len(cromoRemove))):
                        r = randomMutation(cromoADD, mutationProb)
                        fit = routes.getFitness(r[:len(r)-1], distanceDict)
                        if ((fit <= maxKM) and (fit < minMax2)):
                            minMax2 = fit
                            r[len(r)-1] = fit
                            min2 = r[:]

                    if minMax2 > maxKM:
                        return chromo
                    else:
                        chromo[rand] = min
                        chromo[val] = min2
                        return chromo
                # if the fitness is less or eq to the max KM, calculate fitness and return chromo with new salesman
                else:
                    fit = routes.getFitness(min[:len(min) - 1], distanceDict)
                    min[len(min) - 1] = fit
                    chromo[rand] = min
                    fit = routes.getFitness(cromoADD[:len(cromoADD) - 1], distanceDict)
                    cromoADD[len(cromoADD) - 1] = fit
                    chromo[val] = cromoADD
                    return chromo
        #this happens when the fitness from the removed salesman is lesser than the max KM
        # so we just calculate the fitness to new added salesman
        else:
            minMax = 99999
            if routes.getFitness(cromoADD[:len(cromoADD)-1], distanceDict) > maxKM:
                for i in range(0, int(mutationProb*100*len(cromoRemove))):
                    r = randomMutation(cromoADD, mutationProb)
                    fit = routes.getFitness(r[:len(r) - 1], distanceDict)
                    if ((fit <= maxKM) and (fit < minMax)):
                        minMax = fit
                        r[len(r) - 1] = fit
                        min2 = r[:]
                # if the mutation couldnt reduce the fitness, return chromo unchanged
                if minMax > maxKM:
                    return chromo
                # if mutation was successful return updated chromo
                else:
                    fit = routes.getFitness(min2[:len(min2)-1], distanceDict)
                    min2[len(min2)-1] = fit
                    chromo[val] = min2
                    chromo[rand] = cromoRemove
                    return chromo
            # if the removed and added salesmen already have less than max KM
            else:
                fit = routes.getFitness(cromoRemove[:len(cromoRemove) - 1], distanceDict)
                cromoRemove[len(cromoRemove) - 1] = fit
                chromo[rand] = cromoRemove
                fit = routes.getFitness(cromoADD[:len(cromoADD) - 1], distanceDict)
                cromoADD[len(cromoADD) - 1] = fit
                chromo[val] = cromoADD
                return chromo


def randomMutation(chromo, mutationProb):
    lcromo = len(chromo)

    for i in range(1, lcromo-3):
        if random.random() < mutationProb:
            val = i
            while val == i:
                val = random.randint(1, lcromo - 3)
            chromo[i], chromo[val] = chromo[val], chromo[i]

    return chromo


def evolvePopulation_multipleSalesman(population, distancesDict, maxKM, mutationProb, crossoverProb):

    #calculate fitness for every indivual in population
    new_pop = []
    popsize = len(population)

    #only the best of each generation goes directly to next generation
    elit_cromo = (elitism_multipleSalesman(population, popsize))
    new_pop.append(elit_cromo)


    for i in range(1, popsize):
        if random.random() <= crossoverProb:
            sizeCromo = len(population[i])
            if sizeCromo is not 1:
                child = Crossover(population[i], sizeCromo, distancesDict, maxKM, mutationProb)

                new_pop.append(child)
            else:
                new_pop.append(population[i])
        else:
            new_pop.append(population[i])

    return new_pop

def elitism_multipleSalesman(population, popsize):
    bestSize = len(population[0]) # chromo size
    bestIndividual = population[0][:] # best set of salesman
    sumBestFitness = 0 # sum of all salesman fitness in one set
    for i in bestIndividual:
        s = len(i)
        sumBestFitness = sumBestFitness + i[s-1]

    for i in range(1, popsize):
        sizeSalesman = len(population[i])
        if sizeSalesman < bestSize:
            bestSize = sizeSalesman
            bestIndividual = population[i][:]
            sumBest = 0
            for j in bestIndividual:
                sumBest = sumBest + j[len(j) - 1]
            sumBestFitness = sumBest

        elif sizeSalesman == bestSize:
            # when an individual has the same size, also its needed to calculate the sum of
            # all fitness and store the one that has less
            sumPossBest = 0
            for j in population[i]:
                sumPossBest = sumPossBest + j[len(j) - 1]

            if sumPossBest < sumBestFitness:
                bestSize = sizeSalesman
                bestIndividual = population[i][:]
                sumBestFitness = sumPossBest

    return bestIndividual