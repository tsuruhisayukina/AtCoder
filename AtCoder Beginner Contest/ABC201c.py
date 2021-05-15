import math
S = input()
maru = S.count("o")
batu = S.count("x")
hatena = S.count("?")
sukima = 4 - maru
if maru > 4:
    print(0)
    exit
if batu == 10:
    print(0)
    exit
if maru == 4:
    print(math.factorial(4))
    exit
if maru == 1:
    ans = 