import csv

import numpy


f = open('locations.csv', 'w+')
total = 50

for i in range(0, total):
    for j in range(0, total):
        if (j != total-1):
            if (i != j):
                f.write(str(numpy.random.randint(1, 20))+',')
            else:
                f.write(str(0)+',')
        else:
            if (i != j):
                f.write(str(numpy.random.randint(1, 20)))
            else:
                f.write(str(0))
    if i != total-1:
        f.write('\n')

def readdata():
    citiestotal = 0
    distances = []
    distancesDict = {}

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


    return distancesDict, distances, citiestotal