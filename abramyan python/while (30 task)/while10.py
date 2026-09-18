n = int(input("Введите N: "))
k = 0
power = 1
while power * 3 < n:
    power *= 3
    k += 1
print(k)
