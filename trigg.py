from math import *
from colorama import *
import os
os.system('clear') 

def Co(n):
	cosin = sqrt(1-n**2)
	return(cosin)


def Si(n):
	sinus = sqrt(1-n**2)
	return(sinus)


def Tg(n):
	cossin = (sqrt(1/(1+n**2)))
	return(cossin) 



  
choose = str(input('''
[1] - Синус
[2] - Косинус
[3] - Тангенс
: '''))# 'Эта часть кода отвечает за вопрос и вывод информатии'
	
if choose == '1':
	x = float(input('x = ?: '))
	if Co(x) == 0:
		print(Fore.RED + '| Sin: ',x,' | ')
		print(Fore.GREEN + '| Cos: ',Co(x), '|')
	else:
		print(Fore.RED+'| Sin: ',x,' | ')
		print(Fore.GREEN+'| Cos: ',Co(x), '|')
		print(Fore.BLUE+'| Tg: ',x/Co(x), '|')

elif choose == '2' :
	x = float(input('x = ?: '))
	print(Fore.RED+'| Sin: ', Si(x), '|')
	print(Fore.GREEN+'| Cos: ', x, '|')
	print(Fore.BLUE+'| Tg: ', Si(x)/(x),'|')
elif choose == '3':
	x = float(input('x = ?: '))
	print(Fore.RED+'| Sin: ',Si(Tg(x)), '|')
	print(Fore.GREEN+'| Cos:', Tg(x), '|')	
	print(Fore.BLUE+'| Tg: ',x,'|')
else:
	print("Ошибка выбора")







