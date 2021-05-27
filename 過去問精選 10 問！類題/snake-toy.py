N, K = map(int, input().split())
l = list(map(int, input().split()))
l_sort = sorted(l, reverse=True)
ans = 0
for li in l_sort[:K]:
    ans += li
print(ans)