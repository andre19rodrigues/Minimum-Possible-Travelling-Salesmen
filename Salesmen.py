import routes

def addCitiestoSalesmen(citiestotal, Salesmanroute, salesmentotalMax, distancesalesmen, alphabeticRoute, distancesDict):

    for i in range(0, salesmentotalMax):
        l = []
        Salesmanroute.append(l)
        Salesmanroute[i].append('AA')

        for j in range(0, citiestotal-1):
            if(alphabeticRoute[j][1] == 0):
                Salesmanroute[i].append(alphabeticRoute[j][0])
                alphabeticRoute[j][1] = 1
                if(routes.getFitness(Salesmanroute[i], distancesDict) > distancesalesmen):
                    a = len(Salesmanroute[i])
                    Salesmanroute[i].pop(a-1)
                    alphabeticRoute[j][1] = 0

                    Salesmanroute[i].append('AA')
                    if (routes.getFitness(Salesmanroute[i], distancesDict) > distancesalesmen):
                        while (routes.getFitness(Salesmanroute[i], distancesDict) > distancesalesmen):
                            a = len(Salesmanroute[i])
                            b = Salesmanroute [i][a-2]
                            c = alphabeticRoute.index([b,1])
                            alphabeticRoute[c][1] = 0
                            Salesmanroute[i].pop(a-2)
                        break
                    else:
                        break


        var = 0
        for k in range(0, citiestotal-1):
            if (alphabeticRoute[k][1] == 0):
                var = 1

        a = var
        if(var == 0):
            lensal = len(Salesmanroute[i])
            if(Salesmanroute[i][lensal-1] is not 'AA'):
                Salesmanroute[i].append('AA')
                if (routes.getFitness(Salesmanroute[i], distancesDict) > distancesalesmen):
                    while (routes.getFitness(Salesmanroute[i], distancesDict) > distancesalesmen):
                        a = len(Salesmanroute[i])
                        b = Salesmanroute[i][a - 2]
                        c = alphabeticRoute.index([b, 1])
                        alphabeticRoute[c][1] = 0
                        Salesmanroute[i].pop(a - 2)

    return Salesmanroute


def addFlag(alphabeticRoute, citiestotal):
    for i in range(0, citiestotal-1):
        alphabeticRoute[i].append(0)

    return alphabeticRoute