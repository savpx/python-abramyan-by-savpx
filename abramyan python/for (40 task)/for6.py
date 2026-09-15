a = float(input("Введите цену 1 кг конфет: "))
for i in range(12, 21, 2):
    weight = i / 10
    print(f"Цена {weight} кг конфет: {a * weight}")
