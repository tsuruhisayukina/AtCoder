N, A, B = map(int, input().split())
total = 0
for i in range(1, N+1):
    str_i = str(i)
    sum_i = 0
    for s in str_i:
        sum_i += int(s)
    if A <= sum_i <= B:
        total += i
print(total)