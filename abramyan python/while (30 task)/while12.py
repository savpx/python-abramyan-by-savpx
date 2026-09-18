n = int(input("Введите N: "))
k = 0
summa = 0
while summa + k + 1 <= n:
    k += 1
    summa += k
print(k, summa)
