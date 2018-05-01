import csv
import random
from operator import itemgetter

import AlgGen as AG
import routes

distances = []
citiestotal = 0 # nª de alelos em cada cromossoma
citinames = []
population = []
distancesDict = {}
popsize = 100
nGenerations = 6
start_end_point = 'AA'

def readdata():

    global citiestotal

    with open('locations.csv', 'r') as csvfile:
        loc = csv.reader(csvfile)

        a = 65
        b = 65
        c = 65
        d = 65
        for row in loc:
            citiestotal = len(row)
            for i in range(0, citiestotal):
                city = [chr(a)+chr(b), chr(c)+chr(d), row[i]]
                distances.append(city)
                distancesDict[(chr(a)+chr(b), chr(c)+chr(d))] = row[i]
                if d is not 90:
                    d += 1
                else:
                    c += 1
                    d = 65

            c = 65
            d = 65
            if b is not 90:
                b += 1
            else:
                a += 1
                b = 65


readdata()
#print(distances)

alphabeticRoute = []
alphabeticRoute.append(start_end_point)# on the first position we append the start_end_point
for i in range(1, citiestotal):
    alphabeticRoute.append(distances[i][1])
alphabeticRoute.append(start_end_point)# on the last position we append the start_end_point

pop = AG.init_population(alphabeticRoute, citiestotal, distancesDict, popsize, start_end_point)
print(pop)
pop = AG.evolvePopulation(pop, distancesDict, citiestotal, True, popsize)
for i in range(1, nGenerations):
    print(pop)
    print(i)
    pop = AG.evolvePopulation(pop, distancesDict, citiestotal, False, popsize)



#print(pop[0])
#print(routes.getFitnessTotalPopulation(population, distances, citiestotal))