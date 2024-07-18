from ReducedCubicEquation_InitialGuess import ReducedCubicEquation_InitialGuess
from ReducedCubicEquation_NewtonRaphson import ReducedCubicEquation_NewtonRaphson


import math

'''
This program solves a reduced cubic eqaation as set out in Fulvio Mitellos book page 268

'''

BoltzmannConstant= 1.38 * 10**(-23)
ElectricalCharge= 1.602 * 10**(-19)
#NumberDensitySOLMid =  10**19
#ParallelHeatFlux = 5 * 10**6
MassDeuterium = 3.3435 * 10**(-27)
Gamma = 7.5 
#TokamakMajorRadius = 9 # This is a very large tokamak
#TokamakSafetyFactor = 3 # This is a large safety factor
ElectronParallelConductivityCoefficient=2000 # Common value that is used




class Calculation_Numeric():


    def __init__(self):
        #print('Hello World')
        pass
    '''
    def fmomentumLoss(self, x):
           Ttarget =5
           n = self.momentumfactor
           #print('This is n', n)
           Tnorm = x/Ttarget
           if Tnorm >= 1:
               return 1
           else:
               return Tnorm**n 
     '''      
           
    def fmomentumLoss(self, x):
          Ttarget =1
          n = self.momentumfactor
          #print('This is n', n)
          Tnorm = x/Ttarget
          return (1-(math.exp(-Tnorm)))**n
           
    
           
    def Calculate(self, A, B, C, D, E, F, G):
        '''
        
        This function/method obtains the independent variable from a reduced cubic equation.
        The parameters for the reduced cubic equation are a, p and q i,e ax**3 + px + q 
        These are the values obtained by calculation in the first part of the method below
        '''
        #print('HelloAgain')
        try:
            NumberDensitySOLMid = A # not sure why you have to use *args for this to work
            ParallelHeatFlux = B # not sure why you have to use *args for this to work
            fpowerLoss = C
            self.momentumfactor = D
            #print('This is the momentum factor', self.momentumfactor)
            fconductionLoss = E
            TokamakMajorRadius = F
            TokamakSafetyFactor = G
            ConnectionLength =  math.pi * TokamakMajorRadius * TokamakSafetyFactor
            p = 3.5 * ParallelHeatFlux * ConnectionLength *fconductionLoss /ElectronParallelConductivityCoefficient
           # print(p)
            Beta = math.sqrt(2)* ElectricalCharge**(3.0/2)/math.sqrt(MassDeuterium)
           # print(Beta)
            q = lambda x: (2*ParallelHeatFlux*fpowerLoss/(Beta* NumberDensitySOLMid * self.fmomentumLoss((x**(4.0/7)))))**(7.0/2)
            from scipy.optimize import fsolve
            tosolve = lambda x: x**3 + p*x - q(x)
            #print(q)
            self.TemperatureTarget = fsolve(tosolve,1**(7.0/4))**(4.0/7)
            #self.TemperatureTarget = fsolve(tosolve,x0=1)
            print(self.TemperatureTarget)
            '''
            a=1
            M= ReducedCubicEquation_InitialGuess(a,p,q(5**(7.0/4)))
            # The initial guess just involves coming up with a high and low value so we have bounds to apply the Newton Raphson
           # print('This is the reduced')
            #print(M.xlow)
            #print(M.xhigh)
            
            xlowhere= abs(M.xlow)
            xhighhere= abs(M.xhigh)
            
            P= ReducedCubicEquation_NewtonRaphson(xlowhere, xhighhere, a,p,q)
            self.TemperatureTarget = (P.xnew)**(4.0/7)
            
            
            '''
            TemperatureMidPontFirstPart = self.TemperatureTarget**(7.0/2) + p
            
            self.TemperatureMidPoint =  TemperatureMidPontFirstPart**(2.0/7)
            
            #print(self.TemperatureTarget) 
            #print(self.TemperatureMidPoint)
            self.NumberDensityTarget= self.fmomentumLoss(self.TemperatureTarget)*NumberDensitySOLMid * self.TemperatureMidPoint/(2 *  self.TemperatureTarget)
          
            #self.NumberDensityTarget=  NumberDensitySOLMid * self.TemperatureMidPoint/(2 * self.TemperatureTarget)
            self.SOLMidPointPressure = NumberDensitySOLMid * self.TemperatureMidPoint
            self.FluxAtTarget = self.NumberDensityTarget*math.sqrt(self.TemperatureTarget)* math.sqrt(2*ElectricalCharge/MassDeuterium)/self.SOLMidPointPressure
            
            self.TargetPressure = 2* self.NumberDensityTarget * self.TemperatureTarget
            
           
           # NumberDensityAtTarget.set(NumberDensityTarget)
           # print(self.NumberDensityTarget)
        except ValueError:
            pass
    
#app = Calculation_Numeric()
#app.Calculate(10**20, 10**7, 0.1,1,1,3,4 ) 
#print(app.TemperatureTarget) 
