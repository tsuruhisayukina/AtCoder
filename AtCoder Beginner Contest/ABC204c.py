N, M = map(int, input().split())
A = []
B = []
road = []
cnt = N
for i in range(M):
    Ai, Bi = map(int, input().split())
    A.append(Ai)
    B.append(Bi)
    road.append([Ai, Bi])
for i in range(1, 2001):
    for j in range(1, 2001):
        if i == j:
            continue
        if (i in A) and (j in B):
            cnt += 1 
print(cnt)