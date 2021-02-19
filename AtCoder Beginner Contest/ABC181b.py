import math
N=int(input())
total = 0
for i in range(N):
    A, B=map(int, input().split())
    if (A+B)%2==0:
        total+=(A+B)*math.floor((B-A+1)/2)+(A+B)/2
    else:
        total+=(A+B)*(B-A+1)/2
print(math.floor(total))