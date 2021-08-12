'''
def itc(*args):
	print(args)
itc(4,10,23,'MARIO')
'''
''' 
def lead(**kwargs):
	print(kwargs)
lead(team = 123, les = 'gogo', velnus = "ganja")
'''
def team(name,*bek):
	print(f'name:{name}')
	for i in bek:
			print(i)
team('Nura',100, 'Baldej')

def gro(old,**water):
	print(f'age:{old}')
	for name,phone in water.items(): #items prohodit po indeksu
		print(f'{name}:{phone}')
gro(21,fish='balyk',num= +996555064949)