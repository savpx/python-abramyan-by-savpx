import math
import random

deck = [f"{v}{s}" for s in "♣♦♥♠" for v in "6789TJQKA"]
random.seed(7)
print("Всего карт в колоде:", len(deck))

hand = random.sample(deck, 5)
print("Рука игрока (sample):", hand)

print("Карта дня (choice) :", random.choice(deck))

weights = {"обычная": 70, "редкая": 25, "легендарная": 5}
loot = random.choices(list(weights), weights=list(weights.values()), k=5)
print("Лут (choices, 5 шт.):", loot)

random.shuffle(deck)
print("После shuffle      :", deck[:6], "...")

print("\n--- Раздача 3 игрокам по 5 карт ---")
players = ["Алиса", "Борис", "Вера"]
pool = deck.copy()

for p in players:
    player_hand = random.sample(pool, 5)
    for card in player_hand:
        pool.remove(card)
    print(f"{p:6s}: {player_hand}")

print("\n==============Лотерея 6 из 45==========================")

lottery_numbers = sorted(random.sample(range(1, 46), 6))

print("--- Результаты лотереи «6 из 45» ---")
print("Выигрышные номера:", lottery_numbers)

total_combinations = math.comb(45, 6)
probability = 1 / total_combinations

print("\n--- Теоретический расчет (math.comb) ---")
print(f"Всего возможных комбинаций: {total_combinations:,}".replace(",", " "))
print(f"Вероятность угадать все 6 номеров: {probability:.10f}")
print(f"Шанс выиграть джекпот: 1 из {total_combinations:,}".replace(",", " "))
