from math import sin

n = int(input())
a = float(input())
b = float(input())
h = (b - a) / n
print(h)
for i in range(n + 1):
    x = a + i * h
    print(1 - sin(x))