p = float(input("Введите P: "))
k = 0
s = 1000.0
while s <= 1100:
    s += s * p / 100
    k += 1
print(k, s)
