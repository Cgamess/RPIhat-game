import random as r
import imports
import threading as th
try:
  from sense_hat import SenseHat as s
except:
  from sense_emu import SenseHat as s
import time, math, numpy, operator, string, re
global message
try:
  open("t.log","x")
except:
  print()
msg=open("t.log","r")
message = False
timet = time.time()
try:
  from sense_hat import SenseHat as sh
except:
  from sense_emu import SenseHat as sh
def logofade(smoothness=0xf,speed=2,sense=True,out=False):
  if sense:
    try:
      from sense_hat import SenseHat
    except:
      from sense_emu import SenseHat
  import time
  if sense:
    s = SenseHat()
    s.low_light = False
  global clamp
  def clamp(value, minimum, maximum):
      if value < minimum:
          return minimum
      elif value > maximum:
          return maximum
      else:
          return value
          
  global raspi_logo
  def raspi_logo(a=0):
      global p,C,G,R,O,B,W,P,Y,b
      m = 256
      green = [clamp(0 + a, 0, 255), clamp(255 + a, 0, 255), clamp(0 + a, 0, 255)]
      yellow = [clamp(255 + a, 0, 255), clamp(255 + a, 0, 255), clamp(0 + a, 0, 255)]
      cyan = [clamp(0 + a, 0, 255), clamp(255 + a, 0, 255), clamp(255 + a, 0, 255)]
      purple = [clamp(255 + a, 0, 255), clamp(0 + a, 0, 255), clamp(255 + a, 0, 255)]
      blue = [clamp(0 + a, 0, 255), clamp(0 + a, 0, 255), clamp(255 + a, 0, 255)]
      red = [clamp(255 + a, 0, 255), clamp(0 + a, 0, 255), clamp(0 + a, 0, 255)]
      white = [clamp(255 + a, 0, 255), clamp(255 + a, 0, 255), clamp(255 + a, 0, 255)]
      nothing = [clamp(0 + a, 0, 255), clamp(0 + a, 0, 255), clamp(0 + a, 0, 255)]
      pink = [clamp(255 + a, 0, 255), clamp(105 + a, 0, 255), clamp(166 + a, 0, 255)]
      p = purple
      C = cyan
      G = green
      R = red
      O = nothing
      b = nothing
      B = blue
      W = white
      P = pink
      Y = yellow
      logo = [
          O, G, G, O, O, G, G, O,
          O, O, G, G, G, G, O, O,
          O, O, R, R, R, R, O, O,
          O, R, R, R, R, R, R, O,
          R, R, R, R, R, R, R, R,
          R, R, R, R, R, R, R, R,
          O, R, R, R, R, R, R, O,
          O, O, R, R, R, R, O, O,
      ]
      
      return logo
  
  amount=smoothness
  timemultiplyer=speed
  pxlist=[]
  
  for i in range(amount):
      if sense:
        s.set_pixels(list(raspi_logo(((-i/amount)*0xff)))),time.sleep((1/amount)*timemultiplyer)
      pxlist.append(list(raspi_logo(((-i/amount)*0xff))))
  if sense:
    s.clear()
  pxlist.append([[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]])
  if out:
    return(pxlist)
global clamp,raspi_logo,p,C,G,R,O,B,P,Y
if __name__ != "__main__":
  logofade(0xf,2,0,0)
  global clamp,raspi_logo,p,C,G,R,O,B,P,Y
  if message != False:
    print("Initialized in "+str(int(round(time.time()-timet)))+""" second(s)
made by 1 person over 2 days
all internal varibles and functions are global
p-purple
C-cyan
G-green
R-red
O-black
B-blue
P-pink
Y-yellow
raspi_logo-raspberry pi logo
clamp-clamps a value in a range
CASE SENSITIVE
go into the files code and change message to False to stop the message
""")
elif __name__ == "__main__":
  logofade()
  logofade(0xf,2,0,0)
  try:
    if message == True:
      message = True
  except:
    message = False
  if message != False:
    print("Initialized in "+str(int(round(time.time()-timet)))+" second(s)")
else:
  print("What?")
