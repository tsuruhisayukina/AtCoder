N, K = map(int, input().split())
ans = 0
while True:
    sho = N // K
    amari = N % K
    N = sho
    ans += 1
    if sho < K:
        if sho == 0:
            break
        else:
            ans += 1
            break
print(ans)