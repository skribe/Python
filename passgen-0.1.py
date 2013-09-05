#!/usr/bin/env python
'''
passgen.py
Problem: Generate random passwords matching user-defined criteria 
Target Users: public
Target System: Linux
Interface: CLI
Functional Requirments: Choose number and type of characters to generate
    Establish data set of characters to choose from
    Randomly generate characters from available data set
    Display password to user
Maintainer: skribeproductions@gmail.com
'''
VERSION = 0.11

#import modules
import random, string

#define constants

LOWER_SET = list(string.ascii_lowercase)
UPPER_SET = list(string.ascii_uppercase)
NUMBER_SET = list(string.digits)
SPECIAL_SET = list(string.punctuation)


#define variables
numchar = 8
password =''
pw_dic = LOWER_SET + UPPER_SET + NUMBER_SET + SPECIAL_SET

#do stuff
for chars in range(numchar):
    password += random.choice(pw_dic)


#output
print(password)
