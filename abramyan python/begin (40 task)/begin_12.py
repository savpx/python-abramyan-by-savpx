import math

a=float(input("Введите катет a: "))
b=float(input("Введите катет b: "))
c=math.sqrt(a**2+b**2)
p=a+b+c
print("Гипотенуза:", c) 
print("Периметр:", p)