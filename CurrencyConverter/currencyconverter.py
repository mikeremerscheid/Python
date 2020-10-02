from tkinter import *

class CurrencyConverter:
    def __init__(self):
        window = Tk()
        window.title("Currency Converter")
        window.configure(bg="yellow")
        Lebel(window,font"Helvetica 12 bold", bg="yellow", text="Amount to convert").grid(row=1,column1,sticky =W)
        