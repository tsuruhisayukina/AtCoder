N = int(input())
L = list(map(int, input().split()))
cnt = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if L[i] != L[j] and L[j]!= L[k] and L[i] != L[k]:
                max_L = max(L[i], L[j], L[k])
                if max_L < L[i] + L[j] + L[k] - max_L:
                    cnt += 1
print(cnt)