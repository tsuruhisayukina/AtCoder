N, L = map(int, input().split())
S = []
for i in range(N):
    Si = input()
    S.append(Si)
S = sorted(S)
ans = ''.join(S)
print(ans)