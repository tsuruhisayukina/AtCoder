import itertools

N=int(input())
x_y_list=[]
for i in range(N):
    x_y_list.append(list(map(int, input().split())))
combi=itertools.combinations(x_y_list, 3)
for i in combi:
    VA=i[0]
    VB=i[1]
    VC=i[2]
    
    if VA[0]==VB[0]==VC[0]:
        print("Yes")
        exit()
    elif VA[1]==VB[1]==VC[1]:
        print("Yes")
        exit()

    if VA[0]!=VB[0]:
        aAB=(VB[1]-VA[1])/(VB[0]-VA[0])  
    else:
        continue

    if VA[0]!=VC[0]:
        aAC=(VC[1]-VA[1])/(VC[0]-VA[0])
    else:
        continue

    if aAB==aAC:
        print("Yes")
        exit()

print("No")    

