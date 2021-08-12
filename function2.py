a = ("all,any,abs,min,max,eval,reversed,round,slice")
y = input('введите фунцию')
try:
	for i in a:
		if y in a:
			print('est funkciya')
	else:
	    print('net funkcii')
except IndexError:
	print("error")
