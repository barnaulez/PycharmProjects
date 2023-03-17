import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="Label", font=("Arial", 16))
my_label.pack()

def button_clicked():
    label_text = input.get()
    my_label.config(text = label_text)

button = tkinter.Button(text="Click me", command=button_clicked)
button.pack()

input = tkinter.Entry(width=10)
input.pack()





window.mainloop()