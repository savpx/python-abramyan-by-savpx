a=int(input("Введите число A: "))
b=int(input("Введите число B: "))
proiz=1
for i in range(a, b + 1):
    proiz*=i
print(proiz)