N = int(input())
mydict = {}
for i in range(N):
    S, T = input().split()
    mydict[int(T)] = S
mydict_sort = sorted(mydict)
print(mydict[mydict_sort[-2]])