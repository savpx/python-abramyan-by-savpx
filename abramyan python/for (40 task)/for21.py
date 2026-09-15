n=int(input())
fact=1.0
s=1.0
for i in range(1, n + 1):
    fact*=i
    s+=1 / fact
print(s)