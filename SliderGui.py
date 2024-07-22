# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

from matplotlib.ticker import  (MultipleLocator, AutoMinorLocator)
from matplotlib.ticker import FormatStrFormatter

from Calculation_Numeric import Calculation_Numeric

'''
This is the class that produces all the pretty plots. 
It takes the values obtained from the InitialGui program which insubstatiates it and uses these to fill various 4 x 4 matrices through passing values calculated by the
GetValues method. 

We end up with six 4 x 4 matrices, TempAtSolMidPointMatrix,  NumberDensityAtTargetMatrix, etc which are used to plot the lines in the plots on the three graphs, 2 plots for the first
graph, 2 plots for the second and 3 plots for the third. One of the plots is reproduced across the plots.

The matices have a row vector based on three variables, PowerLoss, ConductionLoss and MomentumLoss. So we have a row vector of 90 points which corresponds to the 11 possible values of the 
variables P0werLoss, ConductionLoss and MomentumLoss. There are therefore 11^3 possible 90 row vectors.

The use of the sliders identifies the number for the 1 to 11 for the PowerLoss, 1 to 11 for the ConductionLoss and 1 to 11 for the MomenturmLoss.
The RowVector values [90 values] are the values that are used to plot the line

This class insubstatiates the Calculation_Numeric class which is a front-end for the solver where a reduced cubic equation is solved. This provides a set of values based on different x values.

We have chosen to populate all the values in the 4 x 4 grid. It may have been quicker to calculate the values of the Row Vectors on the fly.



'''


