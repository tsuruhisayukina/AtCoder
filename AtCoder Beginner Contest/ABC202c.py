from collections import Counter
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
cnt = 0
A_cnt = Counter(A)
for j in range(N):
    Dj = B[C[j]-1]
    cnt += A_cnt[Dj]
print(cnt)