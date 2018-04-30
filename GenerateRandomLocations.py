import numpy


f = open('locations.csv', 'w+')
total = 50

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

#
# f = open('locations.csv', 'w+')
#
# control = 10
# i = 0
#
# for a in range(65, 91):
#     for aa in range(65, 91):
#         for b in range(65, 91):
#             for bb in range(65, 91):
#                 if i is not control:
#                     if chr(a)+chr(aa) == chr(b)+chr(bb):
#                         f.write(chr(a)+chr(aa)+','+chr(b)+chr(bb)+','+str(0)+'\n')
#                         i += 1
#                     else:
#                         f.write(chr(a)+chr(aa)+','+chr(b)+chr(bb)+','+str(numpy.random.randint(1, 20))+'\n')
#                         f.write(chr(b)+chr(bb)+','+chr(a)+chr(aa)+','+str(numpy.random.randint(1, 20))+'\n')
#                         i += 1
#                 else:
#                     break


#
# f = open('locations.csv', 'w+')
#
# control = 10
# i = 0
#
# for a in range(65, 91):
#     for b in range(65, 91):
#         if i is not control:
#             if chr(a) == chr(b):
#                 f.write(chr(a)+','+chr(b)+','+str(0)+'\n')
#                 #i += 1
#             else:
#                 f.write(chr(a)+','+chr(b)+','+str(numpy.random.randint(1, 20))+'\n')
#                 f.write(chr(b)+','+chr(a)+','+str(numpy.random.randint(1, 20))+'\n')
#                 i += 1
#         else:
#             break