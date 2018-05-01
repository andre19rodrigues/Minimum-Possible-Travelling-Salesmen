import numpy


f = open('locations.csv', 'w+')
total = 10

for i in range(0, total):
    for j in range(0, total):
        if (j is not total-1):
            if (i is not j):
                f.write(str(numpy.random.randint(1, 20))+',')
            else:
                f.write(str(0)+',')
        else:
            if (i is not j):
                f.write(str(numpy.random.randint(1, 20)))
            else:
                f.write(str(0))
    if i is not total-1:
        f.write('\n')