x = float(input())
n = int(input())
term = 1.0
s = term
for k in range(1, n + 1):
    term *= -(2 * k - 3) * x / (2 * k)
    s += term
print(s)