N = int(input())
for i in range(1, 10):
    for j in range(1, 10):
        ans = i * j
        if ans == N:
            print("Yes")
            exit()
print("No")