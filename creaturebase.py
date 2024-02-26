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

    def render(self):
        if [self.mx, self.my, self.mz, self.world] == [super().cmx, super().cmy, super().cmz, super().cworld]:
            sh.set_pixel(self.x,self.y,self.color)
