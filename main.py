import csv
import datetime
import random
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
nGenerations = 100000
start_end_point = 'AA'
distancesDict = {}
DMsalesman = 50
mutationProb = 0.5
crossoverProb = 0.5

before = datetime.datetime.now()

#shuffle because consecutive colors are very similar
clrs = random.sample(Colors.colors, len(Colors.colors))

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



def DrawGraph(pop, counter):
    G = nx.Graph()
    for i in range(0, len(pop)):
        for j in range(0, len(pop[i]) - 2):
            G.add_node(pop[i][j])
            G.add_node(pop[i][j + 1])
            G.add_edge(pop[i][j], pop[i][j + 1])


    color_map = []
    for node in G:
        a = random.randint(1, 9)
        if node == 'AA':
            #warehouse is always red
            color_map.append('red')
        else:
            for i in range(0, len(pop)):
                if node in pop[i]:
                    color_map.append(clrs[i])

    nx.draw(G, with_labels=True, font_weight='bold', node_color=color_map)
    plt.show()
    #Output as a file
    #plt.savefig(str(counter)+'.png')
    plt.close()



def OptimizeSalesmen():
    f = open('output.csv', 'w+')
    global mutationProb

    pop = AGSalesman.evolvePopulation_multipleSalesman(population, distancesDict, DMsalesman, mutationProb, crossoverProb)

    for i in range(1, nGenerations):
        print(i)

        if(i > int(nGenerations*0.3) and i <= int(nGenerations*0.5)):
            mutationProb = 0.4
        elif(i > int(nGenerations*0.5) and i <= int(nGenerations*0.7)):
            mutationProb = 0.3
        elif (i > int(nGenerations * 0.7) and i <= int(nGenerations * 0.9)):
            mutationProb = 0.2
        elif (i > int(nGenerations * 0.9)):
            mutationProb = 0.1

        if (i == 1):
            savefirstbest = pop[0][:]
        f.write(str(len(pop[0])) + ','+ str(routes.getTotalSalesmenDistance(pop[0]))+'\n')
        pop = AGSalesman.evolvePopulation_multipleSalesman(pop, distancesDict, DMsalesman, mutationProb, crossoverProb)

        #Uncomment the next line to draw the graph of every generation. The execution will be slower
        #DrawGraph(pop[0], i)

    return pop, savefirstbest



if __name__ == '__main__':

    readdata()
    GeneratePopulation()
    print(population) #print initial population

    pop, savefirstbest = OptimizeSalesmen() #Main function to reduce number of salesmen and distances size per salesmen

    #The zero as argument here is useless, but if you want to save the graph of each generation, the function expects to
    #receive as "counter" the generation number to be used in the png file name
    DrawGraph(savefirstbest, 0)     #First optimal solution
    DrawGraph(pop[0], 0)            #Optimal solucion n generations after

    print(pop[0])
    print('\nInitial best: ' + str(len(savefirstbest)) + ' Salesmen  |  ' + str(
        routes.getTotalSalesmenDistance(savefirstbest)) + ' Total distance')
    print('Final best: ' + str(len(pop[0])) + ' Salesmen  |  ' + str(
        routes.getTotalSalesmenDistance(pop[0])) + ' Total distance')

    #Call to get optimal route without salesmen
    #routes.getOptimalTS1Salesman(start_end_point, citiestotal, distances, popsize, nGenerations, distancesDict)

    #print the execution time
    print(datetime.datetime.now() - before)