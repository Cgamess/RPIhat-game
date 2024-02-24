import logo, functs, time
import reagons as rg
import gamefuncts as gf
from gamefuncts import tick
if 0: logo.logofade()
while True:
  daypoint=int((time.time()%86400)//21600)
  start_time = time.time()
  tick()
  print("FPS: ", 1.0 / (time.time() - start_time), len(gf.goblins), daypoint) # FPS = 1 / time to process loop
