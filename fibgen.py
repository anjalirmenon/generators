def fibo():
	a = 0
	yield a
	b = 1
	yield b
	while 1:
		c = a + b
		a, b = b, c
		yield c
d = fibo() 
	
