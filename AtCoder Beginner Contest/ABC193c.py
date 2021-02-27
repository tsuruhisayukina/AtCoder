import math
N=int(input())
a_max=math.floor(N**(1/2))
b_max=math.floor(math.log(N)/math.log(2))
can=[]
for i in range(2, a_max+1):
    for j in range(2, b_max+1):
        if i**j<=N:
            can.append(i**j)
        else:
            continue
print(N-len(set(can)))
