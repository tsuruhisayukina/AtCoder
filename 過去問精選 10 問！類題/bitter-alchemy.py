N, X = map(int, input().split())
m = []
for i in range(N):
    mi = int(input())
    m.append(mi)
    X -= mi
ans = N + X // min(m)
print(ans)