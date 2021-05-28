from collections import Counter
N, K = map(int, input().split())
A = list(map(int, input().split()))
A_cnt = Counter(A)
quantity = len(A_cnt.keys())
if quantity <= K:
    print(0)
    exit()
value_sort = sorted(A_cnt.values())
change = quantity - K
cnt = 0
for i in range(change):
    cnt += value_sort[i]
print(cnt)