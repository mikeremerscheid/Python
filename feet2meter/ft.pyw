from tkinter import Tk, Button, Label, DoubleVar, Entry

window = Tk()
window.title("Inches to Centimeters Conversion App")
window.configure(background="light green")
window.geometry("280x220")
window.resizable(width=False,height=False)

#functionality
def convert():
    value = float(in_entry.get())
    centimeter = value * 2.54
    cm_value.set("%.4f" % centimeter)
    
#functionality
def clear():
    in_value.set("")
    cm_value.set("")

#label
in_lbl = Label(window,text="Inches",bg="purple",fg="white",width=14)
in_lbl.grid(column=0,row=0,padx=14,pady=15)

#entry field
in_value = DoubleVar()
in_entry = Entry(window,textvariable=in_value,width=14)
in_entry.grid(column=1,row=0)
in_entry.delete(0,'end')

#label
cm_lbl = Label(window,text="Centimeters",bg="brown",fg="white",width=14)
cm_lbl.grid(column=0,row=1)

#entry field
cm_value = DoubleVar()
cm_entry = Entry(window,textvariable=cm_value,width=14)
cm_entry.grid(column=1,row=1,pady=30)
cm_entry.delete(0,'end')

#button
convert_btn = Button(window,text="Convert",bg="blue",fg="white",width=14,command=convert)
convert_btn.grid(column=0,row=3,padx=15)

#button
clear_btn = Button(window,text="Clear",bg="black",fg="white",width=14,command=clear)
clear_btn.grid(column=1,row=3,padx=15)

window.mainloop()
