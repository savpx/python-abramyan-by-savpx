n = int(input("Введите N: "))
previous = 1
current = 1
k = 2
while current < n:
    previous, current = current, previous + current
    k += 1
print(k)
