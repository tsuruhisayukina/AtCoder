N, K = map(int, input().split())
for k in range(K):
    if N % 200 == 0:
        N //= 200
    else:
        N = str(N) + "200"
        N = int(N)
print(N)