import customtkinter
import tkinterDnD
from tkinter import *

from Calculation_Numeric import Calculation_Numeric
from SliderGui import SliderGui


'''
This is the main program it sets up the initial Gui where the user is asked to input via drop-downs, the SOL Mid-point 
density and the heat flux in W/m^3
When the button 'Calculate values is clicked, the SliderGui program is insubstatiated and from this the plots are produced.
'''

class InitialGui(customtkinter.CTk):
    
    def button_callback(self):
        #print("Button click", self.optionmenu_1.get())
        #print("Button click", self.optionmenu_2.get())
        p = float(self.optionmenu_1.get());
        g = float(self.optionmenu_2.get().replace(',', ''));
        h = float(self.entry.get())
        i = float(self.optionmenu_3.get());
        print('This is p, g h and i', p, g, h, 'and', i)
        S = SliderGui()
        S.runplot(p,g, h, i)
        
    
    def __init__(self):
        #customtkinter.set_ctk_parent_class(tkinterDnD.Tk)
        
        #customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
        #customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
        
        super().__init__()
        self.geometry("1000x480")
        self.title("CustomTkinter simple_example.py")
        
       # print(type(app), isinstance(app, tkinterDnD.Tk))
        
        self.TempAtTarget = StringVar()
        self.TempAtSolMidPoint = StringVar()
        self.NumberDensityAtTarget=StringVar()
        
        
        frame_1 = customtkinter.CTkFrame(master=self)
        frame_1.pack(pady=20, padx=60, fill="both", expand=True)
        
        label_1 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text = "Please enter the Electron number density at the SOL Mid=point")
        label_1.grid(row=1, column=0, padx=20, pady=20)
        
        label_2 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text = "Please enter the heat flux at the target in W/$m^2$")
        label_2.grid(row=3, column=0, padx=20, pady=20)
        
        label_3 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text = "Please enter the major radius of the tokamak in metres")
        label_3.grid(row=4, column=0, padx=20, pady=20)
        
        label_4 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text = "Please enter the Safety Value")
        label_4.grid(row=5, column=0, padx=20, pady=20)
        
        button_1 = customtkinter.CTkButton(master=frame_1, command=self.button_callback, text = 'Calculate Values')
        button_1.grid(row=6, column=1, padx=20, pady=20)
        
        
        
        
        self.optionmenu_1 = customtkinter.CTkOptionMenu(frame_1,values=["1e17", "1e18", "1e19", "1e20", "1e21"])
        self.optionmenu_1.grid(row=1, column=1, padx=20, pady=20)
        self.optionmenu_1.set("Electron_Number_Density_OptionMenu")
        
        self.optionmenu_2 = customtkinter.CTkOptionMenu(frame_1, values=["10,000","100,000", "1,000,000", "10,000,000"])
        self.optionmenu_2.grid(row=3, column=1, padx=20, pady=20)
        self.optionmenu_2.set("Heat_Flux_At_Target_Watts_metresquared_OptionMenu")
        
        self.entry = customtkinter.CTkEntry(frame_1, placeholder_text="CTkEntry")
        self.entry.grid(row=4, column=1, padx=20, pady=20)
        
        self.optionmenu_3 = customtkinter.CTkOptionMenu(frame_1, values=["1","2","3", "4", "5", "6"])
        self.optionmenu_3.grid(row=5, column=1, padx=20, pady=20)
        self.optionmenu_3.set("Safety Value of tokamak ")
        
        
app = InitialGui()       
app.mainloop()