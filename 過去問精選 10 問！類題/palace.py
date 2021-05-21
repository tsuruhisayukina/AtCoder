N = int(input())
T, A = map(int, input().split())
H_list = list(map(int, input().split()))
diff_small = 10**10
diff_small_i = 0
for i in range(1, N+1):
    ave = T - H_list[i-1] * 0.006
    diff = abs(A - ave)
    if diff_small > diff:
        diff_small = diff
        diff_small_i = i
print(diff_small_i)