
from tkinter import *
import tkinter as tk


from TelaLogin import FunctionTelaLogin

def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("375x667")
window.configure(bg = "#d9d9d9")
window.title = ('Tela Inicial')

canvas = Canvas(
    window,
    bg = "#d9d9d9",
    height = 667,
    width = 375,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"imagens/background.png")
background = canvas.create_image(
    256.0, 324.5,
    image=background_img)

img0 = PhotoImage(file = f"imagens/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    #command = btn_clicked, 
    command = FunctionTelaLogin(self),
    relief = "flat")

b0.place(
    x = 110, y = 435,
    width = 155,
    height = 37)

window.resizable(False, False)
window.mainloop()
