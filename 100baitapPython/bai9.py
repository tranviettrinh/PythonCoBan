import math

from numpy import sqrt
C=50
H=30
D = (input('nhap gia tri D: '))
dsD = D.split(',')
dsQ =[]
for i in range(0,len(dsD)):
    Q = sqrt((2*C*int(dsD[i]))/H)+0.5
    dsQ.append(str(int(Q)))
print(','.join(dsQ))
