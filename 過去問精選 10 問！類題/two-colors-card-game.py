from collections import Counter
N = int(input())
s = []
t = []
for i in range(N):
    si = input()
    s.append(si)
M = int(input())
for i in range(M):
    ti = input()
    t.append(ti)
s = Counter(s)
t = Counter(t)

cnt = 0
for key in s:
    cnt_max = s[key] - t[key]
    if cnt < cnt_max:
        cnt = cnt_max
print(cnt)