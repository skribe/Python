#!/usr/bin/python

"""
Faren2Cel.py
Problem: Convert Farenheit temperatures to Celsius
Target Users: me
Target System: Linux
Interface: CLI
Fucntional Requirements: Ask for Farenheit temperature
    Do conversion
    Output Celsius
Maintainer: skribeproductions@gmail.com
"""
version = 0.1

#import modules

#Inputs
faren = input("Farenheit: ")
farenheit = int(faren)
#Conversion
# Celisus = (F  -  32)  x  5/9 

celsius = (farenheit - 32) * 5/9

#Output
print("Celsius: ", celsius)
