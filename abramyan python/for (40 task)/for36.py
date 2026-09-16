n = int(input())
k = int(input())
s = 0.0
for i in range(1, n + 1):
    p = 1.0
    for _ in range(k):
        p *= i
    s += p
print(s)
