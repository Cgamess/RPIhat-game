import reagons as rg
try:
  import sense_hat as sho
  sh=sho.Sensehat()
except:
  import sense_emu as sho
  sh=sho.SenseHat()

class BaseEntityModel(rg.Map):
    def __init__(self):
        self.hp = 100
        self.dead = False
        self.anibuffer=[]
        self.color = [0, 0, 0]
        self.x, self.y, self.z, self.world = 0, 0, 0, 0
        self.tx, self.ty, self.tz = 0, 0, 0
        self.mx, self.my, self.mz = 0, 0, 0
        self.lcolor = [0, 0, 0]
        self.lx, self.ly, self.lz, self.lworld = 0, 0, 0, 0
        self.ltx, self.lty, self.ltz = 0, 0, 0
        self.lmx, self.lmy, self.lmz = 0, 0, 0
        

    def render(self):
        global tmap,change
        if not tmap:
          tmap=[]
          for i in range(64):
            tmap.append([0,0,0])
        if [self.mx, self.my, self.mz, self.world] == [super().cmx, super().cmy, super().cmz, super().cworld]:
            sh.set_pixel(self.x,self.y,self.color) and not [self.x, self.y, self.z, self.world, self.mx, self.my, self.mz] == [self.lx, self.ly, self.lz, self.lworld, self.lmx, self.lmy, self.lmz]:
            if not change:
              sh.set_pixel(self.lx,self.ly,tmap[self.lx+(self.ly*8)])
