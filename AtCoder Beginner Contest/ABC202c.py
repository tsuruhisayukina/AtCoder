N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
cnt = 0
for i in range(N):
    if B[i] in A and (B.index(B[i]) + 1) in C:
        cnt += 1
print(cnt**2)