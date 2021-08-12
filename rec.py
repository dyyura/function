# def rec(a):
# 	print(a)
# 	rec(a+1)
# rec(1)

# def rec(x):
# 	if x<10:
# 		print(x)
# 		rec(x+1)
# rec(1)

# import sys
# print(sys.getrecursionlimit())

# def itc(a):
# 	if a <= 1:
# 		return 1
# 	else:
# 		return a * itc(a-1)
# c = itc(int(input('write something:')))
# itc(c)

# def rem(a,b):
# 	print(a+b)
# rem(10,5)

# a = (lambda x,b:(x+b))(34,54)
# print(a)

def ok(x):                     
	def lev():
		print('start...')
		print('stop...')
		x()
	return lev

def kkk(v):
	def lol():
		print('jjj')
		v()
		return lol
@kkk
@ok 
def les():
	print('step...')
les()