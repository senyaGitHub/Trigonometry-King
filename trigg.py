from math import *


def sintocos(n):
	cosin = sqrt(1-n**2)
	return(cosin)


def costosin(n):
	sinus = sqrt(1-n**2)
	return(sinus)


choose = input(''' 
[1] - Синус
[2] - Косинус
: ''')
x = float(input())
if choose == 1:
	print(sintocos(x))
else:
	print(costosin(x))	

