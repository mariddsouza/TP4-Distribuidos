from tkinter import *


def btn_clicked():
    print("Button Clicked")

window = Tk()

window.geometry("375x667")
window.configure(bg = "#fdc605")
canvas = Canvas(
    window,
    bg = "#fdc605",
    height = 667,
    width = 375,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"Interface/imagens/background.png")
background = canvas.create_image(
    175.5, 304.5,
    image=background_img)

entry0_img = PhotoImage(file = f"Interface/imagens/img_textBox0.png")
entry0_bg = canvas.create_image(
    188.0, 426.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#f5f5f5",
    highlightthickness = 0)

entry0.place(
    x = 54.0, y = 404,
    width = 268.0,
    height = 43)

entry1_img = PhotoImage(file = f"Interface/imagens/img_textBox1.png")
entry1_bg = canvas.create_image(
    188.0, 517.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#f5f5f5",
    highlightthickness = 0)

entry1.place(
    x = 54.0, y = 495,
    width = 268.0,
    height = 43)

img0 = PhotoImage(file = f"Interface/imagens/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 109, y = 557,
    width = 155,
    height = 37)

img1 = PhotoImage(file = f"Interface/imagens/img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 84, y = 619,
    width = 203,
    height = 33)

window.resizable(False, False)
window.mainloop()
