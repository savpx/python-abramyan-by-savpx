x=float(input("Введите массу шоколадных конфет X (кг): "))
a=float(input("Введите стоимость (рублей): "))
y=float(input("Введите массу ирисок (кг): "))
b=float(input("Введите стоимость (рублей): "))
kilogram_price_x = a / x
kilogram_price_y = b / y
chocolate_iriski_price_ratio = kilogram_price_x / kilogram_price_y
print("Стоимость 1 кг шоколадных конфет:", kilogram_price_x, "руб.")
print("Стоимость 1 кг ирисок:", kilogram_price_y, "руб.")
print('Шоколадные конфеты дороже ирисок в', chocolate_iriski_price_ratio, 'раз')