
from itertools import chain


def fibbo(n):
	if(n<2):
		return n
	else:
		return fibbo(n-1)+fibbo(n-2)
hello = 123
def greeting(abc):
	print(abc+1)

greeting(hello)
ca = {}
cal = 0
def fibo(n):
	global cal
	cal = cal +1
	if n in ca:
		return ca[n]
	if(n<2):
		return n
	else:
		ca[n] = fibo(n-1)+fibo(n-2)
		return ca[n]

print(fibo(100))
print(ca)
print(cal)
