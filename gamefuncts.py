from sense_hat import SenseHat as s
import creaturebase as cb
import functs, time
import functs as f
import math
import random as r
import re
import reagons as rg
import logo
import imports
import threading as th
try:
  import sense_hat as sho
  sh=sho.Sensehat()
except:
  import sense_emu as sho
  sh=sho.SenseHat()
tlim=0
fpsm=120

def mtt(current_position, target_position, range_threshold=0):
    try:
      x, y = current_position
      target_x, target_y = target_position
      
      # Check if the current position is within the range_threshold of the target position
      if abs(x - target_x) <= range_threshold: pass
      else:
          if x < target_x and abs(x - target_x) > range_threshold:
              x += 1
          elif x > target_x and abs(x - target_x) > range_threshold:
              x -= 1
      if abs(x - target_x) <= range_threshold: pass
      else:
          if y < target_y and abs(y - target_y) > range_threshold:
              y += 1
          elif y > target_y and abs(y - target_y) > range_threshold:
              y -= 1
    except AttributeError as e: print(e)
    
    return x,y
def createseq(lenl):
    a = list(range(lenl))
    for i in range(len(a)):
        a[i]+=1
    return a
def creatempty(lenl,value=None):
    a = list(range(lenl))
    for i in range(len(a)):
        a[i]=value
    return a
def createalt(lenl, valuelist=[]):
    a = []
    for i in range(lenl):
        a.extend(valuelist)
    return a
def makealtani(loops,wait,alts,lenl=1):
    a=[]
    for i in range(loops):
        for j in createalt(lenl,alts):
            a.append(creatempty(wait,j))
    b=[]
    for i in a:
        b.extend(i)
    return(b)

class Player(cb.BaseEntityModel):
    def __init__(self):
        super().__init__()
        self.color = [255, 255, 255]
    def move(self,way=[0,0]):
      if 0:
        self.x=r.randint(-1,1)+self.x
        self.y=r.randint(-1,1)+self.y
      else:
        if way:
          self.x=+way[0]
          self.y=+way[1]
    def render(self):
        if [self.mx, self.my, self.mz, self.world] == [super().cmx, super().cmy, super().cmz, super().cworld]:
            sh.set_pixel(self.x,self.y,self.color)

class Goblin(cb.BaseEntityModel):
    def __init__(self):
        super().__init__()
        self.color = [0, 255, 0]
        self.x = r.randint(0,7)
        self.y = r.randint(0,7)
        def render(self):
            super().render()
    def move(self):
      for i in range(r.randint(0,int(math.ceil(len(goblins)/4)))):
          if 3 == r.randint(3,4):
            self.x, self.y = mtt([player.x, player.y], [self.x, self.y], 1)
    def spawn(amount=1):
      for i in range(amount):
        goblins.append(Goblin())
    def set_amount(amount=1):
      if len(goblins) > amount:
        goblins.pop(slice(((goblins-amount)-1),((amount)-1)))
      elif amount==len(goblins): pass
      else:
        for i in range(amount-len(goblins)):
          goblins.append(Goblin())
    def RenderAll():
      for i in goblins:
        if i.hp > 0:
          i.render()
    def MoveAll():
      for i in goblins:
        if i.hp > 0:
          if r.randint(0,1):
            i.move()
goblins=[]
player = Player()
Goblin.spawn(8)

def md():
  player.move([0,0])
def rd():
  player.move([1,0])
def dd():
  player.move([0,-1])
def ud():
  player.move([0,1])
def ld():
  player.move([-1,0])

sh.stick.direction_middle = md
sh.stick.direction_right = rd
sh.stick.direction_down = dd
sh.stick.direction_up = ud
sh.stick.direction_left = ld

def tick():
  if 0: Goblin.spawn(1)
  global oldmap,map,gamma
  if 0: sh.clear()
  map = (player.world,f.utils.clamp(player.tx,rg.xmap[0],rg.xmap[1]),f.utils.clamp(player.ty,rg.ymap[0],rg.ymap[1]),0)

  if map in rg.map:
    tmap = rg.map[map]
    for i in range(len(tmap)):
        for j in range(len(tmap[i])):
          tmap[i][j]=int(tmap[i][j])
    sh.set_pixels(tmap)
    oldmap=map
    if map in [(0,0,0,0),(0,0,1,0)]:
      s.gamma = [31] * 32
      gamma = [31] * 32
    else:
      s.gamma = [31] * 32
      gamma = [31] * 32
  else:
    tmap = rg.map[oldmap]
    for i in range(len(tmap)):
        for j in range(len(tmap[i])):
          tmap[i][j]=int(tmap[i][j])
    sh.set_pixels()
  if tlim: time.sleep(1/(fpsm*3))
  Goblin.RenderAll()
  Goblin.MoveAll()
  if tlim: time.sleep(1/(fpsm*3))
  if 0: print(len(goblins))
  if player.hp >= 0:
    player.render()
    player.move()
  if tlim: time.sleep(1/(fpsm*3))
