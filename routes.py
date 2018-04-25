

def getFitness(cromo, distances, citiestotal):

    distancesSIZE = len(distances)

    popsize = len(cromo)
    sum = 0

    for j in range(0, citiestotal):
        for k in range(0, distancesSIZE):
            if j + 1 < citiestotal:
                if distances[k][0] == cromo[j] and distances[k][1] == cromo[j+1]:
                    a = distances[k][0]
                    b = distances[k][1]
                    c = distances[k][2]
                    sum = sum + int(distances[k][2])
            else:
                break
    return sum