a = float(input("Введите A: "))
b = float(input("Введите B: "))
c = float(input("Введите C: "))
count = 0
while a >= c:
    a -= c
    width = b
    while width >= c:
        width -= c
        count += 1
print(count)
