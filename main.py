import csv
import random
from operator import itemgetter

import AlgGen as AG
import routes

distances = []
citiestotal = 0
citinames = []
population = []
popsize = 10
nGenerations = 30

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
for i in range(0, citiestotal):
    alphabeticRoute.append(distances[i][1])

pop = AG.init_population(alphabeticRoute, citiestotal, distances, popsize)
print(pop)
pop = AG.evolvePopulation(pop, distances, citiestotal, True)
for i in range(1, nGenerations):
    print(pop)
    print(i)
    pop = AG.evolvePopulation(pop, distances, citiestotal, False)



print(pop[0])
#print(routes.getFitnessTotalPopulation(population, distances, citiestotal))