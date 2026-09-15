a=float(input())
n=int(input())
s=1
p=1
for k in range(1, n + 1):
    p*=a
    s+=p * (-1) ** k
print(s)