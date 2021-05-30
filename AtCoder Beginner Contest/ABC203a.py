a, b, c = map(int, input().split())
if a == b != c:
    print(c)
elif a != b == c:
    print(a)
elif a == c != b:
    print(b)
elif a == b and b == c:
    print(b)
else:
    print(0)