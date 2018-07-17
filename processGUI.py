
import tkinter as tk

class CustomWidget(tk.Frame):

    
    def __init__(self, parent, processName):
        tk.Frame.__init__(self, parent)
        
        self.label = tk.Label(self, text=processName, anchor="n")
        self.entry = tk.Entry(self)

        self.label.pack(side="top", fill="x")
        self.entry.pack(side="bottom", fill="x", padx=4)


    def bind(self, event, callback):
        self.label.bind(event, callback)
        self.entry.bind(event, callback)
        return
    
    def get(self):
        return self.entry.get()
