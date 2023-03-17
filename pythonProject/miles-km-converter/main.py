from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=40, pady=20)
km = 0

def calculate():
    kms_result = float(input.get())*1.609
    kms_label.config(text=kms_result)

input = Entry(width=15)
input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(row=1, column=0)

kms_label = Label(text=km)
kms_label.grid(row=1, column=1)

kms_kms_label = Label(text="Km")
kms_kms_label.grid(row=1, column=2)

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(row=2, column=1)




window.mainloop()
