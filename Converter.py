import tkinter as tk
from tkinter import *
from tkinter import ttk
from math import *
import math 



def length_convert(length_comboBox_1,length_comboBox_2,length_input,length_output):
		
		from_unit = length_comboBox_1.get()
		to_unit = length_comboBox_2.get()
		
		input_val = float(length_input.get())

		result = 0 
		## logic 
		if from_unit == 'm':
				if to_unit == 'm':
						result = input_val
				elif to_unit == 'cm':
							result = input_val * 100.0
				elif to_unit == 'mm':
						result = input_val * 1000.0
		
		elif from_unit == 'cm':
				if to_unit == 'm':
						result = input_val / 100.0
				elif to_unit == 'cm':
						result = input_val
				elif to_unit == 'mm':
						result = input_val * 10.0
		
		elif from_unit == 'mm':
				if to_unit == 'm':
						result = input_val / 1000.0
				elif to_unit == 'cm':
						result = input_val / 10.0
				elif to_unit == 'mm':
						result = input_val 


		## display result
		length_output.delete(0, END)
		length_output.insert(0, str(result))


		return


def temperature_convert(temperature_comboBox_1,temperature_comboBox_2,temperature_input,temperature_output):
		from_unit = temperature_comboBox_1.get()
		to_unit = temperature_comboBox_2.get()
		
		input_val = float(temperature_input.get())

		result = 0 
		## logic 
		if from_unit == 'feh':
				if to_unit == 'feh':
					result = input_val
				elif to_unit == 'cel':
					result = (input_val- 32) * 5.0 / 9.0
				elif to_unit == 'kel':
					result = (input_val- 32) * 5.0 / 9.0 + 273.15
		
		if from_unit == 'cel':
				if to_unit == 'feh':
					result = (input_val * 9.0 / 5) + 32.0
				elif to_unit == 'cel':
					result = input_val
				elif to_unit == 'kel':
					result = input_val +  273.15
		
		if from_unit == 'kel':
				if to_unit == 'feh':
					result = input_val - 459.67
				elif to_unit == 'cel':
					result = input_val - 273.15
				elif to_unit == 'kel':
					result = input_val


		## display result
		temperature_output.delete(0, END)
		temperature_output.insert(0, str(result))

		return


################## MAIN FUNCTION ##################

def Converter_main():
	root = Tk()
	root.title("Converter")


	### design of Buttons

	## LENGTH part
	length_label = tk.Label(root, text = "LENGTH")

	length_comboBox_1 = ttk.Combobox(root, values=[ "m", "cm","mm"])
	to_label = tk.Label(root, text = "to")
	length_comboBox_2 = ttk.Combobox(root, values=[ "m", "cm","mm"])

	length_input   = Entry(root)
	# length_output  = Entry(root, state='disabled')
	length_output  = Entry(root)

	length_convert_btn = Button(root, text="Convert", command=lambda:length_convert(length_comboBox_1,length_comboBox_2,length_input,length_output ))

	# Put the buttons on the screen
	length_label.grid(row=0, column=0, columnspan=7, padx=20, pady=10)
	length_comboBox_1.grid(row=1, column=0)
	to_label.grid(row=1, column=1)
	length_comboBox_2.grid(row=1, column=2)
	length_input.grid(row=3, column=0)
	length_output.grid(row=3, column=2)
	length_convert_btn.grid(row=2,column =3)



	## Temperature part
	temperature_label = tk.Label(root, text = "TEMPERATURE")

	temperature_comboBox_1 = ttk.Combobox(root, values=[ "feh", "cel","kel"])
	to_label_2 = tk.Label(root, text = "to")
	temperature_comboBox_2 = ttk.Combobox(root, values=[ "feh", "cel","kel"])

	temperature_input   = Entry(root)
	temperature_output  = Entry(root)

	temperature_convert_btn = Button(root, text="Convert", command=lambda:temperature_convert(temperature_comboBox_1,temperature_comboBox_2,temperature_input,temperature_output))

	# Put the buttons on the screen
	temperature_label.grid(row=4, column=0, columnspan=7, padx=20, pady=10)
	temperature_comboBox_1.grid(row=5, column=0)
	to_label_2.grid(row=5, column=1)
	temperature_comboBox_2.grid(row=5, column=2)
	temperature_input.grid(row=7, column=0)
	temperature_output.grid(row=7, column=2)
	temperature_convert_btn.grid(row=6,column =3)


	root.geometry("400x300") 

	root.resizable(False,False)
	root.mainloop()


Converter_main()