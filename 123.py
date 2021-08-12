# zadainie 1
'''
list_1 = ['name','age','1','19']
def half2():
		for i in range(len(list_1)):
			if i % 2 == 0:
				list_1[i], list_1[i + 1] = list_1[i + 1], list_1[i]
		print(list_1)
half2()		

def half3():
    a = input().split()
    print((list(reversed(a[:(int(len(a)) // 2)]))) 
    + (list(reversed(a[(int(len(a)) // 2)::]))))
half3()
'''
#  zadanie 2
'''
a = eval(input('Введите конечное число Фибонначи: '))

def fib(n):
  a, b = 0, 1
  for i in range(n):
    yield a
    a, b = b, a + b
print(list(fib(a)))
''' 
# zadanie 3
def kunk(a = 3, b = 6):
  return a + b
print(kunk(b = 4, a = 5))
kunk()
def batr(a = 6, b = 1):
  return a - b
print(batr(b = 4, a = 33))
batr()
def gero(l = 4, s = 4):
  return kunk and batr 
print(kunk(a= 3,b = 6),batr(b = 32,a = 40))
gero()