N = int(input())
cake_price = 4
donut_price = 7
max_cakes = N // cake_price
max_donuts = N // donut_price
for cake in range(max_cakes+1):
    for donut in range(max_donuts+1):
        money = cake_price * cake + donut_price * donut
        if money == N:
            print("Yes")
            exit()
print("No")