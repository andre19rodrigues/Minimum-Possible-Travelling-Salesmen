import AlgGen as AG

def getFitness(cromo, distancesDict):


    sum = 0
    cromolen = len(cromo)

    for j in range(0, cromolen - 1):
        s = (cromo[j], cromo[j + 1])
        val = distancesDict[s]
        sum = sum + int(val)

    return sum

 # for k in range(0, distancesSIZE):
 #            if j + 1 < cromolen:
 #                if distances[k][0] == cromo[j] and distances[k][1] == cromo[j+1]:
 #                    sum = sum + int(distances[k][2])
 #                    break
 #            else:
 #                break


def genAlphabeticRoute(citiestotal, distances):
    # alphabeticRoute.append(start_end_point)# on the first position we append the start_end_point

    alphabeticRoute = []
    for i in range(1, citiestotal):
        l = [distances[i][1], 0]
        alphabeticRoute.append(l)
    # alphabeticRoute.append(start_end_point)# on the last position we append the start_end_point

    return alphabeticRoute


def getOptimalTS1Salesman(start_end_point, citiestotal, distances, popsize, nGenerations, distancesDict):
    alphabeticRoute = []
    alphabeticRoute.append(start_end_point)  # on the first position we append the start_end_point

    for i in range(1, citiestotal):
        alphabeticRoute.append(distances[i][1])
    alphabeticRoute.append(start_end_point)  # on the last position we append the start_end_point

    pop = AG.init_population(alphabeticRoute, citiestotal, distancesDict, popsize, start_end_point)
    print(pop)
    pop = AG.evolvePopulation(pop, distancesDict, citiestotal, True)
    print(pop)
    for i in range(0, nGenerations):
        print(i)
        print(pop)
        pop = AG.evolvePopulation(pop, distancesDict, citiestotal, False)