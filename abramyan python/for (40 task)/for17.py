a=float(input())
n=int(input())
s=1
p=1
for _ in range(n):
    p*=a
    s+=p
print(s)