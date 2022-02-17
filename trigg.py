
from math import *


def sintocos(n):
	cosin = sqrt(1-n**2)
	return(cosin)


def costosin(n):
	sinus = sqrt(1-n**2)
	return(sinus)


def tantocos(n):
	cossin = (sqrt(1/(1+n**2)))
	return(cossin) 


while True: 
  
	choose = str(input('''
[1] - Синус
[2] - Косинус
[3] - Тангенс
[exit] - Выход
: '''))# 'Эта часть кода отвечает за вопрос и вывод информатии'
	


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
		print('| Sin: ', costosin(x), '|')
		print('| Cos: ', x, '|')
		print('| Tg: ', costosin(x)/(x),'|')
	elif choose == '3':
		x = float(input())
		print('| Sin: ',sqrt(1-(tantocos(x)**2)))
		print('| Cos:', tantocos(x), '|')	
		print('| Tg: ',x,'|')
	elif choose == 'exit':
		break
	else:
		print("Ошибка выбора")





ch = input(''' 
В каком формате данные?
[1]
[2]
[3] ''')

if  ch == '1': # для выбора из градусов радианов и значений
	pass




