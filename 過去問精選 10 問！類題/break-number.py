N = int(input())
cnt_max = 0
max_i = 1
for i in range(1, N+1):
    n = i
    cnt = 0
    while True:
        if n % 2 == 1:
            break
        cnt += 1
        n /= 2
    if cnt > cnt_max:
        cnt_max = cnt
        max_i = i
print(max_i)
        