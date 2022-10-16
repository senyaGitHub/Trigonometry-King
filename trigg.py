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
___       _                                      _ 
 |  __ o (_| _ __  _ __  _ _|_ __ \/   |/  o __ (_|
 |  |  | __|(_)| |(_)|||(/_ |_ |  /    |\  | | |__|

[1] - Sin?
[2] - Cos?
[3] - Tg?
: '''))# 'Эта часть кода отвечает за вопрос и вывод информатии'



if choose == '1' :
	while True:
		try:
			x = float(input('x = ?: '))
			if Co(x) == 0:
				print(Fore.RED + '| Sin: ',x,' | ')
				print(Fore.GREEN + '| Cos: ',Co(x), '|')
			else:
				print(Fore.RED+'| Sin: ',x,' | ')
				print(Fore.GREEN+'| Cos: ',Co(x), '|')
				print(Fore.BLUE+'| Tg: ',x/Co(x), '|')
			break
		except ValueError:
			print (Back.RED+"Вы должны ввести число, и/или оно должно быть в диапозоне (0;1).")
			print(Style.RESET_ALL)


		

elif choose == '2' :
	while True:
		try:
			x = float(input('x = ?: '))
			if x == 0:
				print(Fore.RED+'| Sin: ', Si(x), '|')
				print(Fore.GREEN+'| Cos: ', x, '|')

			else:
				print(Fore.RED+'| Sin: ', Si(x), '|')
				print(Fore.GREEN+'| Cos: ', x, '|')
				print(Fore.BLUE+'| Tg: ', Si(x)/(x),'|')
				break
		except ValueError:
			print (Back.RED+"Вы должны ввести число,и/или оно должно быть в диапозоне (0;1).")	
			print(Style.RESET_ALL)	

elif choose == '3' :
	while True:
		try:
			x = float(input('x = ?: '))
			print(Fore.RED+'| Sin: ',Si(Tg(x)), '|')
			print(Fore.GREEN+'| Cos:', Tg(x), '|')	
			print(Fore.BLUE+'| Tg: ',x,'|')
			break
		except ValueError:
			print (Back.RED+"Вы должны ввести число.")	
			print(Style.RESET_ALL)	
else:
	print("Ошибка выбора, введите число от 1 до 3 чтобы выбрать значение.")







