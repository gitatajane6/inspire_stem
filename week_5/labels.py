from tkinter import *

window = Tk()

# Adjust size
window.geometry("500x400")

window.title("Sensors Tutorial")

temp = 20
hum = 68

lbl = Label(window, text="Temperature : {0}".format(temp))

lbl.grid(column=400, row=100)

lb2 = Label(window, text="Humidity: {0}".format(hum))

lb2.grid(column=400, row=200)

window.mainloop()