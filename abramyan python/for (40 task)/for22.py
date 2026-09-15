x=float(input())
n=int(input())
term=1.0
s=term
for i in range(1, n + 1):
    term*= x / i
    s+=term
print(s)