import math

from scipy.optimize import fsolve

'''
We use a lambda function within a lambda function and then pass this to a root finding function 'fsolve'

'''


class ReducedCubicSolver():
    
    def __init__(self, momentumFactor):
        self.momentumfactor = momentumFactor

    def fmomentumLoss(self, x):
          Ttarget =1
          # get the value from the init function
          n = self.momentumfactor
          #print('This is n', n)
          Tnorm = x/Ttarget
          return (1-(math.exp(-Tnorm)))**n
    

    def Solver(self, pImport,ParallelHeatFluxImport, fpowerLossImport, BetaImport, NumberDensitySOLMidImport):
           # First lambda function
            q = lambda x: (2*ParallelHeatFluxImport*fpowerLossImport/(BetaImport* NumberDensitySOLMidImport * self.fmomentumLoss((x**(4.0/7)))))**(7.0/2)
           # second lambda function embedded in the first
            tosolve = lambda x: x**3 + pImport*x - q(x)
            # 1 as initial value of x and make value available to rest of program
            self.Solved = fsolve(tosolve,1**(7.0/4))**(4.0/7)
            #print(q)