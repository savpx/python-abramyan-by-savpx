import random

random.seed(42)
print('random()             :', round(random.random(), 6))
print('uniform(1, 10)       :', round(random.uniform(1, 10), 3))
print('randint(1,6)         :', random.randint(1,6))
print('randrange(0,100,5))  :', random.randrange(0,100,5))

print('\n--- Бросок двух кубиков, 5 раз ---')
for i in range(1, 6):
    a, b = random.randint(1, 6), random.randint(1, 6)
    print(f'Бросок {i}: {a} + {b} = {a + b}')

print('\n--- Статистика 10000 бросков одного кубика ---')
random.seed(2026)
counts = {i: 0 for i in range(1, 7)}
N = 10_000
for _ in range(N):
    counts[random.randint(1, 6)] += 1

for face, cnt in sorted(counts.items()):
    bar = '#' * (cnt // 50)
    print(f'{face}: {cnt:5d} ({cnt / N * 100:5.2f}%) {bar}')

print('\n--- Отклонение от теоретической вероятности (16.67%) ---')
for face, cnt in sorted(counts.items()):
    lala = cnt / N * 100 - 16.67
    print(f'Грань {face}: отклонение {lala:+.2f}%')
    
print('\n--- Статистика 100000 бросков ТРЕХ кубиков ---')

sums_counts = {i: 0 for i in range(3, 19)}
N_three = 100_000

for _ in range(N_three):
    total_sum = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
    sums_counts[total_sum] += 1

for total_sum, cnt in sorted(sums_counts.items()):
    bar = '#' * (cnt // 500)
    print(f'Сумма {total_sum:2d}: {cnt:5d} ({cnt / N_three * 100:5.2f}%) {bar}')
most_frequent_sum = max(sums_counts, key=sums_counts.get)

print(f'Чаще всего выпадает сумма: **{most_frequent_sum}** (она выпала {sums_counts[most_frequent_sum]} раз)')