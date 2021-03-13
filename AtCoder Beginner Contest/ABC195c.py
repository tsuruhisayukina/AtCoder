import math
N = int(input())
one = N/10**3
two = N/10**6
three = N/10**9
four = N/10**12
five = N/10**15
comma=0

if one<1:
    print(comma)
    exit

if one>=1 and two<1:
    comma = N-10**3+1
    print(comma)
    exit

if two>=1 and three<1:
    comma = N-10**3+1 + N-10**6+1
    print(comma)
    exit

if three>=1 and four<1:
    comma = N-10**3+1 + N-10**6+1 + N-10**9+1
    print(comma)
    exit

if four>=1 and five<1:
    comma = N-10**3+1 + N-10**6+1 + N-10**9+1 + N-10**12+1
    print(comma)
    exit

if five>=1:
    comma = N-10**3+1 + N-10**6+1 + N-10**9+1 + N-10**12+1 + N-10**15+1
    print(comma)
    exit   
