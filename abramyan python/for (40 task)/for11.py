n = int(input("Введите число N: "))
sum_result = 0
for i in range(n, 2 * n + 1):
    sum_result += i ** 2
print(sum_result)
