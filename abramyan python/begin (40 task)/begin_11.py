a=float(input("Введите число a: "))
b=float(input("Введите число b: "))
if a==0 or b==0:
    print("Ошибка: числа должны быть ненулевыми.")
else:
    summ= abs(a)+abs(b)
    razn= abs(a)-abs(b)
    proiz= abs(a)*abs(b)
    chast= abs(a)/abs(b)
print("Сумма модулей:", summ)
print("Разность модулей:", razn)
print("Произведение модулей:", proiz)
print("Частное модулей:", chast)