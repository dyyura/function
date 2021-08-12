'''
def add(num, azat):
	return azat
print(add(10, 22))
'''

'''
def add():
	local = 10 + 9
	return local
print(add())


def subtract():
	plus = 99 - 47
	return plus
print(subtract())


def multiply():
	roar = 87 * 87
	return roar
print(multiply())

def devide():
	leu = 996 / 54
	return leu
print(devide())

#zadacha 2
'''
'''
def loan(str):
	index = 0
	for i in str:
		index += 1 
	print(index)
str = input('сколько букв в строке:')
loan(str)

def counter(a):
	c = 0
	for x in a:
		if ('a' <= x <= "z") or ('A' <= x <= 'Z') or ('а' <= x <= 'я') or ('А' <= x <= 'Я'):
			c += 1
		else:
				pass
	print(c)					
a = input("Some words:")
counter(a)
def word_sum(a):
#У меня есть функция word_sum который содержит аргумент a
    c = 0
#Указываю с какого индекса он должен начинаться
    for x in a:
#Пишу цикл чтобы мой итераттор x прошелся по всему списку который я 
#ввожу в input()
        if ('a' <= x <= 'z') or ('A' <= x <='Z') or ('а' <= x <= 'я')>
#Далее пишу условие чтобы мой элемент содержал так и с большого регис>
            c += 1
#Пишу чтобы он начинался с шага  +1
        else:
#Или же ничего не выводил
            pass
    print(c)

a = input("Введите данные:")
word_sum(a)
# zadacha 3
'''
# def lola(a,b):
# 	a.update(b)
# 	print(a)
# a = {input("brand:"): "cola"}
# b = {input("model:"): "iphone"}
# lola(a,b)

#zadacha 4
def men():
  name = input("Назовите имя файла: ")
  a = open(f'/домашняя папка/function/{name}.txt', 'a+')
  pokushat = input("Что бы вы хотели поесть : ")
  vypit = input("Что бы вы хотели поесть : ")
  a.write(pokushat)
  a.write(" ")
  a.write(vypit)
  a.close()
men()