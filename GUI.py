from tkinter import *
from PIL import Image, ImageTk
from processGUI import CustomWidget

class Janela:   
    playing = FALSE
    lastEvent = ""
    
        
    def getEvent(self):
        event = self.lastEvent
        self.lastEvent = ""
        return event
       
    def open(self):
        self.raiz.mainloop()
    
    
    def playButtonPressHandler(self):
        self.lastEvent = "playButtonClick"
        if self.playing == TRUE:
            self.playButton["image"] = self.photoPause
            self.playing = FALSE
            
        else:
            self.playButton["image"] = self.photoPlay
            self.playing = TRUE
      
    def closeWindowPressHandler(self):
        print("windowClosed")
        self.lastEvent = "mainWindowClosed"
        self.raiz.destroy()
    
    def customPressHandler(self,event):
        print("customWidgetPressed")
        return
        
            
                
            
    def __init__(self):
        self.raiz = Tk()
        self.raiz.protocol("WM_DELETE_WINDOW", self.closeWindowPressHandler)
 
        self.topContainer = Frame(self.raiz,padx = 8,pady = 8,bd = 4, bg = "white")
        self.topContainer.pack()
        
        self.titleContainer = Frame(self.topContainer, padx = 0, pady = 4, bg = "white")
        self.titleContainer.pack()
        
        self.barContainer = Frame(self.topContainer, padx = 0, pady = 4, bg = "white", bd = 2)
        self.barContainer.grid_propagate(0)
        self.barContainer.pack()
        
        self.simulationContainer = Frame(self.topContainer, padx = 0, pady = 4, bg = "white", bd = 4, height = 400, width = 600)
        self.simulationContainer.pack()
        
        self.title = Label(self.titleContainer, text = 'Proxima Simulation', bg = "white")
        self.title["font"] = ("Tahoma","22")
        self.title.pack()
        
        self.simuTime = Label(self.barContainer, text = 'Simulation = ', bg = "white")
        self.simuTime["font"] = ("MS PGothic","12")
        self.simuTime.pack(side = LEFT)
       
        self.imagePlay = Image.open(r"C:\Users\rodri\Proxima Simulation\play1.jpg")
        self.imagePlay = self.imagePlay.resize((20,20), Image.ANTIALIAS)
        self.photoPlay = ImageTk.PhotoImage(self.imagePlay)
        self.imagePause = Image.open(r"C:\Users\rodri\Proxima Simulation\pause.jpg")
        self.imagePause = self.imagePause.resize((20,20), Image.ANTIALIAS)
        self.photoPause = ImageTk.PhotoImage(self.imagePause)
        
        self.playButton = Button(self.barContainer,image = self.photoPlay ,command=self.playButtonPressHandler, bg = "white", height = 20, width = 20, compound = LEFT)
        
        self.playButton.pack(side = RIGHT)
        
        
        self.simuTimeText = Label(self.barContainer, text = '0.00', bg = "white")
        self.simuTimeText["font"] = ("MS PGothic","12")
        self.simuTimeText.pack(side = RIGHT)
        
        self.custom = CustomWidget(self.simulationContainer, "Process 1")
        self.custom.bind("<Button-1>",self.customPressHandler)
        self.custom.place(x = 200, y = 200)
        
j = Janela()
j.open()
