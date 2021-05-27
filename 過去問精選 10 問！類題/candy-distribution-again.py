N, x = map(int, input().split())
a = list(map(int, input().split()))
a_sort = sorted(a)
total = sum(a_sort)
candy = x
cnt = 0
for i in range(N):
    if candy >= a_sort[i]:
        cnt += 1
    candy -= a_sort[i]
if total < x:
    cnt -= 1
    print(cnt)
else:
    print(cnt)