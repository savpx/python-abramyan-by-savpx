a = int(input())
b = int(input())
for x in range(a, b + 1):
    for _ in range(x - a + 1):
        print(x)
