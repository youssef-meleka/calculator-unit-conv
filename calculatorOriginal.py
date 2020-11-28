from tkinter import *
from math import *
import math 

def button_click(number,e):
	#e.delete(0, END)
	current = e.get()
	e.delete(0, END)
	e.insert(0, str(current) + str(number))

def button_clear(e):
	e.delete(0, END)

def button_add(e):
	first_number = e.get()
	global f_num
	global math
	math = "addition"
	f_num = float(first_number)
	e.delete(0, END)
	return

def button_equal(e):
	second_number = e.get()
	e.delete(0, END)
	
	if math == "addition":
		e.insert(0, f_num + int(second_number))

	if math == "subtraction":
		e.insert(0, f_num - int(second_number))

	if math == "multiplication":
		e.insert(0, f_num * int(second_number))

	if math == "division":
		e.insert(0, f_num / int(second_number))

	if math == "cosine":
		print(cos(f_num))
			
	if math == "sine":
		e.insert(0, sin(f_num))

	if math == "tangent":
		e.insert(0, tan(f_num))

	if math == "inverse":
		e.insert(0, float(1/(f_num)))    

	if math == "logarithm":
		e.insert(0, log(float(f_num)))

	if math == "logarithm e":
		e.insert(0, log(f_num, 2.718281))
	
	if math == "x power 2":
		e.insert(0,f_num **2)

	if math == "x power 3":
		e.insert(0,f_num **3)	

	if math == "x power y":
		e.insert(0,f_num **int(second_number))

	if math == "e power x":
		e.insert(0, (2.718281)**f_num)	

def button_subtract(e):
	first_number = e.get()
	global f_num
	global math
	math = "subtraction"
	f_num = float(first_number)
	e.delete(0, END)

def button_multiply(e):
	first_number = e.get()
	global f_num
	global math
	math = "multiplication"
	f_num = float(first_number)
	e.delete(0, END)

def button_divide(e):
	first_number = e.get()
	global f_num
	global math
	math = "division"
	f_num = float(first_number)
	e.delete(0, END)

def button_cos(e):
	first_number = e.get()
	global f_num
	global math
	math = "cosine"
	f_num = float(first_number)
	e.delete(0, END)
	e.insert(0, float(cos(f_num)))

def button_sin(e):
	first_number = e.get()
	global f_num
	global math
	math = "sine"
	f_num = float(first_number)
	e.delete(0, END)
	e.insert(0, float(sin(f_num)))

def button_tan(e):
	first_number = e.get()
	global f_num
	global math
	math = "tangent"
	f_num = float(first_number)
	e.delete(0, END)
	e.insert(0, float(tan(f_num)))

def button_inverse(e):
	first_number = e.get()
	global f_num
	global math
	math = "inverse"
	f_num = float(first_number)
	e.delete(0, END)
	e.insert(0, float(1/(f_num)))

def button_log(e):	
	first_number = e.get()
	global f_num
	global math
	math = "logarithm"
	f_num = float(first_number)
	e.delete(0, END)
	e.insert(0, log(float(f_num)))

def button_ln(e): 	
	first_number = e.get()
	global f_num
	global math
	math = "logarithm e"
	f_num = float(first_number)
	e.delete(0, END)
	e.insert(0, log(f_num,2.718281))

def button_power2(e):
	first_num = e.get()
	global f_num
	global math
	math = "x power 2"
	f_num = float(first_num)
	e.delete(0, END)
	e.insert(0, f_num**2)

def button_power3(e):
	first_num = e.get()
	global f_num
	global math
	math = "x power 3"
	f_num = float(first_num)
	e.delete(0, END)
	e.insert(0, f_num**3)

def button_power(e):
	first_num = e.get()
	global f_num
	global math
	math = "x power y"
	f_num = float(first_num)
	e.delete(0, END)

def button_e_power_x(e):
	first_number = e.get()
	global f_num
	global math
	math = "e power x"
	f_num = float(first_number)
	e.delete(0, END)
	e.insert(0, (2.718281)**f_num)


