n = int(input("Введите N: "))
result = 0
while n > 0:
    result = result * 10 + n % 10
    n //= 10
print(result)
