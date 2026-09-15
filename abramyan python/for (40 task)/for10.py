n = int(input("Введите число N: "))
sum_result = 0.0
for i in range(1, n + 1):
    sum_result += 1 / i
print(sum_result)