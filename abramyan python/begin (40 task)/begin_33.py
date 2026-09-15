x=float(input("Введите массу конфет X (кг): "))
a=float(input("Введите стоимость A (рублей): "))
y=float(input("Введите массу Y (кг): "))
price_per_kg = a/x
cost_y = price_per_kg*y
print("Стоимость Y кг конфет:", cost_y)
print("Стоимость 1 кг конфет:", price_per_kg)
