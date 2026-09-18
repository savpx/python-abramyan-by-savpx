n = int(input("Введите N: "))
previous = 1
current = 1
while current <= n:
    previous, current = current, previous + current
print(current)
