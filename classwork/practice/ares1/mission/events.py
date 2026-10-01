import random

EVENTS = [
    ("Микрометеорит пробил обшивку",   -15, 0.4),
    ("Солнечная вспышка: радиация",   -10, 0.2),
    ("Удачная коррекция курса",        +5, 0.2),
    ("Найдены запасы предыдущей миссии", +20, 0.1),
    ("Отказ системы охлаждения",       -25, 0.1),
]

def random_event(seed=None):
    rnd = random.Random(seed)
    names, weights = [e[0] for e in EVENTS], [e[2] for e in EVENTS]
    event_index = rnd.choices(range(len(EVENTS)), weights=weights, k=1)[0]
    return EVENTS[event_index][0], EVENTS[event_index][1]
