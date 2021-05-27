N = int(input())
ans = 10 ** 10
for i in range(1, N):
    A = i
    B = N - A
    min_sum = 0
    for a in str(A):
        min_sum += int(a)
    for b in str(B):
        min_sum += int(b)
    if ans > min_sum:
        ans = min_sum
print(ans)