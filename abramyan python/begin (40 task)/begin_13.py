import math

R1 = float(input("Введите радиус R1: "))
R2 = float(input("Введите радиус R2: "))
if R1<=R2:
    print("Ошибка: R1 должен быть больше R2.")
else:
    S1 = math.pi * R1**2
    S2 = math.pi * R2**2
    S3 = S1-S2
print("Площадь первого круга S1 =", S1)
print("Площадь второго круга S2 =", S2)
print("Площадь кольца S3 =", S3)
