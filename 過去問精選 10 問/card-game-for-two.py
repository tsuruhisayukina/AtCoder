N = int(input())
a = list(map(int, input().split()))
a = sorted(a, reverse=True)
alice = 0
bob = 0
for i in range(len(a)):
    if i % 2 == 0:
        alice += a[i]
    else:
        bob += a[i]
ans = alice - bob
print(ans)