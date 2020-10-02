from tkinter import * # Import whole module

class CurrencyConverter: # Create class
    def __init__(self):  #Special method in Python class
        window = Tk() # Create application window
        window.title("Currency Converter") #Add title to application window
        window.geometry("300x150")
        window.configure(bg="sky blue") #Add background color to application window
        
        
        # Adding Label widgets to application window
        Label(window,font="Helvetica 12 bold", bg="sky blue", text="Amount to convert").grid(row=1,column=1,sticky =W) 
        Label(window,font="Helvetica 12 bold", bg="sky blue", text="Conversion Rate").grid(row=2,column=1,sticky =W)
        Label(window,font="Helvetica 12 bold", bg="sky blue", text="Converted Amount").grid(row=3,column=1,sticky =W)
        
        #Create objects and add entry functions
        self.amountToConvertVar = StringVar()
        Entry(window, textvariable = self.amountToConvertVar, justify = RIGHT).grid(row=1,column=2)
        self.conversionRateVar = StringVar()
        Entry(window, textvariable = self.conversionRateVar, justify = RIGHT).grid(row=2,column=2)
        self.convertedAmountVar = StringVar()
        lblConvertedAmount = Label(window,font="Helvetica 12 bold",bg="sky blue", textvariable = self.convertedAmountVar).grid(row=3,column=2,sticky = E)
        
        
        #Create convert and clear buttons. When clicked, they will call their respective functions.
        btconverted_amount = Button(window, text  = "Convert",font="Helvetica 12 bold", bg="blue", fg="white", command = self.ConvertedAmount).grid(row=4,column=1,sticky = E)
        btdelete_all = Button(window, text="Clear", font="Helvetica 12 bold", bg="red",fg="white",command = self.delete_all).grid(row=4,column=2,padx=25,pady=25,sticky = E)
        
        window.mainloop() #Runs the application program
        
    #Function to do the conversion Stores inputs and performs conversions
    def ConvertedAmount(self):
        amt = float(self.conversionRateVar.get())
        convertedAmountVar = float(self.amountToConvertVar.get()) * amt
        self.convertedAmountVar.set(format(convertedAmountVar, '10.2f'))
        
    #Function to clear inputs
    def delete_all(self):
        self.amountToConvertVar.set("")
        self.conversionRateVar.set("")
        self.convertedAmountVar.set("")
        
CurrencyConverter()
        
    
    
        