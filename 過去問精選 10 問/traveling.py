N = int(input())
t = 0
x = 0
y = 0
for i in range(N):
    ti, xi, yi = map(int, input().split())
    dt = ti - t
    dl = abs(xi - x) + abs(yi - y)
    if xi == x and yi == y:
        print("No")
        exit
    t = ti
    x = xi
    y = yi
    if dl > dt:
        print("No")
        exit()
    if dl % 2 != dt % 2:
        print("No") 
        exit()
print("Yes")