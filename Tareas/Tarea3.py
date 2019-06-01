from tkinter import ttk
from tkinter import *

class Desk:
    def __init__(self, window):
      
        
        
        ancho = 700
        
       
        alto = 500
        
      
        self.wind = window

        
        self.wind.geometry(str(ancho)+'x'+str(alto))

        
        self.wind.columnconfigure(0, weight=1)
        
        
        self.wind.title("Tercer Ejercicio")
        
       
        frame = LabelFrame(self.wind, text = "Ingrese el año")
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)
        
        
        Label(frame, text = "Primer año: ").grid(row = 1, column = 0)
        
        
        self.var1 = Entry(frame)
        self.var1.focus()
        self.var1.grid(row = 1, column = 1)
        
        
        Label(frame, text = "Segundo año: ").grid(row = 2, column = 0)
        self.var2 = Entry(frame)
        self.var2.grid(row = 2, column = 1)
        
        
        Button(frame, text = "Calcular", command = self.fun).grid(row = 3, columnspan = 2, sticky = W + E)

       
        self.message = Label(text = '', fg = 'green')
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)
        
    

    def validation(self):
        return len(self.var1.get()) != 0 and len(self.var2.get()) != 0
    

    def cero(self):
        return len(self.var1.get()) != 0 and len(self.var2.get()) != 0


    def fun(self):
        num1= int(self.var1.get())
        num2= int(self.var2.get())
          
        if self.validation():
            if num1==num2:
                self.message['text'] = "Los años son iguales, por favor, coloca distintos"
            elif(num1>num2):
                resultado=num1-num2
                self.message['text'] = "Han pasado {} años".format(resultado)
            else:
                resultado=num2-num1
                self.message['text'] = "Faltan  {} años".format(resultado)
            
        else:
            self.message['text'] = "Es necesario que todos lo campos esten llenos"              


if __name__ == '__main__':
    
    
    window = Tk()
    
 
    app = Desk(window)

    window.mainloop()