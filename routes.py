import AlgGen as AG

def getFitness(chromo, distancesDict):

    sum = 0
    cromolen = len(chromo)

    for j in range(0, cromolen - 2):
        s = (chromo[j], chromo[j + 1])
        val = distancesDict[s]
        sum = sum + int(val)

    return sum

#generates a route using the alphabetic order of the city names
def genAlphabeticRoute(citiestotal, distances):

    alphabeticRoute = []
    for i in range(1, citiestotal):
        l = [distances[i][1], 0]
        alphabeticRoute.append(l)

    return alphabeticRoute


#optimal route for normal TS, so using only one salesman
def getOptimalTS1Salesman(start_end_point, citiestotal, distances, popsize, nGenerations, distancesDict):
    alphabeticRoute = []
    alphabeticRoute.append(start_end_point)  # on the first position we append the start_end_point

    for i in range(1, citiestotal):
        alphabeticRoute.append(distances[i][1])
    alphabeticRoute.append(start_end_point)  # on the last position we append the start_end_point

    pop = AG.init_population(alphabeticRoute, citiestotal, distancesDict, popsize, start_end_point)
    #print(pop)
    pop = AG.evolvePopulation(pop, distancesDict, citiestotal, True, nGenerations)
    for i in range(1, nGenerations):
        #print(pop)
        print(i)
        pop = AG.evolvePopulation(pop, distancesDict, citiestotal, False, nGenerations)

    print(pop[0])


def getTotalSalesmenDistance(population):

    sum = 0
    for i in range(0, len(population)):
        sum = sum + int(population[i][-1])

    return sum

def checkAllcities(population, cities):

    for i in range(0, len(cities)):
        if cities[i] in population:
            val = True
        if val == False:
            return False
        else:
            val = False