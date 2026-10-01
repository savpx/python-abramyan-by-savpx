import sched, time

s = sched.scheduler(time.time, time.sleep)

def say(text):
    print(f"[{time.strftime('%H:%M:%S')}] {text}")

start = time.time()
print("Старт. Отсчёт времени от t0 = 0\n")

s.enter(2, 1, say, ("Прошло 2 секунды (приоритет 1)",))
s.enter(2, 0, say, ("Прошло 2 секунды (приоритет 0 – сработает ПЕРВЫМ)",))
s.enter(1, 1, say, ("Прошла 1 секунда",))
s.enterabs(start + 3, 1, say, ("Абсолютное время t0+3 с",))
s.enter(0.5, 1, say, ("Прошло 0.5 секунды",))

print("Очередь до run():", len(s.queue), "задач")
print("run() блокирует поток, пока все задачи не выполнятся:\n")


print("--- Содержимое s.queue до запуска ---")
for item in s.queue:
    print(f"Время: {item.time:.2f} | Приоритет: {item.priority} | Задача: {item.argument[0]}")

print("\n--- Объяснение порядка сортировки ---")
print("Очередь автоматически сортируется:")
print("1. По времени выполнения (time) — от самого ближайшего к дальнему.")
print("2. При совпадении времени — по приоритету (priority) — чем меньше число, тем выше приоритет.")
print("=====================================\n")


s.run()
print("\nГотово. Пустая очередь?", s.empty())
