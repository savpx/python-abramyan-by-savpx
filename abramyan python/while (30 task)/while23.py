a = int(input("Введите A: "))
b = int(input("Введите B: "))
while b != 0:
    a, b = b, a % b
print(a)
