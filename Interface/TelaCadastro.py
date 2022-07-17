from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("375x667")
window.configure(bg = "#d9d9d9")
canvas = Canvas(
    window,
    bg = "#d9d9d9",
    height = 667,
    width = 375,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

entry0_img = PhotoImage(file = f"Interface/imagens/cadastrar1.png")
entry0_bg = canvas.create_image(
    188.0, 236.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#f5f5f5",
    highlightthickness = 0)

entry0.place(
    x = 54.0, y = 214,
    width = 268.0,
    height = 43)

entry1_img = PhotoImage(file = f"Interface/imagens/cadastrar2.png")
entry1_bg = canvas.create_image(
    188.0, 324.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#f5f5f5",
    highlightthickness = 0)

entry1.place(
    x = 54.0, y = 302,
    width = 268.0,
    height = 43)

entry2_img = PhotoImage(file = f"Interface/imagens/cadastrar3.png")
entry2_bg = canvas.create_image(
    188.0, 408.5,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#f5f5f5",
    highlightthickness = 0)

entry2.place(
    x = 54.0, y = 386,
    width = 268.0,
    height = 43)

img0 = PhotoImage(file = f"Interface/imagens/cadastrar-button.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 110, y = 465,
    width = 155,
    height = 37)

background_img = PhotoImage(file = f"Interface/imagens/background-cadastrar.png")
background = canvas.create_image(
    202.5, 305.0,
    image=background_img)

window.resizable(False, False)
window.mainloop()
