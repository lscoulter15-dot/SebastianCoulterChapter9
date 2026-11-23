# Naame: Sebastian Coulter
# Assignment 9: Graphical User Interface

# Import EasyFrame to creatw the GUI window

from tkinter import COMMAND 
from breezypythongui import EasyFrame 


# Create a temperature converter class using EasyFrame for the GUI 
class TemperatureConverter (EasyFrame):

   # Initial the temperature converter and set up its interface
   def __init__(self):
       super().__init__()

       # Add labels for Fahrenheit and Celsius 
       self.addLabel("Fahrenheit", 0,0)
       self.addLabel("Celsius",0, 1)

       # Create input fields for Fahrenherit and Celsius temperatures
       self.fahrenheit = self.addFloatField (32.0, 1, 0)


       self.celsius = self.addFloatField (0.0, 1, 1)

      # Add buttons to convert temperatures in both directions
       self.addButton(">>>", 2, 0, command=self.convertTemperature)
       self.addButton("<<<", 2, 1, command=self.convertToFahrenheit)

   # Convert the entered Fahrenheit temperature to Celsius 
   def convertTemperature(self):
       fahrenheit = self.fahrenheit.getNumber()
       celsius =(fahrenheit-32) * 5/9 
       self.celsius.setNumber(celsius)

   # Convert the entered Celsius temperature to fahrenheit 
   def convertToFahrenheit(self):
       celsius = self.celsius. getNumber()
       fahrenheit = (celsius * 9/5) +32
       self.fahrenheit.setNumber(fahrenheit)

# start the temperature converter application
TemperatureConverter().mainloop()