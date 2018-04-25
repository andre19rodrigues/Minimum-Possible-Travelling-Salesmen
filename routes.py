

def getFitness(cromo, distances, citiestotal):

    distancesSIZE = len(distances)

    popsize = len(cromo)
    sum = 0

    for j in range(0, citiestotal):
        for k in range(0, distancesSIZE):
            if j + 1 < citiestotal:
                if distances[k][0] == cromo[j] and distances[k][1] == cromo[j+1]:
                    sum = sum + int(distances[k][2])
                    break
            else:
                break
    return sum


def getFitnessTotalPopulation(population, distances, citiestotal):

    sum = 0
    for i in range(0, len(population)):
        sum = sum + getFitness(population[i], distances, citiestotal)

    return sum