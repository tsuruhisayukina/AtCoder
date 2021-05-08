N = int(input())
A = N % 100
ans = N // 100
if A == 0:
    print(ans)
else:
    print(ans + 1)