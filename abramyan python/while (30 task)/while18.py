n = int(input("Введите N: "))
count = 0
summa = 0
while n > 0:
    count += 1
    summa += n % 10
    n //= 10
print(count, summa)
