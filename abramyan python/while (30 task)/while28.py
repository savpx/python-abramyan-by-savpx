eps = float(input("Введите epsilon: "))
previous = 2.0
current = 2 + 1 / previous
k = 2
while abs(current - previous) >= eps:
    previous = current
    current = 2 + 1 / previous
    k += 1
print(k, previous, current)
