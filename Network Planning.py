import numpy as np
from math import factorial

#erlang function
def erlang(A, m):
    L = (A ** m) / factorial(m)
    sum_ = 0
    for n in range(m + 1):
        sum_ += (A ** n) / factorial(n)

    return (L / sum_)

#user inputs
citySize = 1000
usersPerKm = 100
callsPerUser = 5/(60*24)
avgCallDuration = 2
providerChannels = 100
maxCellChannels = 20
carrier = 6.5
blocking = 0.05

usersTotal = citySize * usersPerKm #total number of users in a city
aUser = callsPerUser * avgCallDuration #erlang for a user

reuseFactor = [3,4,7,9,12,13]
n = [[2,3,4],[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3]] #number of interfering cells

N = []
x = 0

# 3N/n > C/I
for i in reuseFactor :
    j = n[x]
    a = (3*i)/j[0]
    b = (3*i)/j[1]
    c =(3*i)/j[2]
    x = x + 1
    if ( a > carrier ):
        N.append([i,6])
    if ( b > carrier):
        N.append([i,3])
    if ( c > carrier):
        N.append([i,2])


Min = 999999
x = 0

#get minimum (N*number of sectors) to maximize number of trunks
for i in N :
    temp = i[0]*i[1]
    if (temp < Min):
        Min = temp
        reuse = i[0]
        sector = i[1]
    
    
trunks = int(np.floor(providerChannels/(Min*2)))

erlangCell = np.arange(0.01,70,0.01)
finalErlang = 0

#trial and error to get best fitting erlang for givin blocking probability
for i in erlangCell:

    b = int(erlang(i, trunks)*100)/100

    if (b == blocking):
        aCell = i

subCell = int(aCell/aUser) #subscribers per cell

print ("Subs per Cell : " , subCell)
print ("Reuse-factor : " , reuse)
print ("Sectoring of : " , 360/sector)

