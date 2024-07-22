from ReducedCubicSolver import ReducedCubicSolver


import math

'''
This program gets the values . The Reduced CubicSolver program does all the heavy lifting as it solves the reduced cubic equation s**3 + px = q(x) = 0
'''

BoltzmannConstant= 1.38 * 10**(-23)
ElectricalCharge= 1.602 * 10**(-19)
MassDeuterium = 3.3435 * 10**(-27)
Gamma = 7.5 
ElectronParallelConductivityCoefficient=2000 # Common value that is used




class Calculation_Numeric():


    def __init__(self):
        #print('Hello World')
        pass
 
           
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
            momentumfactor = D
            #print('This is the momentum factor', self.momentumfactor)
            fconductionLoss = E
            TokamakMajorRadius = F
            TokamakSafetyFactor = G
            ConnectionLength =  math.pi * TokamakMajorRadius * TokamakSafetyFactor
            p = 3.5 * ParallelHeatFlux * ConnectionLength *fconductionLoss /ElectronParallelConductivityCoefficient
           # print(p)
            Beta = math.sqrt(2)* ElectricalCharge**(3.0/2)/math.sqrt(MassDeuterium)
           # print(Beta)
           # insubstatiate the ReducedCubicSolver class
            LocalSolver = ReducedCubicSolver(momentumfactor)
            
            # put in the values to the Solver method
           
            LocalSolver.Solver(p, ParallelHeatFlux, fpowerLoss, Beta, NumberDensitySOLMid)
            
            #print(q)
            # The solution is your temperature
            self.TemperatureTarget = LocalSolver.Solved
            #self.TemperatureTarget = fsolve(tosolve,x0=1)
            print(self.TemperatureTarget)
         
            TemperatureMidPontFirstPart = self.TemperatureTarget**(7.0/2) + p
            
            # Calculate the temperature at the mid-point
            
            self.TemperatureMidPoint =  TemperatureMidPontFirstPart**(2.0/7)
            
            #print(self.TemperatureTarget) 
            #print(self.TemperatureMidPoint)
            self.NumberDensityTarget= LocalSolver.fmomentumLoss(self.TemperatureTarget)*NumberDensitySOLMid * self.TemperatureMidPoint/(2 *  self.TemperatureTarget)
          
            #self.NumberDensityTarget=  NumberDensitySOLMid * self.TemperatureMidPoint/(2 * self.TemperatureTarget)
            self.SOLMidPointPressure = NumberDensitySOLMid * self.TemperatureMidPoint
            self.FluxAtTarget = self.NumberDensityTarget*math.sqrt(self.TemperatureTarget)* math.sqrt(2*ElectricalCharge/MassDeuterium)/self.SOLMidPointPressure
            
            self.TargetPressure = 2* self.NumberDensityTarget * self.TemperatureTarget
        
        except ValueError:
            pass
    
#app = Calculation_Numeric()
#app.Calculate(10**20, 10**7, 0.1,1,1,3,4 ) 
#print(app.TemperatureTarget) 
