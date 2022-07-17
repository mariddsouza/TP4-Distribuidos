from tkinter import *
import tkinter as tk


def btn_clicked():
    print("Button Clicked")


def FunctionTelaLogin(self):
    window2 = Tk()

    window2.geometry("375x667")
    window2.configure(bg = "#d9d9d9")
    canvas = Canvas(
        window2,
        bg = "#d9d9d9",
        height = 667,
        width = 375,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)



    entry0_img = tk.PhotoImage(file = f"imagens/img_textBox0.png")
    self.entry0_bg = canvas.create_image(
        184.0, 245.5,
        image = entry0_img)

    entry0 = Entry(
        bd = 0,
        bg = "#f5f5f5",
        highlightthickness = 0)

    entry0.place(
        x = 50, y = 223,
        width = 268.0,
        height = 43)

    entry1_img = PhotoImage(file = f"imagens/img_textBox1.png")
    self.entry1_bg = canvas.create_image(
        184.0, 335.5,
        image = entry1_img)

    entry1 = Entry(
        bd = 0,
        bg = "#f5f5f5",
        highlightthickness = 0)

    entry1.place(
        x = 50, y = 313,
        width = 268.0,
        height = 43)

    img0 = PhotoImage(file = f"imagens/acessar.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b0.place(
        x = 105, y = 380,
        width = 155,
        height = 37)

    img1 = PhotoImage(file = f"imagens/img1-login.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b1.place(
        x = 80, y = 475,
        width = 206,
        height = 28)

    background_img = PhotoImage(file = f"background-login.png")
    self.background = canvas.create_image(
        202.5, 307.0,
        image=background_img)

  
