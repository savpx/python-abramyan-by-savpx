n = int(input("Введите N: "))
found = False
while n > 0:
    if (n % 10) % 2 == 1:
        found = True
    n //= 10
print(found)
