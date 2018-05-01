import random

crossoverProb = 0.5
mutationProb = 0.2

def Crossover(motherCromo, fatherCromo):

    lmother = len(motherCromo)
    lfather = len(fatherCromo)
    a = random.randint(0, lmother-2)
    b = random.randint(0, lmother-2)

    child = []
    child.insert(0, 'AA')
    for i in range(1, lmother):
        child.append(999999)

    child.append('AA')

    for i in range(1, lmother):
        if (a < b and i > a and i < b):
            child[i] = motherCromo[i]

        elif (a > b and not (i < a and i > b)):
            child[i] = motherCromo[i]


    for i in range(1, lfather):
            for j in range(1, lmother):
                if (fatherCromo[i] not in child):
                    if (child[j] == 999999):
                        child[j] = fatherCromo[i]
                        break

    return child



def randomMutation(cromo):

    lcromo = len(cromo)

    for i in range(1, lcromo-2):
        if random.random() < mutationProb:
            val = i
            while val == i:
                val = random.randint(1, lcromo - 2)
            cromo[i], cromo[val] = cromo[val], cromo[i]

    return cromo
