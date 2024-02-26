try:
  import sense_hat as s
  sh=s.SenseHat()
except:
  import sense_emu as s
  sh=s.SenseHat()
import random as r
import threading as th
import time, math, numpy, operator, string, re

