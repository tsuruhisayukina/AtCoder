#解説みた、Counter({'1': 1, '2': 1, '3': 1, '4': 1})←Counterの表示
from collections import Counter
import itertools
S=input()
num=""
if len(S)==1 and int(S)%8==0:
    print("Yes")
    exit()

if len(S)==2 or len(S)==3:
    combi=itertools.permutations(S, len(S))
    for i in combi:
        for j in i:
            num+=j
        if int(num)%8==0:
            print("Yes")
            exit()
        num=""

if len(S)>=4:
    cnt=Counter(S)
    for i in range(104, 1000, 8):
       if not Counter(str(i)) - cnt:
            print("Yes")
            exit()
    
print("No")