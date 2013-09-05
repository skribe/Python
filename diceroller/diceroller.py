#! /usr/bin/python
"""
diceroller.py
Problem: A way to roll dice
Target Users: me
Target System: Linux
Interface: CLI
Functional Requirments: Choose which type of die to roll
    Choose how many dice to roll
    Output the rolls
Maintainer: skribeproductions@gmail.com
"""
version = 0.1

#import modules
import random

#Define Dice
def roll(sides, dice):
    result = 0
    for rolls in range(0,dice):
        result += random.randint(1,sides)
    return result

#Inputs
type = input("Enter the type of dice to roll (d4, d6,d8.d10,d12,d20,d100): ")
number = input("Enter the number of dice to roll: ")

sides = int(type)
dice = int(number)

#Outputs
diceroll = roll(sides,dice)
print("You rolled: ", diceroll)
