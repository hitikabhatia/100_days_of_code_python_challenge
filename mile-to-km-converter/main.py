from tkinter import *
FONT = ("Arial",10,"normal")
window = Tk()
window.title("Mile to Km Converter")
window.config(padx= 20, pady= 20)

def convert_in_km():
    miles_value = float(input_miles.get())
    km_value = miles_value * 1.60934
    km_output.config(text= f"{km_value}")

#place the input entry box
input_miles = Entry()
input_miles.config(width= 10)
input_miles.grid(column = 1, row = 0)
input_miles.focus()

#labels
miles_word =Label(text= "Miles", font= FONT)
miles_word.config(padx= 20, pady= 10)
miles_word.grid(row = 0, column = 2)

is_equal_to_word = Label(text= "is equal to", font= FONT)
is_equal_to_word.grid(row = 1, column = 0)

km_output = Label(text= 0, font= FONT)
km_output.grid(row = 1, column = 1)

km_word = Label(text= "Km", font= FONT)
km_word.grid(row = 1, column = 2)

#Button
calculate_button = Button(text= "Calculate", font= FONT, command= convert_in_km)
calculate_button.grid(row = 2, column = 1)


window.mainloop()