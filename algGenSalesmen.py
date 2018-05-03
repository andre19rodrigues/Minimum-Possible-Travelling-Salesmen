import random
import routes
mutationProb = 0.2

def Crossover(cromo, sizeCromo, distanceDict, maxKM):
    # select two random cromo from cromo array
    rand = random.randint(0, (sizeCromo - 2))
    val = rand
    while val == rand:
        val = random.randint(0, sizeCromo - 2)

    # position selected to add to new cromo
    cromoPos = random.randrange(1, (len(cromo[rand]) - 2))


    cromoRemove = [None] * len(cromo[rand])
    for i in range(0, len(cromo[rand])):
        cromoRemove[i] = cromo[rand][i]
    value = cromoRemove.pop(cromoPos)

    cromoADD = [None] * len(cromo[val])
    for i in range(0, len(cromo[val])):
        cromoADD[i] = cromo[val][i]

    cromoADD.insert(len(cromoADD) - 2, value)

    min = []
    min2 = []
    if len(cromoRemove) == 3: # when the size of the cromoRemove is 3 [AA, AA, 123],
        minMax2 = 99999
        if routes.getFitness(cromoADD[:len(cromoADD)-1], distanceDict) > maxKM:
            for i in range(0, 100):
                r = randomMutation(cromoADD)
                fit = routes.getFitness(r[:len(r)-1], distanceDict)
                if fit < maxKM and fit < minMax2:
                    minMax2 = fit
                    r[len(r) - 1] = fit
                    min2 = r

            if minMax2 > maxKM:
                return cromo
            else:
                cromo[val] = min2
                cromo.pop(rand)
                return cromo
        else:
            fit = routes.getFitness(cromoADD[:len(cromoADD)-1], distanceDict)
            cromoADD[len(cromoADD)-1] = fit
            cromo[val] = cromoADD
            cromo.pop(rand)
            return cromo

    else:
        minMax = 99999
        if routes.getFitness(cromoRemove[:len(cromoRemove)-1], distanceDict) > maxKM:
            for i in range(0, 100):
                r = randomMutation(cromoRemove)
                fit = routes.getFitness(r[:len(r)-1], distanceDict)
                if fit < maxKM and fit < minMax:
                    minMax = fit
                    r[len(r)-1] = fit
                    min = r
            if minMax > maxKM:
                return cromo

            else:
                minMax2 = 99999
                if routes.getFitness(cromoADD[:len(cromoADD)-1], distanceDict) > maxKM:
                    for i in range(0, 100):
                        r = randomMutation(cromoADD)
                        fit = routes.getFitness(r[:len(r)-1], distanceDict)
                        if fit < maxKM and fit < minMax:
                            minMax2 = fit
                            r[len(r)-1] = fit
                            min2 = r

                    if minMax2 > maxKM:
                        return cromo
                    else:
                        cromo[rand] = min
                        cromo[val] = min2
                        return cromo
                else:
                    fit = routes.getFitness(cromoRemove[:len(cromoRemove) - 1], distanceDict)
                    cromoRemove[len(cromoRemove) - 1] = fit
                    cromo[rand] = cromoRemove
                    fit = routes.getFitness(cromoADD[:len(min2) - 1], distanceDict)
                    cromoADD[len(cromoADD) - 1] = fit
                    cromo[val] = cromoADD
                    return cromo

        else:
            minMax = 99999
            if routes.getFitness(cromoADD[:len(cromoADD)-1], distanceDict) > maxKM:
                for i in range(0, 100):
                    r = randomMutation(cromoADD)
                    fit = routes.getFitness(r[:len(r) - 1], distanceDict)
                    if fit < maxKM and fit < minMax:
                        minMax = fit
                        r[len(r) - 1] = fit
                        min2 = r
                if minMax > maxKM:
                    return cromo
                else:
                    fit = routes.getFitness(min2[:len(min2)-1], distanceDict)
                    min2[len(min2)-1] = fit
                    cromo[val] = min2
                    cromo[rand] = cromoRemove
                    return cromo
            else:
                fit = routes.getFitness(cromoRemove[:len(cromoRemove) - 1], distanceDict)
                cromoRemove[len(cromoRemove) - 1] = fit
                cromo[rand] = cromoRemove
                fit = routes.getFitness(cromoADD[:len(min2) - 1], distanceDict)
                cromoADD[len(cromoADD) - 1] = fit
                cromo[val] = cromoADD
                return cromo

def randomMutation(cromo):
    lcromo = len(cromo)

    for i in range(1, lcromo-3):
        if random.random() < mutationProb:
            val = i
            while val == i:
                val = random.randint(1, lcromo - 3)
            cromo[i], cromo[val] = cromo[val], cromo[i]

    return cromo


def evolvePopulation_multipleSalesman(population, distancesDict, maxKM):
    #calculate fitness for every indivual in population
    new_pop = []
    popsize = len(population)
    # if not first:
    #     for i in range(1, popsize): # starts at 1 because the first one alredy comes with fitness
    #         sizeSalesman = len(population[i])
    #         for j in range(0, sizeSalesman):
    #             fit = routes.getFitness(population[i][j], distancesDict)
    #             population[i][j].append(fit)

    #only the best of each gen goes directly to next gen
    elit_cromo = (elitism_multipleSalesman(population, popsize))
    new_pop.append(elit_cromo)


    for i in range(1, popsize):
        crossoverProb = 0.3
        if random.random() <= crossoverProb:
            sizeCromo = len(population[i])
            if sizeCromo is not 1:
                child = Crossover(population[i], sizeCromo, distancesDict, maxKM)

                new_pop.append(child)
            else:
                new_pop.append(population[i])
        else:
            new_pop.append(population[i])

    for i in range(1, len(new_pop)):
        cromoMutation = randomMutation(new_pop[i])
        new_pop[i] = cromoMutation

    return new_pop

def elitism_multipleSalesman(population, popsize):
    bestSize = len(population[0])
    bestIndividual = population[0]
    sumBestFitness = 0
    for i in bestIndividual:
        s = len(i)
        sumBestFitness = sumBestFitness + i[s-1]

    for i in range(1, popsize):
        sizeSalesman = len(population[i])
        if sizeSalesman < bestSize:
            bestSize = sizeSalesman
            bestIndividual = population[i]
            sumBest = 0
            for j in bestIndividual:
                sumBest = sumBest + j[len(j) - 1]
            sumBestFitness = sumBest

        elif sizeSalesman == bestSize:
            # when an indivual has the same size, also ist need to calculate the sum of
            # all fitness and store the one that has less
            sumPossBest = 0
            for j in population[i]:
                sumPossBest = sumPossBest + j[len(j) - 1]

            if sumPossBest < sumBestFitness:
                bestSize = sizeSalesman
                bestIndividual = population[i]
                sumBestFitness = sumPossBest

    return bestIndividual