n=int(input())
p=1
for i in range(n):
    a=float(input())
    b=a-int(a)
    print(b)
    p*=b
print(p)
