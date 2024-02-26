import logo, functs, time
try:
  from sense_hat import SenseHat as s
  s()
except:
  from sense_emu import SenseHat as s
  s()
import threading as th
import reagons as rg
import gamefuncts as gf
from gamefuncts import tick
if __name__ == "__main__":
  if 0: logo.logofade() # Need to fix the logo function, we need to convert it a to int
  while True:
    daypoint=int((time.time()%86400)//21600)
    start_time = time.time()
    tick()
    print("FPS: ", 1.0 / (time.time() - start_time), len(gf.goblins), daypoint) # FPS = 1 / time to process loop
