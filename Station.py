import time
class Station:
    
    cycleTime = 1
    currentCycleTime = 0
    lastTick = 0
   


    def tick(self):
        self.elapsed = time.clock() - self.lastTick
        self.currentCycleTime = self.elapsed + self.currentCycleTime
        if self.currentCycleTime >= self.cycleTime:
            self.currentCycleTime = 0
            
        #print ("%.2f" % self.currentCycleTime)
        self.lastTick = time.clock()
        
    def __init__(self, cycleTime):
        print('oi')
        self.cycleTime = cycleTime
        self.lastTick = time.clock()