a=int(input("Введите число A: "))
b=int(input("Введите число B: "))
summ_kv=0
for i in range(a, b + 1):
    summ_kv+=i**2
print(summ_kv)