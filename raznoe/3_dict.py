
# =================================
#          Dict (словарь)
# =================================

print('-= dict =-')

# Словарь — неупорядоченная коллекция произвольных объектов с доступом по ключу.

a = {}
print(a)

b = {'key1' : 'value1', 'key2': 2, 'key3': [1,2,3]}
print(b)

# Создание с помощью функции dict:
c = dict(key='val', spam='eggs')
print(c)

d = dict([(1, 10), (2, 20)])
print(d)

# Создание словаря с помощью мотода fromkeys:
e = dict.fromkeys(['a', 'b', 'c'])
print(d)
f = dict.fromkeys(['a', 'b', 'c'], 'initial')
print(f)

# создание словаря с помощью генератора:
g = {i:i**2 for i in range(10)}
print(g)

# Доступ к элементу
print(f['a'])

f['b'] = 'spam'
f['d'] = 'eggs'
print(f)
# f['e'] # обращение к несуществующему ключу вызовет исключение

# удаление элемента
del f['d']

# Операции со словарями

# кол-во элементов
print(len(f))

# проверим, есть ли данный ключ
if 'a' in f:
	print("a in f")

if 'a' not in f: 
	print('a not in f')

if not 'a' in f:
	print('a not in f')	

print(f.get('d', 'eggs'))

# цикл по словарю
for key, value in f.items():
	print(key, value)

for key in f.keys():
	print(key)

for value in f.values():
	print(value)

# удаляет элемент c и возвращает его значение
print(f.pop('c'))
print(f)

# удаляет и возвращает пару (ключ, значение)
print(f.popitem())

print(f.setdefault('x', 'spam'))
print(f)


# вывод отсортированных по ключу пар ключ/значение
dict = {'a': 'alpfa', 'b': 'beta', 'g': 'gamma'}
print(dict)
for key in sorted(dict.keys()):
	print(key, dict[key])

# вывод пар ключ/значение отсортированных по значению
dict = {'one': 10, 'more': 5, 'thing': 11}
dict = sorted(dict.items(), key=lambda x: x[-1])
for key, value in dict:
	print('{0:>10} {1:<2}'.format(key, value))













