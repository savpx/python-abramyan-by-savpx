n = int(input("Введите N: "))
divisor = 2
prime = True
while divisor * divisor <= n:
    if n % divisor == 0:
        prime = False
    divisor += 1
print(prime)
