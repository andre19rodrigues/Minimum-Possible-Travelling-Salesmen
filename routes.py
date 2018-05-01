

def getFitness(cromo, distances, citiestotal):
    sum = 0

    for j in range(0, citiestotal):
        s = (cromo[j], cromo[j + 1])
        val = distances[s]
        sum = sum + int(val)

    return sum


def getFitnessTotalPopulation(population, distances, citiestotal):
    sum = 0
    for i in range(0, len(population)):
        sum = sum + getFitness(population[i], distances, citiestotal)

    return sum


 # for k in range(0, distancesSIZE):
        #     if j + 1 < citiestotal + 1:
        #         if distances[k][0] == cromo[j] and distances[k][1] == cromo[j+1]:
        #             sum = sum + int(distances[k][2])
        #             break
        #     else:
        #         break