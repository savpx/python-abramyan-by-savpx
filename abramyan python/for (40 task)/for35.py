n = int(input())
a1 = 1
a2 = 2
a3 = 3
print(a1)
print(a2)
print(a3)
for _ in range(4, n + 1):
    a1, a2, a3 = a2, a3, a3 + a2 - 2 * a1
    print(a3)