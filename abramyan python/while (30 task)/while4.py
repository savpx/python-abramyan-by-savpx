n=int(input('Введите число N: '))
while n>1 and n%3==0:
    n//3
if n==1:
    print(True)
else:
    print(False)