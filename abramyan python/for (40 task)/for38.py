n = int(input())
s = 0.0
for i in range(1, n + 1):
    p = 1.0
    for _ in range(n - i + 1):
        p *= i
    s += p
print(s)