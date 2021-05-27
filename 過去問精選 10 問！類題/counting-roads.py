N, M = map(int, input().split())
num = {}
for n in range(1, N+1):
    num[n] = 0
for i in range(M):
    ai, bi = map(int, input().split())
    num[ai] += 1
    num[bi] += 1
for ans in sorted(num.keys()):
    print(num[ans])