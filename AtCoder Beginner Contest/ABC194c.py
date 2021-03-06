import itertools
N=int(input())
A_l=list(map(int, input().split()))
total=0
for v in itertools.combinations(A_l, 2):
    total+=(v[0]-v[1])**2
print(total)