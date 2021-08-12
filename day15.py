# # ex1
# a = (lambda x,y,z:(x*y*z))(4,5,6)
# b = ('Value of swimmingpool')
# print(a,b)

# a = eval(input('Type lenght of cube:'))
# b = (lambda a:(a*3))(a)
# print ('value:', b)

# ex2
# a = (lambda x,z: (x-z))(365,164)
# print(a,"days left until new year")

# ex3
# def rec(a):
# 	print(a)
# 	if a%2==0:
# 		return a
# 	else:
# 		rec(a+2)
# rec(2)
##method 2
# def  rec(a): 
# 	print(a)
# 	rec(a+2)
# rec(1)
# ex4
# def rec(x):
# 	print(x)  
# 	if x==set():   #esli x pustoi
# 		return x   #verni x
# 	else:
# 		x.pop()     #udalayet/vozvrawaet odin element
# 		return rec(x)  #verni rec
# a = {'sss', 'sssaa', 'dff', True, 123}  
# rec(a)
# ex5
# import random
# def aidar(s):    
# 	a = []
# 	for n in s():
# 		if n not in a:
# 			a.append(n)
# 	print(a)

# @aidar
# def inits():
# 	s = []
# 	for i in range(100):
# 		a=random.randint(10,50)
# 		s.append(a)
# 	return s

# ex6 
def lex(x):
	a = input('login:')
	b = input('password')
	x(login,password)
@lex
def fox(login,password):
	s = 0
	for i in login:
		print(s+ord(i))
		break
	for i in passord:
		print(s+ord(i))
		break
