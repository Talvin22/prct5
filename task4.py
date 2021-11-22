first = input('Введите первый список: ')
second = input('Введите второй список')
first = first.split()
second = second.split()

num = set(first)&set(second)

if num:
	print('True')
else:
	print("False")