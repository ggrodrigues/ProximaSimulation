
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

class CustomWidget(tk.Frame):
    
    currentInput = 0
    currentOutput = 0
    
    def updateInput(self,event):
        
        print(event.widget)
        self.currentInput = self.currentInput + 10
        if self.currentInput > 100: 
            self.currentInput = 0
        self.inputLine.delete("inputStatus")
        self.inputLine.create_rectangle(0,42 - ((self.currentInput/100)*42),20, 42,fill = "#76ff03", tag = "inputStatus")
        self.inputLine.tag_lower("inputStatus")
        print("done")
        return
    def updateOutput(self,event):
        
        print(event.widget)
        self.currentOutput = self.currentOutput + 10
        if self.currentOutput > 100: 
            self.currentOutput = 0
        self.outputLine.delete("outputStatus")
        self.outputLine.create_rectangle(0,42 - ((self.currentOutput/100)*42),20, 42,fill = "#76ff03", tag = "outputStatus")
        self.outputLine.tag_lower("outputStatus")
        print("done")
        return
    
    def __init__(self, parent, processName):
        tk.Frame.__init__(self, parent)
        self.config(borderwidth = 3, relief = RAISED, padx = -10, pady = -10)
        self.label = tk.Label(self, text=processName)
        self.tickWidget = tk.Label(self, text = "0.0")
        self.inputLine = tk.Canvas(self,width = 15,height = 40,relief = RIDGE, bd = 1, bg = "white")
        self.inputLine.bind("<Button-1>", self.updateInput)
        self.outputLine = tk.Canvas(self,width = 15,height = 40,relief = RIDGE, bd = 1, bg = "white")
        self.outputLine.bind("<Button-1>", self.updateOutput)
        self.imageInputNG = Image.open(r"C:\Users\rodri\Proxima Simulation\arrow.png")
        self.imageInputNG = self.imageInputNG.resize((15,15), Image.ANTIALIAS)
        self.photoInputNG = ImageTk.PhotoImage(self.imageInputNG)
        #print((self.inputLine.winfo_reqwidth()))
        self.inputLine.create_image(self.inputLine.winfo_reqwidth()/2,self.inputLine.winfo_reqheight()/2,image = self.photoInputNG, anchor="center")
        self.outputLine.create_image(self.inputLine.winfo_reqwidth()/2,self.inputLine.winfo_reqheight()/2,image = self.photoInputNG, anchor="center")
        
        self.label.grid(row = 0, column = 1)
        self.tickWidget.grid(row = 1, column = 1)
        self.inputLine.grid(rowspan = 2, column = 0, row = 0)
        self.outputLine.grid(rowspan = 2, column = 2, row = 0)
        

    def updateTime(self,time):
        self.tickWidget["text"] ='%.1f s'  % (time)
        return
    
    
    def bind(self, event, callback):
        self.label.bind(event, callback)
        self.tickWidget.bind(event, callback)
        return
        
        return
    
    def get(self):
        return self.tickWidget.get()

# t = Tk()

# p = CustomWidget(t, "processo")
# p.pack()
# t.mainloop()
