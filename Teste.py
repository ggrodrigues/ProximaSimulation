import tkinter
import time
from Base import Base
from Station import Station
from GUI import Janela


x = Base()


s = Station(2)
x.subscribe(s)

s2 = Station(5)
x.subscribe(s2)

#time.sleep(100)
#x.stopNow()




