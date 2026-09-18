p = float(input("Введите P: "))
k = 1
distance = 10.0
summa = 10.0
while summa <= 200:
    distance += distance * p / 100
    summa += distance
    k += 1
print(k, summa)
