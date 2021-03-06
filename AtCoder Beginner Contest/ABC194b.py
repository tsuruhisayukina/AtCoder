N=int(input())
A_l=[]
B_l=[]
for i in range(N):
    A, B=map(int, input().split())
    A_l.append(A)
    B_l.append(B)

time=max(max(A_l, B_l, key=max))

for i in A_l:
    for j in B_l:
        if A_l.index(i)!=B_l.index(j) and time>max(i, j):
            time=max(i, j)
        if A_l.index(i)==B_l.index(j) and time>i+j:
            time=i+j

print(time)
