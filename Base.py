import time
import threading 
from GUI import Janela

class Base:


    leadTime = 'colocacao'
    currentTime = time.clock()
    startTime = 0
    elapsedTime = 0
    subscribers = []
    connectionMatrix = []
    stop = False
    pause = False
    
    
    def playClick(self):
        print("playClicked")
        if self.pause == False:
            self.pause = True
        else:
            self.currentTime = time.clock()
            self.pause = False
        return
            
    def mainWindowClosedClick(self):
        print("mainWindowClosedClick")
        
        self.stopNow()
        self.guiT = threading.Thread(target = self.guiClose)
        self.guiT.start()
        
        return
            
    def frameClick(self):
        print("frameClicked")
    
    eventHandler = {
        'playButtonClick' : playClick,
        'frameClick' : frameClick,
        'mainWindowClosed' : mainWindowClosedClick
    }
    
    
    






    def tick(self):
        print("%.2f" % (self.elapsedTime))
        
        for s in self.subscribers:
            s.tick()
        return
            
















    def run(self):
        self.startTime = time.clock()
       
        while self.stop == False:
            if self.pause == False:
                if time.clock() - self.currentTime >= 0.05:
                   self.elapsedTime = self.elapsedTime +(time.clock() - self.currentTime)
                   self.currentTime = time.clock()
                   
                   self.tick()
                   
            if hasattr(self, 'j'):
                self.j.simuTimeText["text"] = '%.1f s'  % (self.elapsedTime)
                event = self.j.getEvent()
                if bool(event):
                    if event in self.eventHandler:
                        self.eventHandler[event](self)
        print("run thread terminating")
        return
           
           
           
               
               
               
               

    def guiOpen(self):
        self.j = Janela()
        self.j.open()
        
        return
    
    def guiClose(self):
        self.j.raiz.quit()
        
        return
        
        
                    
        
    
    def stopNow(self):
        self.stop = True
        return
        

    def subscribe(self,object):
        self.subscribers.append(object)
        return

    def __init__(self):
        print("ok")
        self.t = threading.Thread(target = self.run)
        self.t.start()
        self.guiT = threading.Thread(target = self.guiOpen)
        self.guiT.start()
        return
        
            
        


