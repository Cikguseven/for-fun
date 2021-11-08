# Recursive function to generate multiples of integer

def f(n):
	if n == 1:
		return 3
	else:
		return f(n-1) + 3

for i in range(1, 10):
	print(f(i))