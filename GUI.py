from tkinter import *
from PIL import Image, ImageTk
from processGUI import CustomWidget
import math

class Janela:   
    playing = FALSE
    lastEvent = ""
    dragCustom = False
    subscribers = []
    
    def getEvent(self):
        event = self.lastEvent
        self.lastEvent = ""
        return event
       
    def open(self, callback):
        self.callback = callback
        self.raiz.mainloop()
        return
    
    
    def playButtonPressHandler(self):
        self.callback("playButtonClick")
        if self.playing == FALSE:
            self.playButton["image"] = self.photoPause
            self.playing = TRUE
        else:
            self.playButton["image"] = self.photoPlay
            self.playing = FALSE
        return
    
    def addButtonPressHandler(self):
        self.callback("addButtonClick")
        
        return
      
    def closeWindowPressHandler(self):
        self.callback("mainWindowClosed")
        
    
    def mouseMotionHandler(self,event):
        self.mousePos = [event.x,event.y]
        return
    
    def customLetGoHandler(self,event):  
        
        parentName = event.widget.winfo_parent()
        parent = self.raiz.nametowidget(parentName)
        currentMousePos = [parent.winfo_pointerx(), parent.winfo_pointery()]
        error = [-self.startMousePos[0] + currentMousePos[0], -self.startMousePos[1] +currentMousePos[1]]
        squarePos = self.simulationContainer.bbox("dislocationRec")
        parent.place(x = squarePos[0], y = squarePos[1])
        self.simulationContainer.delete("dislocationRec")
        

        return
    
    def customHoldHandler(self,event):  
        parentName = event.widget.winfo_parent()
        parent = self.raiz.nametowidget(parentName)
        currentMousePos = [parent.winfo_pointerx(), parent.winfo_pointery()]
        error = [-self.startMousePos[0] + currentMousePos[0], -self.startMousePos[1] +currentMousePos[1]]
        #self.simulationContainer.coords("dislocationRec",    self.startCustomPos[0]+error[0]     ,self.startCustomPos[1]+error[1]           ,self.startCustomPos[0]+error[0]+parent.winfo_width(), self.startCustomPos[1]+error[1]+parent.winfo_height())
        for i in self.inputs:
           if len(self.inputs) > 1 and i != [self.startCustomPos[0],self.startCustomPos[1] + parent.winfo_height()/2]:
                parentOutput = [self.startCustomPos[0]+error[0]+ parent.winfo_width() ,self.startCustomPos[1]+error[1]  + parent.winfo_height()/2]
                if (math.hypot(i[0]-parentOutput[0],i[1]-parentOutput[1])) < 15:
                    print(math.hypot(i[0]-parentOutput[0],i[1]-parentOutput[1]))
                    print("close enough")
                    self.simulationContainer.coords("dislocationRec", (i[0] - parent.winfo_width() , (i[1] - parent.winfo_height()/2 )+1, i[0], i[1] + parent.winfo_height()/2 ))
                else:
                    self.simulationContainer.coords("dislocationRec",    self.startCustomPos[0]+error[0]     ,self.startCustomPos[1]+error[1]           ,self.startCustomPos[0]+error[0]+parent.winfo_width(), self.startCustomPos[1]+error[1]+parent.winfo_height())
           elif len(self.inputs) == 1:
                self.simulationContainer.coords("dislocationRec",    self.startCustomPos[0]+error[0]     ,self.startCustomPos[1]+error[1]           ,self.startCustomPos[0]+error[0]+parent.winfo_width(), self.startCustomPos[1]+error[1]+parent.winfo_height())
                    
           #print(i)
           #print(self.startCustomPos[0],self.startCustomPos[1] + parent.winfo_height()/2)
            
        
        #for o in self.outputs:
            #print(o)
            #print(self.startCustomPos[0]+ parent.winfo_width() ,self.startCustomPos[1] + parent.winfo_height()/2)
        
        #parent.place(x = self.startCustomPos[0]+error[0], y =self.startCustomPos[1]+error[1])
        

        return
        
        
    def customPressHandler(self,event):
        self.inputs = []
        self.outputs = []
        for w in self.simulationContainer.children:
            widget = self.simulationContainer.nametowidget(w)
            self.inputs.append([widget.winfo_x(),widget.winfo_y()+widget.winfo_height()/2])
            self.outputs.append([widget.winfo_x()+widget.winfo_width(),widget.winfo_y()+widget.winfo_height()/2])
        print(self.inputs)
        print(self.outputs)
        parentName = event.widget.winfo_parent()
        parent = self.raiz.nametowidget(parentName)
        self.startMousePos = [parent.winfo_pointerx(), parent.winfo_pointery()]
        self.startCustomPos = [parent.winfo_x(), parent.winfo_y()]
        self.simulationContainer.create_rectangle(parent.winfo_x(),parent.winfo_y(), parent.winfo_x()+parent.winfo_width(), parent.winfo_y()+parent.winfo_height(),fill = "#29b6f6",stipple = "gray75", width = 2,outline = "gray", tag = "dislocationRec")
        self.simulationContainer.tag_raise("dislocationRec")
        parent.place(x = 500,y = 500)
        return
    
    def updateProcess(self,object):
        for x in self.subscribers:
            if x.label.cget("text") == object.name:
                x.updateTime(object.currentCycleTime)
                break
        return
        
        
            
    def addSubscriber(self,object):
        widget = CustomWidget(self.simulationContainer,object.name)
        widget.place(x = 200,y = 200)
        widget.bind("<B1-Motion>",self.customHoldHandler)
        widget.bind("<Button-1>",self.customPressHandler)
        widget.bind("<ButtonRelease-1>",self.customLetGoHandler)
        self.subscribers.append(widget)
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
        
        self.simulationContainer = Canvas(self.topContainer, bg = "white", highlightthickness=3, highlightcolor = "blue", height = 400, width = 600)
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
        
        self.imageAdd = Image.open(r"C:\Users\rodri\Proxima Simulation\add.jpg")
        self.imageAdd = self.imageAdd.resize((20,20), Image.ANTIALIAS)
        self.photoAdd = ImageTk.PhotoImage(self.imageAdd)
        self.addButton = Button(self.barContainer,image = self.photoAdd ,command=self.addButtonPressHandler, bg = "white", height = 20, width = 20, compound = LEFT)
        self.addButton.pack(side = RIGHT)
       
        
        self.simuTimeText = Label(self.barContainer, text = '0.00', bg = "white")
        self.simuTimeText["font"] = ("MS PGothic","12")
        self.simuTimeText.pack(side = RIGHT)
        
        

#j = Janela()
#j.open()