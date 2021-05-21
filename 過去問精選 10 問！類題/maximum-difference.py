N = int(input())
A = list(map(int, input().split()))
diff_max = 0
for i in range(N):
    for j in range(N):
        diff = abs(A[i] - A[j])
        if diff_max < diff:
            diff_max = diff
print(diff_max)