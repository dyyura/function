a = ("Razakov 32", 10, 1005, ["tables", "chairs"], 23.00)
b = []
for i in a:
	try:
		set(i)
		b.append(True)
	except TypeError:
		b.append(False)
print(b(all))


