debug = 0
if 1:
  import imgshape as iss
from logo import p,P,C,B,W,O,G,R,b
try:
  from sense_hat import SenseHat
  sh=SenseHat()
except:
  from sense_emu import SenseHat
  sh=SenseHat()
class Map:
    cmx, cmy, cmz = 0, 0, 0
    cworld = 0
map={}
if 0:
  img = ""
  mp = iss.process_image(img)
  map3=mp
map2={(0,0,0,0):[
  G,G,G,B,B,G,G,G,
  G,G,G,B,B,B,G,G,
  G,G,G,G,B,B,G,G,
  G,G,G,G,B,C,B,G,
  G,G,G,G,C,B,G,G,
  G,G,G,B,B,G,G,G,
  G,G,G,G,B,C,G,G,
  G,G,G,B,B,C,G,G,
],
(0,0,1,0):[
  G,G,G,B,B,G,G,G,
  G,G,C,B,C,G,G,G,
  G,G,B,G,B,B,G,G,
  G,G,C,B,B,C,B,G,
  G,G,G,C,C,B,G,G,
  G,G,G,B,B,G,G,G,
  G,G,G,B,B,C,G,G,
  G,G,G,B,B,C,G,G,
],
(0,0,2,0):sh.load_image("river.png", redraw=False),
(0,0,3,0):sh.load_image("river2.png", redraw=False),
(1,0,4,0):[
  R,B,G,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O
],
(-1,0,4,0):[
  R,B,G,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O
]
}
map.update(map2)
try:
  map.update(map3)
except:
  pass
try:
  k = list(map.keys())
  xmappings = []
  ymappings = []
  zmappings = []
  
  for a in k:
      b = a[2]
      c = a[2]
      ymap = [b, c]
      d = a[1]
      e = a[1]
      xmap = [d, e]
      f = a[0]
      g = a[0]
      zmap = [f, g]
      ymappings.append(ymap)
      xmappings.append(xmap)
      zmappings.append(zmap)
  
  xmap = [0, 0]
  for i in xmappings:
      if i[0] < xmap[0]:
          if debug: print(i, xmap)
          xmap[0] = i[0]
      if i[1] > xmap[1]:
          if debug: print(i, xmap)
          xmap[1] = i[1]
  
  ymap = [0, 0]
  for i in ymappings:
      if i[0] <= ymap[0]:
          if debug: print(i, ymap)
          ymap[0] = i[0]
      if i[1] >= ymap[1]:
          if debug: print(i, ymap)
          ymap[1] = i[1]
  
  zmap = [0, 0]
  for i in zmappings:
      if i[0] < zmap[0]:
          if debug: print(i, zmap)
          zmap[0] = i[0]
      if i[1] >= zmap[1]:
          if debug: print(i, zmap)
          zmap[1] = i[1]
  
  if debug:print("xmap:", xmap)
  if debug:print("ymap:", ymap)
  if debug:print("zmap:", zmap)

  if 0:
    if debug:print("""
  x:"""+str(xmap)+"""
  y:"""+str(ymap)+""" 
  z:"""+str(zmap)
  )
except TypeError as e: print(e)
