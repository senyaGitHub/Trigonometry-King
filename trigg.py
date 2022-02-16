
from math import *


def sintocos(n):
	cosin = sqrt(1-n**2)
	return(cosin)


def costosin(n):
	sinus = sqrt(1-n**2)
	return(sinus)

def tantocosandsin(n):
	cossin = (sqrt(1/(1+n**2)))
	return(cossin)


while True:
  
	choose = str(input(''' 
[1] - Синус
[2] - Косинус
[3] - Тангенс
[exit] - Выход
: '''))
	


	if choose == '1':
			x = float(input())
			if sintocos(x) == 0:
				print('| Sin: ',x,' | ')
				print('| Cos: ',sintocos(x), '|')
			else:
				print('| Sin: ',x,' | ')
				print('| Cos: ',sintocos(x), '|')
				print('| Tg: ',x/sintocos(x), '|')

	elif choose == '2' :
		x = float(input())
		print('| Cos: ', x, '|')
		print('| Sin: ', costosin(x), '|')
		print('| Tg: ', costosin(x)/(x),'|')
	elif choose == '3':
		x = float(input())
		print('| Tg: ',x,'|')
		print('| Cos:', tantocosandsin(x), '|')	
	elif choose == 'exit':
		break
	else:
		print("Ошибка выбора")