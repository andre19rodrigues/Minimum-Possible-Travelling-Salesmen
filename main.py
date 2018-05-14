import csv
import datetime
import random

import AlgGen as AG
import GenerateRandomLocations
import Salesmen as sm
import routes
import algGenSalesmen as AGSalesman


distances = []
citiestotal = 0
citinames = []
population = []
salesmenRoute = []
popsize = 100
nGenerations = 50
start_end_point = 'AA'
distancesDict = {}
DMsalesman = 100


def multiple_salesman():
    for i in range(0, popsize):
        alphabeticRoute = routes.genAlphabeticRoute(citiestotal, distances)
        aRoute = random.sample(alphabeticRoute, len(alphabeticRoute))
        # print('aroute   '+str(aRoute))
        salesmenRoute = []
        salesmenRoute = sm.addCitiestoSalesmen(citiestotal, salesmenRoute, citiestotal, DMsalesman, aRoute, distancesDict)

        for i in range(citiestotal, 0, -1):
            try:
                if (len(salesmenRoute[i]) == 1):
                    del (salesmenRoute[i])
            except:
                xyz = 0

        for i in range(0, len(salesmenRoute)):
            salesmenRoute[i].append(routes.getFitness(salesmenRoute[i], distancesDict))
            # print(str(salesmenRoute[i]) +' '+ str(routes.getFitness(salesmenRoute[i], distancesDict)))

        population.append(salesmenRoute)

    # print(population)

    pop = AGSalesman.evolvePopulation_multipleSalesman(population, distancesDict, DMsalesman)
    for i in range(1, nGenerations):
        # print(pop)
        print(i)
        pop = AGSalesman.evolvePopulation_multipleSalesman(pop, distancesDict, DMsalesman)

    print('\nInitial: ' + str(len(population[0])) + ' Salesmen  |  ' + str(
        routes.getTotalSalesmenDistance(population[0])) + ' Total distance')
    print('Optimal: ' + str(len(pop[0])) + ' Salesmen  |  ' + str(
        routes.getTotalSalesmenDistance(pop[0])) + ' Total distance')

if __name__ == '__main__':
    before = datetime.datetime.now()
    print(datetime.datetime.now() - before)

    # read data from file
    distancesDict, distances, citiestotal = GenerateRandomLocations.readdata()

    multiple_salesman()

    # classical SalesMan
    # routes.getOptimalTS1Salesman(start_end_point, citiestotal, distances, popsize, nGenerations, distancesDict)



