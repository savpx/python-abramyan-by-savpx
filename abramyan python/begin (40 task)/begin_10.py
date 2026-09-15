a=float(input("Введите число a: "))
b=float(input("Введите число b: "))
if a==0 or b==0:
    print("Ошибка: числа должны быть ненулевыми.")
else:
    summ=(a+b)**2
    razn=(a-b)**2
    proiz=(a*b)**2
    chast=(a/b)**2
print("Сумма квадратов:", summ)
print("Разность квадратов:", razn)
print("Произведение квадратов:", proiz)
print("Частное квадратов:", chast)