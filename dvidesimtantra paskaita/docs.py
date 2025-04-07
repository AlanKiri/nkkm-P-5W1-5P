import tkinter as tk
from tkinter import messagebox

# Langas
window = tk.Tk()
window.title('Pavadinimas')
# Plotis, aukstis
window.geometry('400x1000')

# exit
# window.quit()
# window.destroy()

# Komponentai

# label = tk.Label(window, text='Mano tekstas', pady=5)
# label.pack()

# kintamasis = 'test'

# def button_click():
#     print(kintamasis)

# button = tk.Button(window, text='Paspausk', command=button_click, pady=5)
# button.pack()

# entry = tk.Entry(window)
# entry.pack()

# text= tk.Text(window, height=5, width=40)
# text.pack()

# checkbox = tk.Checkbutton(window, text='Noriu')
# checkbox.pack()

# radio = tk.Radiobutton(window, text='1', value=1)
# radio.pack()

# listbox = tk.Listbox(window)
# listbox.pack()

# scale = tk.Scale(window, from_=0, to=100, orient='horizontal')
# scale.pack()

# canvas = tk.Canvas(window, width=200, height=200)
# canvas.pack()
# canvas.create_line(0,0, 200, 200)

# label1= tk.Label(text='tekstas1')
# label2= tk.Label(text='tekstas2')
# label3= tk.Label(text='tekstas3')
# label4= tk.Label(text='tekstas4')
# label5= tk.Label(text='tekstas5')
# label6= tk.Label(text='tekstas6')

# Row -> vertikaliai, column -> horizontaliai

# label1.grid(column=0, row=0)
# label2.grid(column=0, row=1)
# label3.grid(column=0, row=2)
# label4.grid(column=0, row=3)
# label5.grid(column=0, row=4)
# label6.grid(column=0, row=5)

# testlabel = tk.Label(text='tektas')
# testlabel.place(x=100, y=100)

# def on_click():
#     messagebox.showinfo('Title', 'Noriu susipazinti')

# message_button = tk.Button(text='message', command=on_click)
# message_button.grid(column=0, row=6)

text_var = tk.StringVar()
entry = tk.Entry(window, textvariable=text_var)
entry.pack()

def on_click():
    messagebox.showinfo('Title', text_var.get())

message_button = tk.Button(text='show content', command=on_click)
message_button.pack()

















window.mainloop()