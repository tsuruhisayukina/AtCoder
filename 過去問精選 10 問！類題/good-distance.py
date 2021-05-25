import math
N, D = map(int, input().split())
X_l = []
for i in range(N):
    X = list(map(int, input().split()))
    X_l.append(X)
cnt = 0
for i in X_l:
    for j in X_l:
        if i == j:
            continue
        distance = 0
        for d in range(D):
            distance += (i[d] - j[d])**2
        distance = math.sqrt(distance)
        if float.is_integer(distance):
            cnt += 1
print(int(cnt/2))