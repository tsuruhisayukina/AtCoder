A, B = map(int, input().split())
cnt = 0
for i in range(A, B+1):
    str_i = str(i)
    mae = str_i[0:2]
    ushiro = str_i[3:5]
    ushiro = ushiro[1] + ushiro[0]
    if mae == ushiro:
        cnt += 1
print(cnt)