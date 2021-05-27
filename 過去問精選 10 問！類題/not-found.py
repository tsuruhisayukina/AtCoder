S = list(input())
for i in range(97, 97+26):
    al = chr(i)
    if not al in S:
        print(al)
        exit() 
print("None")