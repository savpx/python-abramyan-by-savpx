import sys
print(sys.version)
print('кол во путей:', len(sys.path))
for p in sys.path[:4]:
    print('  ',p)

import math, random
print(math.pi)
print(random.random())

mods = sorted(sys.modules)
print('Всего загружено модулей:',len(mods))
print('Пример:',mods[:5])

#todo 1
public=[n for n in dir(math) if not n.startswith('__')]
print('Публичных имен в math:',len(public))
print('Первые 8:',public[:8])

#todo 2
print('Мой __name__ =',__name__,'мой __file__ =', __file__)