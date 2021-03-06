A, B=map(int, input().split())
total=A+B
fat=B
if total>=15 and fat>=8:
    print(1)
    exit()
elif total>=10 and fat>=3:
    print(2)
    exit
elif total>=3:
    print(3)
    exit
else:
    print(4)
    exit