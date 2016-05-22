f = open('text.txt', 'r')
print(f)
print(f.read())
print(f.read(10))

# переместим курсор в начало файла
f.seek(0) 

# Читаем файл построчно:
for line in f:
	print(line)

f.seek(0) 
# Чтение файла целиком в список строк (включая символ конца строки)
lines = f.readlines()
print(lines)

# запись в файл списка чисел
f2 = open('text2.txt', 'w')
l = [str(i) for i in range(10)]
for i in l:
	f2.write(i+'\n')
f.close()

# чтение списка из файла
f2 = open('text2.txt', 'r')
l = [line.strip() for line in f2]
print(l)

# запись в файл списка строк
lst = [
	'Отговорила роща золотая\n', 
	'Березовым, веселым языком,\n', 
	'И журавли, печально пролетая,\n',
	'Уж не жалеют больше ни о ком.\n',
]
f2 = open('text3.txt', 'w')
f2.writelines(lst)
f.close()


# подсчитаем максимальную длину строки в файле
l = max(len(line) for line in open('text.txt') if line.strip())
print(l)

