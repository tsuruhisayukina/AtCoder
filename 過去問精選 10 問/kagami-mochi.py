N = int(input())
d = []
for i in range(N):
    di = int(input())
    if di in d:
        continue
    d.append(di)
print(len(d))
