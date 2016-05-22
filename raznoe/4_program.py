#!/usr/bin/python
# -*- coding: utf-8 -*-

# Возможны еще такие варианты:
#!/usr/bin/env python
#!/usr/local/bin/python

# Импорт модулей
import sys

def hello1():
    # help(print) — чтобы узнать, какие аргументы принимает функция print()    
    print('Привет', sys.argv[1], sep=', ', end='!\n')
    # Аргументы командной строки можно получить через sys.argv[1], sys.argv[2] ...
    # sys.argv[0] содержит название самого скрипта

def hello2(params, pref='Привет'):    
    if len(params) == 1:
        name = params[0]
    elif len(params) == 2:
        name = params[0] + ' ' + params[1]
        # или с использованием форматирования
        name = '{0} {1}'.format(params[0], params[1])
        # или так, получая доступ к элементам списка
        name = '{0[0]} {0[1]}'.format(params)
        # или так, передавая элементы списка в качестве аргументов функции
        name = '{0} {1}'.format(*params)
        # или так, используя именованные параметры
        name = '{name} {sname}'.format(name=params[0], sname=params[1])
        # или форматирование в старом стиле (но лучше все-таки пользоваться новым)
        name = '%s %s' % (params[0], params[1])
        pref = 'Здравствуйте'
    else:
        name = 'NoName'
    print(pref, name, sep=', ', end='!\n')

def main():
    # hello1()
    hello2(sys.argv[1:])

# Начало программы — передаем управление функции main
if __name__ == '__main__':
    main()