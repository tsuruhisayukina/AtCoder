c = []
for i in range(3):
    ci = list(map(int, input().split()))
    c.append(ci)

for i in range(1, 3+1):
    for j in range(1, 3+1):
        print(c[i-1][j-1])