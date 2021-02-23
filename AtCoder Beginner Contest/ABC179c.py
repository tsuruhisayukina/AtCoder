import math
N=int(input())
A=1
ans=0
for i in range(N):
    ans+=math.floor((N-1)/A)
    A+=1
print(ans)