class SliderGui():
    
    def __init__(self):
        pass
    #initialise an empty Slider Gui object 
      
    
    def GetValues(self, pp,gg, dd,ee,ff, hh, ii):
        self.TempAtTarget=0.0; # set dummy initial values
        self.TempAtSolMidPoint=0.0 # set dummy initial values
        self.NumberDensityAtTarget=0.0 # set dummy initial values
        try:
             #print('This is p', pp)
             NumberDensitySOLMid = pp # not sure why you have to use *args for this to work
             self.ParallelHeatFlux = gg # not sure why you have to use *args for this to work
             TokamakMajorRadius = hh
             TokamakSafetyFactor =ii
             fmol =dd
             fmomentum = ee
             fconduction = ff
             #self.ClickedItem = self.r.get() # get a numeric values back which is what we test for in the 'if' block below and in the 'showGraph' function 
            # print('This is clicked item', self.ClickedItem)
            # if self.ClickedItem ==1:
             P= Calculation_Numeric() # insubstantiate the numberic front-end
             #We then use the Calculate function within the object to 
             P.Calculate(NumberDensitySOLMid, self.ParallelHeatFlux, fmol, fmomentum, fconduction, TokamakMajorRadius, TokamakSafetyFactor) # use the calculate function present in all solvers
             #print('This is the temperature at the target', P.TemperatureTarget)
             self.TempAtTarget= P.TemperatureTarget #make the results available for the rest of the program
             
             self.TempAtSolMidPoint = P.TemperatureMidPoint #make the results available for the rest of the program
             self.NumberDensityAtTarget = P.NumberDensityTarget
             self.FluxAtTarget = P.FluxAtTarget #make the results available for the rest of the program
             self.TargetPressure = P.TargetPressure
             self.SolMidPointPressure = P.SOLMidPointPressure
        except ValueError:
         pass
    
    def runplot(self, p, g, h, i):
        
        
        
       
        TempAtTargetMatrix = np.zeros(shape=(11,11,11,90))
        '''
        This is a hypercube - a 4d matrix. we should read the shape parameter as (m,z,y,x)
        In our case we create a 90 value x rowvector 
        see code below:
             for m in np.arange(1, 10, 0.1):
        This is our density parameter which forms our x axis on the grid
        We then see how the variables n, q, and r  which are PowerLoss, MomentumLoss and ConductionLoss affect our densities and temperatures
        at the SOL mid point and at the target
        Hence all the different Matrices
        We put in the x rows all in one block - we use a RowVector - see just below.
        '''
        TempAtSolMidPointMatrix = np.zeros(shape=(11,11,11,90))
        NumberDensityAtTargetMatrix = np.zeros(shape=(11,11,11,90))
        FluxAtTargetMatrix = np.zeros(shape=(11,11,11,90))
        PressureAtSolMidPointMatrix = np.zeros(shape=(11,11,11,90))
        PressureAtTargetMatrix = np.zeros(shape=(11,11,11,90))
        TempAtTargetRowVector=[]
        TempAtSolMidPointRowVector = []
        NumberDensityAtTargetRowVector = []
        NumberDensityAtSOLMidPointVector=[]
        FluxAtTargetRowVector = []
        PressureAtSolMidPointRowVector = []
        PressureAtTargetRowVector = []
        
        
        
     
        # Create subplot
        fig, (ax1,ax2,ax3) = plt.subplots(3) # Create the plot on the figure with 3 subplots
        ax4= ax3.twinx()
        plt.subplots_adjust(bottom=0.25, hspace=0.55)# We use hspace to ensure there is enough space between the three plots.
       
        t = np.arange(1, 10, 0.1)
        for r in np.arange(1,12,1):
            for q in np.arange(1,12,1):
                for n in np.arange(1,12,1):
                    for m in np.arange(1, 10, 0.1):
                        #print('This is t',m)
                        self.GetValues(p*m, g, n/10, q/2, r/10, h, i)
                        #print('This is the temperature at the target', self.TempAtTarget)
                        #print('This is t', t)
                        #print('This is n', n)
                        #print('This is m', m)
                        TempAtTargetRowVector.append(self.TempAtTarget)
                        FluxAtTargetRowVector.append(self.FluxAtTarget)
                        PressureAtSolMidPointRowVector.append(self.SolMidPointPressure)
                        PressureAtTargetRowVector.append(self.TargetPressure)
                        TempAtSolMidPointRowVector.append(self.TempAtSolMidPoint)
                        NumberDensityAtTargetRowVector.append(self.NumberDensityAtTarget)
                        NumberDensityAtSOLMidPointVector.append(p*m)
                        #print('This is the length of s', len(TempAtTargetRowVector))
                        #print('This is s',TempAtTargetRowVector)
               # t = np.linspace(int(p), int(1e20), 0.1)
                    #print('This in the counter n', n)
                    TempAtTargetMatrix[r-1][q-1][n-1] = np.squeeze(np.array(TempAtTargetRowVector))
                    TempAtSolMidPointMatrix[r-1][q-1][n-1]= np.squeeze(np.array(TempAtSolMidPointRowVector))
                    NumberDensityAtTargetMatrix[r-1][q-1][n-1]= np.squeeze(np.array(NumberDensityAtTargetRowVector))
                    FluxAtTargetMatrix[r-1][q-1][n-1] = np.squeeze(np.array(FluxAtTargetRowVector))
                    PressureAtSolMidPointMatrix[r-1][q-1][n-1] = np.squeeze(np.array(PressureAtSolMidPointRowVector))
                    PressureAtTargetMatrix [r-1][q-1][n-1] = np.squeeze(np.array(PressureAtTargetRowVector))
                    TempAtTargetRowVector=[]
                    TempAtSolMidPointRowVector=[]
                    NumberDensityAtTargetRowVector=[]
                    FluxAtTargetRowVector = []
                    PressureAtSolMidPointRowVector = []
                    PressureAtTargetRowVector = []
                    NumberDensityAtSOLShow = NumberDensityAtSOLMidPointVector 
                    NumberDensityAtSOLMidPointVector=[]
            #print('This is t', t)
            #print('This is TempAtTargetMatrix[n-1]', TempAtTargetMatrix[n-1])
        l, = ax1.plot(t, TempAtTargetMatrix[r-1][q-1][n-1]) # This is where we plot the values
        ll,= ax1.plot(t, TempAtSolMidPointMatrix[r-1][q-1][n-1]) # This is where we plot the values
        z, = ax2.plot(t, NumberDensityAtTargetMatrix[r-1][q-1][n-1]) # This is where we plot the values
        #print('This is the NumberDensityAtSOLShow', NumberDensityAtSOLShow)  
        zz, = ax2.plot(t, NumberDensityAtSOLShow) # This is where we plot the values 
        rr, = ax3.plot(t, FluxAtTargetMatrix[r-1][q-1][n-1]) # This is where we plot the values
        rrr,= ax4.plot(t, PressureAtSolMidPointMatrix[r-1][q-1][n-1], color = 'red') # This is where we plot the values
        rrrr,= ax4.plot(t, PressureAtTargetMatrix[r-1][q-1][n-1], color = 'green') # This is where we plot the values
          
            # Create axes for frequency and amplitude sliders
        axPowerLoss = plt.axes([0.25, 0.15, 0.65, 0.03]) # This is where we set the axes up relative to the other axes
        axMomentumLoss = plt.axes([0.25, 0.1, 0.65, 0.03])
        axConductionLoss = plt.axes([0.25, 0.05, 0.65, 0.03]) 
           
            # Create a slider from 0.0 to 1 in axes axPowerLoss
        PowerLoss = Slider(ax = axPowerLoss,label= 'PowerLoss', valmin= 0.0, valmax = 1.0, valinit =0, valstep=0.1)
             
            # Create a slider from 0.0 to 5.5 in axes axMomentumLoss
        MomentumLoss = Slider(ax = axMomentumLoss,label= 'MomentumLoss', valmin= 0.5, valmax = 5.5, valinit =0.5, valstep=0.5)
             
        ConductionLoss = Slider(ax = axConductionLoss,label= 'ConductionLoss', valmin= 0.0, valmax = 1.0, valinit =0, valstep=0.1)
        
        # Do the labelling
           
        ax1.set_xlabel(f'Electron Number Density at SOL Mid-point starting at {p} #/m$^3$')
        ax1.set_ylabel("Temp \n in eV", rotation=0, ha = 'right', va = 'center')
        ax1.set_title('SOL and Target Temperature vs SOL Mid-point Electron density ramp', fontweight='bold', size=10)
        ax1.legend((l, ll), ('Target Temperature', 'SOL Mid Point Temperature'))
        
        ax2.set_xlabel(f'Electron Number Density at SOL Mid-point starting at {p} #/m$^3$')
        ax2.set_ylabel("Electron Number \n Density \n in #/$m^3$", rotation=0, ha = 'right', va = 'center')
        ax2.set_title('SOL and Target Electron Density vs SOL Mid-point Electron density ramp' , fontweight='bold', size=10)
        ax2.legend((z, zz), ('Target Electron Density', 'SOL Mid-point Electron Density'))
        
        
        
        ax3.set_xlabel(f'Electron Number Density at SOL Mid-point starting at {p} #/m$^3$')
        ax3.set_ylabel('ELectron Flux \n in particles /m$^2$ \n normalised \n to target pressure', rotation=0, ha = 'right', va = 'center')
        ax3.set_title('Electron Flux at the Target', fontweight='bold', size=10)
        ax3.legend((rr, rrr, rrrr), ('Target Electron Flux', 'Sol Mid-point Pressure', 'Target Pressure'))
        
        
       
            # Create function to be called when slider value is changed
            
        def autoscale_y(ax,margin=0.1):
            """This function rescales the y-axis based on the data that is visible given the current xlim of the axis.
            ax -- a matplotlib axes object
            margin -- the fraction of the total height of the y-data to pad the upper and lower ylims"""
        
        
            def get_bottom_top(line):
                xd = line.get_xdata()
                yd = line.get_ydata()
                lo,hi = ax.get_xlim()
                y_displayed = yd[((xd>lo) & (xd<hi))]
                h = np.max(y_displayed) - np.min(y_displayed)
                bot = np.min(y_displayed)-margin*h
                top = np.max(y_displayed)+margin*h
                return bot,top
        
            lines = ax.get_lines()
            bot,top = np.inf, -np.inf
        
            for line in lines:
                new_bot, new_top = get_bottom_top(line)
                if new_bot < bot: bot = new_bot
                if new_top > top: top = new_top
        
            ax.set_ylim(bot,top)
         
        def update(val):
            # This is the function that updates the graphs based on where the sliders are
            # Get the values from the slider
            f = PowerLoss.val
            h = MomentumLoss.val
            i = ConductionLoss.val
            a=0
            b=0
            c=0
            #print('This is the fmol value', PowerLoss.val, MomentumLoss.val)
            # This is a if structure for the PowerLoss slider
            if f==0:
                a= n-1
            elif f==0.1:
                 a = n-2
            elif f==0.2:
                 a= n-3  
            elif round(f,3) ==0.3:
                 a= n-4
            elif round(f,4) ==0.4:
                 a= n-5
            elif round(f,5) ==0.5:
                 a=n-6
            elif round(f,6) ==0.6:
                 a=n-7
            elif round(f,7) ==0.7:
                 a=n-8
            elif round(f,8) ==0.8:
                 a=n-9
            elif round(f,9) ==0.9:
                 a=n-10
            elif f ==1.0:
                 a=n-11
                 
            # This is a if structure for the MomentumLoss slider
            
            if  round(h,3) == 0.5:
                    b = q-1    
            elif  round(h,3) == 1.0:
                    b = q-2
            elif round(h,3) == 1.5:
                    b = q-3 
            elif round(h,3) == 2.0:
                    b = q-4
            elif round(h,3) == 2.5:
                    b = q-5  
            elif round(h,3) == 3.0: 
                    b = q-6 
            elif round(h,3) == 3.5:
                    b = q-7 
            elif round(h,3) == 4.0:
                    b = q-8         
            elif round(h,3) == 4.5:
                    b = q-9  
            elif round(h,3) == 5.0:
                    b = q-10 
            elif round(h,3) == 5.5:
                    b = q-11 
                    
            # This is a if structure for the ConductionLoss slider
            
            
            if  round(i,3) == 0:
                    c = r-1    
            elif  round(i,3) == 0.1:
                    c = r-2
            elif round(i,3) == 0.2:
                    c = r-3 
            elif round(i,3) == 0.3:
                    c = r-4
            elif round(i,3) == 0.4:
                    c = r-5  
            elif round(i,3) == 0.5:
                    c = r-6 
            elif round(i,3) == 0.6:
                    c = r-7 
            elif round(i,3) == 0.7:
                    c = r-8         
            elif round(i,3) == 0.8:
                    c = r-9  
            elif round(i,3) == 0.9:
                    c = r-10 
            elif round(i,3) == 1.0:
                    c = r-11 
                    
            
            # Get the line values          
            l.set_ydata(TempAtTargetMatrix[c][b][a])        
            ll.set_ydata(TempAtSolMidPointMatrix[c][b][a])
            z.set_ydata(NumberDensityAtTargetMatrix[c][b][a])
            rr.set_ydata(FluxAtTargetMatrix[c][b][a]) 
            rrr.set_ydata(PressureAtSolMidPointMatrix[c][b][a])
            rrrr.set_ydata(PressureAtTargetMatrix[c][b][a])
            # Scale the y axis 
            autoscale_y(ax1)
            autoscale_y(ax2)
            autoscale_y(ax3)
            autoscale_y(ax4) 
            # Call update function when slider value is changed
        #Update the graphs
        PowerLoss.on_changed(update)
        MomentumLoss.on_changed(update)
        ConductionLoss.on_changed(update)
        
        
        # set the grid size for the axes    
        ax1.xaxis.set_major_locator(MultipleLocator(1))
        ax1.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
        ax1.xaxis.set_minor_locator(MultipleLocator(1))

        ax1.yaxis.set_major_locator(MultipleLocator(10))
        ax1.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
        ax1.yaxis.set_minor_locator(MultipleLocator(5))

        ax1.grid(which='both')
        #ax1.grid()
        
        
        ax2.xaxis.set_major_locator(MultipleLocator(1))
        ax2.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
        ax2.xaxis.set_minor_locator(MultipleLocator(1))
        '''
        ax2.yaxis.set_major_locator(MultipleLocator(1))
        ax2.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
        ax2.yaxis.set_minor_locator(MultipleLocator(0.5))
        '''
       
        ax2.grid(which='both')
        
        ax3.xaxis.set_major_locator(MultipleLocator(1))
        ax3.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
        ax3.xaxis.set_minor_locator(MultipleLocator(1))
        '''
        ax3.yaxis.set_major_locator(MultipleLocator(10))
        ax3.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
        ax3.yaxis.set_minor_locator(MultipleLocator(5))
        '''
       
        ax3.grid(which='both')
        plt.show()
    
   
    
#app = SliderGui()
#app.runplot()
