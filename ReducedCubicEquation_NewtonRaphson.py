import math

'''
This ia simple implementation of a Newton- Raphson

'''

class ReducedCubicEquation_NewtonRaphson():
    def __init__(self, xlowcalc, xhighcal, a, p, q):
       Initialx = (xlowcalc+xhighcal)/2
      # print(Initialx)
       x=Initialx
       while True:
           y = x**3 + p*x -q(x)
           ydiff = 3*(x**2) + p
           xnew = x - (y/ydiff)
           if (abs(x - xnew) > 0.001):
              x=xnew
           else:
               self.xnew=xnew
               #print(self.xnew)
               break
            