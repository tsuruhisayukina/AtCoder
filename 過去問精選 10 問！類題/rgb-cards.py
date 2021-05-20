r, g, b = input().split()
num = r + g + b
num = int(num)
if num % 4 == 0:
    print("YES")
else:
    print("NO")