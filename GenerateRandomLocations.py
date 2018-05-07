import numpy


f = open('locations.csv', 'w+')
total = 500

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