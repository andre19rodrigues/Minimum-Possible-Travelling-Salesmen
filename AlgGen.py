import random

crossoverProb = 0.5
mutationProb = 0.2

def uniformCrossover(motherCromo, fatherCromo, citiestotal):

    a = random.randint(0, citiestotal-1)
    b = random.randint(0, citiestotal-1)

    child = []
    for i in range(0, citiestotal):
        child.append(999999)

    for i in range(0, citiestotal):
        if (a < b and i > a and i < b):
            child[i] = motherCromo[i]

        elif (a > b and not (i < a and i > b)):
            child[i] = motherCromo[i]


    for i in range(0, citiestotal):
        if (fatherCromo[i] not in child):
            for j in range(0, citiestotal):
                if (child[j] == 999999):
                    child[j] = fatherCromo[i]
                    break

    return child


def randomMutation(cromo, popsize):
    for i in range(0, popsize):
        if(random.random(0,1) < mutationProb):
            val = random.randint(range(0, popsize-1), i)
            cromo[i], cromo[val] = cromo[val], cromo[i]

    return cromo
