import math

'''
This program returns a negarive number which python has problems with when exponential values are taken i.e it gives complex values


'''

class ReducedCubicEquation_InitialGuess():

    def __init__(self, A, p, q):
        x=A
        print('This is p', p)
        print('This is q', q)
        while True:
            y= x**3 + p*x - q
            #print('This is y', y)
            if y> 0:
                LowValueY, xlow = self.CalculateLowValue(y,A,p,q) 
               # print('This is LowValuey', LowValueY)
                self.xlow=xlow
                self.xhigh=1
                break
            elif y<0:
                HighValueY, xhigh = self.CalculateHighValue(y,A,p,q) 
               # print('This is highValuey', HighValueY)
                self.xlow=1
                self.xhigh= xhigh *-1
                break;
        #print(self.xlow, self.xhigh)
        
    def CalculateLowValue(self, ylow, A1, p1, q1):
        x1=A1
        while True:
            ylow= x1**3 + p1*x1 - q1
            #print('This is ylow', ylow)
            if ylow> 0:
                x1=x1/2
                #print(x1)
            else:
                break
                
        return(ylow, x1);
    
    def CalculateHighValue(self, yhigh, A2, p2, q2):
        x2=A2
        while True:
            yhigh= x2**3 + p2*x2 - q2
          #  print('This is yhigh', yhigh)
            if yhigh < 0:
                x2=x2+10
                #print(x2)
            else:
                break
                
        return(yhigh, x2);
    
    def fmomentumLoss(self, temp, Ttarget = 5, n=1.5):
          Tnorm = t/Ttarget
          if Tnorm >= 1:
              return 1
          else:
              return Tnorm**temp   
    
       