############################################### MAIN Function ###############################################
def Calculator_main():
	root = Tk()
	e = Entry(root, width=45, borderwidth=10)
	root.title("Simple Calculator")
	e.grid(row=0, column=0, columnspan=7, padx=20, pady=10)

	# design of Buttons

	button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1,e))
	button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2,e))
	button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3,e))
	button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4,e))
	button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5,e))
	button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6,e))
	button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7,e))
	button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8,e))
	button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9,e))
	button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0,e))
	
	btn_add = Button(root, text="+", padx=39, pady=20, command=lambda:button_add(e))
	btn_equal = Button(root, text="=", padx=89, pady=20, command=lambda:button_equal(e))
	btn_clear = Button(root, text="Clear", padx=80, pady=20, command=lambda:button_clear(e))

	btn_subtract = Button(root, text="-", padx=41, pady=20, command=lambda:button_subtract(e))
	btn_multiply = Button(root, text="*", padx=40, pady=20, command=lambda:button_multiply(e))
	btn_divide = Button(root, text="/", padx=41, pady=20, command=lambda:button_divide(e))

	btn_cos = Button(root, text="cos", padx=40, pady=20, command=lambda:button_cos(e))
	btn_sin = Button(root, text="sin", padx=41, pady=20, command=lambda:button_sin(e))
	btn_tan = Button(root, text="tan", padx=41, pady=20, command=lambda:button_tan(e))

	btn_inverse = Button(root, text="1/x", padx=41, pady=20, command=lambda:button_inverse(e))

	btn_log = Button(root, text="log", padx=41, pady=20, command=lambda:button_log(e))
	btn_ln = Button(root, text="ln", padx=45, pady=20, command=lambda:button_ln(e))

	btn_power2 = Button(root, text="x^2", padx=45, pady=20, command=lambda:button_power2(e))
	btn_power3 = Button(root, text="x^3", padx=45, pady=20, command=lambda:button_power3(e))
	btn_power = Button(root, text="x^y", padx=45, pady=20, command=lambda:button_power(e))

	btn_pi = Button(root, text="Pi", padx=50, pady=20, command=lambda: button_click(math.pi,e))
	btn_e = Button(root, text="e", padx=53, pady=20, command=lambda: button_click(math.e,e))
	btn_e_power_x = Button(root, text="e^x", padx=48, pady=20, command=lambda:button_e_power_x(e))


	# Put the buttons on the screen

	button_1.grid(row=3, column=0)
	button_2.grid(row=3, column=1)
	button_3.grid(row=3, column=2)

	button_4.grid(row=2, column=0)
	button_5.grid(row=2, column=1)
	button_6.grid(row=2, column=2)

	button_7.grid(row=1, column=0)
	button_8.grid(row=1, column=1)
	button_9.grid(row=1, column=2)

	button_0.grid(row=4, column=0)
	btn_clear.grid(row=4, column=1, columnspan=2)
	btn_add.grid(row=5, column=0)
	btn_equal.grid(row=5, column=1, columnspan=2)

	btn_subtract.grid(row=6, column=0)
	btn_multiply.grid(row=6, column=1)
	btn_divide.grid(row=6, column=2)

	btn_cos.grid(row=1, column=3)
	btn_sin.grid(row=2, column=3)
	btn_tan.grid(row=3, column=3)

	btn_inverse.grid(row=4, column=3)

	btn_log.grid(row=5, column=3)
	btn_ln.grid(row=6, column=3)

	btn_power2.grid(row=1, column=4)
	btn_power3.grid(row=2, column=4)
	btn_power.grid(row=3, column=4)

	btn_pi.grid(row=4, column=4)
	btn_e.grid(row=5, column=4)
	btn_e_power_x.grid(row=6, column=4)


	root.resizable(False,False)
	root.mainloop()	


Calculator_main()
