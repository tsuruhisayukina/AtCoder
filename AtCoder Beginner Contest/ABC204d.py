N = int(input())
T = list(map(int, input().split()))
ans = 10**7
for i in range(2 ** N):
    tin_0 = 0
    tin_1 = 0
    for j in range(N):
        if (i >> j) & 1:
            tin_1 += T[j]
            continue
        tin_0 += T[j]
    if max(tin_0, tin_1) < ans:
        ans = max(tin_0, tin_1)
print(ans)