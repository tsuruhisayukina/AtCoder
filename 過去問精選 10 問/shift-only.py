N = int(input())
A = list(map(int, input().split()))
cnt = 0
while True:
    A_div = []
    for a in A:
        if a % 2 == 1:
            print(cnt)
            exit()
        div = a / 2
        A_div.append(div)
    A = A_div
    cnt += 1
