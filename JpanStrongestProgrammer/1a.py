M, D = map(int, input().split())
count = 0
for m in range(4, M+1):
    for d in range(22, D+1):
        d1 = d % 10
        d10 = d // 10
        if d1 < 2:
            continue
        if d10 < 2:
            continue
        if m == d1 * d10:
            count += 1
print(count)