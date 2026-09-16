n = int(input())
a = float(input())
b = float(input())
h = (b - a) / n
print(h)
for i in range(n + 1):
    print(a + i * h)