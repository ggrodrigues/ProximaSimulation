import time
import threading 
from Station import Station
from GUI import Janela

class Base:


    leadTime = 'colocacao'
    currentTime = time.clock()
    startTime = 0
    elapsedTime = 0
    subscribers = []
    connectionMatrix = []
    stop = False
    pause = True
    nextProcess = 0
    
    

    
    def playClick(self):
        print("playClicked")
        if self.pause == False:
            self.pause = True
        else:
            self.currentTime = time.clock()
            self.pause = False
        return
        
    def addClick(self):
        
        s = Station("process" + str(self.nextProcess), 2 )
        self.nextProcess = self.nextProcess + 1
        self.subscribe(s)
        print("addClicked")
        return
        
    def newConnection(self):

        print("newConnection")
        return
            
    def mainWindowClosedClick(self):
        print("mainWindowClosedClick")
        
        self.stopNow()
        self.guiT = threading.Thread(target = self.guiClose)
        self.guiT.start()
        
        return
            
    
    eventHandler = {
        'newConnectionMade': newConnection,
        'playButtonClick' : playClick,
        'addButtonClick' : addClick,
        'mainWindowClosed' : mainWindowClosedClick
    }
    
    def onGuiEvent(self, event):
        self.eventHandler[event](self)
        return
    
    






    def tick(self):
        print("%.2f" % (self.elapsedTime))
        self.j.simuTimeText["text"] = '%.1f s'  % (self.elapsedTime)
        for s in self.subscribers:
            s.tick()
            self.j.updateProcess(s)
        return
            
















    def run(self):
        self.startTime = time.clock()
       
        while self.stop == False:
            if self.pause == False:
                if time.clock() - self.currentTime >= 0.1:
                   self.elapsedTime = self.elapsedTime +(time.clock() - self.currentTime)
                   self.currentTime = time.clock()
                   self.tick()
                   
        print("run thread terminating")
        return
           
           
           
               
               
               
               

    def guiOpen(self):
        self.j = Janela()
        self.j.open(self.onGuiEvent)
        
        return
    
    def guiClose(self):
        self.j.raiz.quit()
        
        return
        
        
                    
        
    
    def stopNow(self):
        self.stop = True
        return
        

    def subscribe(self,object):
        self.subscribers.append(object)
        self.j.addSubscriber(object)
        return

    def __init__(self):
        print("ok")
        self.t = threading.Thread(target = self.run)
        self.t.start()
        self.guiT = threading.Thread(target = self.guiOpen)
        self.guiT.start()
        return
        
            
        


