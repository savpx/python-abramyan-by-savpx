n = int(input())
a1 = 1.0
a2 = 2.0
print(a1)
print(a2)
for _ in range(3, n + 1):
    a1, a2 = a2, (a1 + 2 * a2) / 3
    print(a2)