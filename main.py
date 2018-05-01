import csv
import random

import AlgGen as AG
import Salesmen as sm
import routes

distances = []
citiestotal = 0
citinames = []
population = []
salesmenRoute = []
popsize = 500
nGenerations = 50
start_end_point = 'AA'

Msalesman = 5
DMsalesman = 50


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






for i in range(0, 3):
    alphabeticRoute = routes.genAlphabeticRoute(citiestotal, distances)
    aRoute = random.sample(alphabeticRoute, len(alphabeticRoute))
    #print('aroute   '+str(aRoute))
    salesmenRoute = []
    salesmenRoute = sm.addCitiestoSalesmen(citiestotal, salesmenRoute, Msalesman, DMsalesman, aRoute, distances)

    for i in range(Msalesman, 0, -1):
        try:
            if (len(salesmenRoute[i])==1):
                del(salesmenRoute[i])
        except:
            xyz = 0
    #print(salesmenRoute)
    #print(alphabeticRoute)

    for i in range(0, len(salesmenRoute)):
        print(str(salesmenRoute[i]) +' '+ str(routes.getFitness(salesmenRoute[i], distances)))

    print()



#routes.getOptimalTS1Salesman(start_end_point, citiestotal, distances, popsize, nGenerations)