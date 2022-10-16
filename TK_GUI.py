from math import *
from tkinter import *
from tkinter import ttk



def mathematics(choose, x):

	def Co(n):
		cos = sqrt(1-n**2)
		return(cos)


	def Si(n):
		sin = sqrt(1-n**2)
		return(sin)


	def Tg(n):
		tg = (sqrt(1/(1+n**2)))
		return(tg) 


		
	if choose == "sin":
		if Co(x) == 0:
			sin = x
			cos = Co(x)
			return [sin, cos]
		else:
			sin = x
			cos = Co(x)
			tg = x/Co(x)
			return [sin,cos,tg]

	elif choose == "cos" :
		sin =  Si(x)
		cos = x
		tg = Si(x)/(x)
		return [sin,cos,tg]
	elif choose == "tg":
		sin = Si(Tg(x))
		cos = Tg(x)
		tg = x
		return [sin,cos,tg]




def clicked():
	result = []
	result = mathematics(combox.get(), txt.get())
	print(txt.get())
	print(result)	
	













window = Tk()
window.geometry("300x100")
window.grid()
window.resizable(0,0)

strg = 'something'

combox = ttk.Combobox(text=strg)
combox['values'] = ('Sin','Con','Tg')

combox.state(["readonly"])
combox.grid(column=1, row=0)


lbl = Label(window, text="Number")
lbl.grid(column=0, row=3)


txt = Entry(window,width=10)
txt.grid(column=1, row=3)



btn = Button(window, text="Calculate", command=clicked)
btn.grid(column=1, row=4)
window.mainloop()















