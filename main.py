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
			tg = 0
		else:
			sin = x
			cos = Co(x)
			tg = x/Co(x)

	if choose == "cos":
		sin =  Si(x)
		cos = x
		tg = Si(x)/(x)
	
	if choose == "tg":
		sin = Si(Tg(x))
		cos = Tg(x)
		tg = x
	return sin,cos,tg



def clicked():
	result = list(mathematics(combox.get(), float(txt.get())))
	result = [round(i, 4) for i in result]
	lbl.config(text = f"Sin: {result[0]} Cos: {result[1]}, Tg: {result[2]}")
	print(result)	
	




window = Tk()
window.geometry("400x100")
window.grid()


combox = ttk.Combobox()
combox['values'] = ('sin','cos','tg')

combox.state(["readonly"])
combox.grid(column=1, row=0)

lbl = Label(window, text="Number between 0 and 1")
lbl.grid(column=0, row=3)

txt = Entry(window,width=10)
txt.grid(column=1, row=3)


btn = Button(window, text="Calculate", command=clicked)
btn.grid(column=1, row=4)
window.mainloop()















