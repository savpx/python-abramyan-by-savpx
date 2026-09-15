v1=float(input("Введите скорость первого автомобиля (км/ч): "))
v2=float(input("Введите скорость второго автомобиля (км/ч): "))
s=float(input("Введите расстояние между автомобилями (км): "))
t=float(input("Введите время в часах T: "))
s_nachalnoe=s
s_obshchee=(v1 + v2) * t
s_konechnoe=s_nachalnoe + s_obshchee
print("Расстояние между автомобилями через", t, "часов:", s_konechnoe, "км")