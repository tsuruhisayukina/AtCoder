N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A = set(A)
B = set(B)
ans = A ^ B
for i in ans:
    print(i, end = " ")