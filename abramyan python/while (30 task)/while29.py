eps = float(input("Введите epsilon: "))
previous_previous = 1.0
previous = 2.0
current = (previous_previous + 2 * previous) / 3
k = 3
while abs(current - previous) >= eps:
    previous_previous, previous = previous, current
    current = (previous_previous + 2 * previous) / 3
    k += 1
print(k, previous, current)
