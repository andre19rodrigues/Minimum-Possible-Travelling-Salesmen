import csv
import datetime
import random

import AlgGen as AG
import Salesmen as sm
import routes
import algGenSalesmen as AGSalesman
import networkx as nx
import matplotlib.pyplot as plt
import Colors

distances = []
citiestotal = 0
citinames = []
population = []
salesmenRoute = []
popsize = 100
nGenerations = 20
start_end_point = 'AA'
distancesDict = {}
DMsalesman = 80
mutationProb = 0.5
crossoverProb = 0.5

before = datetime.datetime.now()

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



def GeneratePopulation():
    for i in range(0, popsize):
        alphabeticRoute = routes.genAlphabeticRoute(citiestotal, distances)
        aRoute = random.sample(alphabeticRoute, len(alphabeticRoute))
        salesmenRoute = []
        salesmenRoute = sm.addCitiestoSalesmen(citiestotal, salesmenRoute, citiestotal, DMsalesman, aRoute, distancesDict)

        for i in range(citiestotal, 0, -1):
            try:
                if (len(salesmenRoute[i])==1):
                    del(salesmenRoute[i])
            except:
                #do nothing
                xyz = 0

        for i in range(0, len(salesmenRoute)):
            salesmenRoute[i].append(routes.getFitness(salesmenRoute[i], distancesDict))

        population.append(salesmenRoute)



def OptimizeSalesmen():
    f = open('output.csv', 'w+')
    global mutationProb
    pop = AGSalesman.evolvePopulation_multipleSalesman(population, distancesDict, DMsalesman, mutationProb, crossoverProb)

    counter = 0
    ant = []
    for i in range(1, nGenerations):
        print(i)

        if(i > int(nGenerations*0.2) and i <= int(nGenerations*0.4)):
            mutationProb = 0.4
        elif(i > int(nGenerations*0.4) and i <= int(nGenerations*0.6)):
            mutationProb = 0.3
        elif (i > int(nGenerations * 0.6) and i <= int(nGenerations * 0.8)):
            mutationProb = 0.2
        elif (i > int(nGenerations * 0.8)):
            mutationProb = 0.1

        if (i == 1):
            savefirstbest = pop[0][:]
        f.write(str(len(pop[0])) + ','+ str(routes.getTotalSalesmenDistance(pop[0]))+'\n')
        pop = AGSalesman.evolvePopulation_multipleSalesman(pop, distancesDict, DMsalesman, mutationProb, crossoverProb)

    return pop, savefirstbest


def DrawGraph(pop):
    G = nx.Graph()
    for i in range(0, len(pop[0])):
        for j in range(0, len(pop[0][i]) - 2):
            G.add_node(pop[0][i][j])
            G.add_node(pop[0][i][j + 1])
            G.add_edge(pop[0][i][j], pop[0][i][j + 1])


    #shuffle because consecutive colors are very similar
    clrs = random.sample(Colors.colors, len(Colors.colors))

    color_map = []
    for node in G:
        a = random.randint(1, 9)
        if node == 'AA':
            #warehouse is always red
            color_map.append('red')
        else:
            for i in range(0, len(pop[0])):
                if node in pop[0][i]:
                    color_map.append(clrs[i])

    nx.draw(G, with_labels=True, font_weight='bold', node_color=color_map)
    plt.show()


if __name__ == '__main__':

    readdata()
    GeneratePopulation()
    print(population)
    pop, savefirstbest = OptimizeSalesmen()
    DrawGraph(pop)
    print(pop[0])
    print('\nInitial best: ' + str(len(savefirstbest)) + ' Salesmen  |  ' + str(
        routes.getTotalSalesmenDistance(savefirstbest)) + ' Total distance')
    print('Final best: ' + str(len(pop[0])) + ' Salesmen  |  ' + str(
        routes.getTotalSalesmenDistance(pop[0])) + ' Total distance')

    #Call to get optimal route without salesmen
    routes.getOptimalTS1Salesman(start_end_point, citiestotal, distances, popsize, nGenerations, distancesDict)

    print(datetime.datetime.now() - before)