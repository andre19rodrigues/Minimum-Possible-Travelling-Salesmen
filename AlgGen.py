import random

crossoverProb = 0.5
mutationProb = 0.2

def uniformCrossover(motherCromo, fatherCromo, popsize):

    mask = []
    for i in range(0, popsize):
        if random.random(0, 1) < crossoverProb:
            mask.append(1)
        else:
            mask.append(0)

    child1 = []
    child2 = []

    for i in range(0, popsize):
        if(mask[i] == 1):
            child1.append(fatherCromo[i])
            child2.append(motherCromo[i])
        else:
            child1.append(motherCromo[i])
            child2.append(fatherCromo[i])

    return child1, child2


def randomMutation(cromo, popsize):
    for i in range(0, popsize):
        if(random.random(0,1) < mutationProb):
            val = random.randint(range(0, popsize-1), i)
            cromo[i], cromo[val] = cromo[val], cromo[i]

    return cromo
