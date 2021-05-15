A_list = list(map(int, input().split()))
A_sort = sorted(A_list)
A3_A2 = A_sort[2] - A_sort[1]
A2_A1 = A_sort[1] - A_sort[0]
if A3_A2 == A2_A1:
    print("Yes")
else:
    print("No")