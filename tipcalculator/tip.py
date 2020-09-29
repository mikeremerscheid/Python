from tkinter import Tk, Radiobutton, Button, Label, StringVar, IntVar, Entry

class TipCalculator():
    def __init__(self):
        window = Tk()
        window.title("Tip Calculator App")
        window.configure(background="sky blue")
        window.geometry("375x250")
        window.resizable(width=False,height=False)
        window.mainloop()

TipCalculator()
