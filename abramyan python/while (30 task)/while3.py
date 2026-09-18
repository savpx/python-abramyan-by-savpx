n=int(input("Введите N: "))
k=int(input("Введите K: "))
dell=0
while n>=k:
    n=n-k
    dell+=1
print('Частное:', dell)
print('Остаток:', n) 