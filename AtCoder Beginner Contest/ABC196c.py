# N = input()
# ans = 0

# for i in range(10, int(N)+1):
#     str_i = str(i)
#     if len(str_i)%2==1:
        
#         continue
#     center = len(str(i))//2 
    
#     if str_i[:center] != str_i[center:]:
#         continue
#     ans += 1
# print(ans)
N = int(input())
for i in range(1, 1000001):
    if int(str(i) * 2) > N:
        print(i - 1)
        exit()


