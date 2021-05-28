W, H, N = map(int, input().split())
x_left = 0
x_right = W
y_down = 0
y_up = H
for i in range(N):
    xi, yi, a = map(int, input().split())
    if a == 1:
        x_left = max(xi, x_left)
    elif a == 2:
        x_right = min(xi, x_right)
    elif a == 3:
        y_down = max(yi, y_down)
    else:
        y_up = min(yi, y_up)

    if x_right <= x_left or y_up <= y_down:
        print(0)
        exit()
    
area = (x_right - x_left) * (y_up - y_down)
print(area)