x = float(input())
n = int(input())
term = x
s = term
for k in range(1, n + 1):
    term *= (2 * k - 1) ** 2 * x ** 2 / ((2 * k) * (2 * k + 1))
    s += term
print(s)