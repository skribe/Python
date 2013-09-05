#!/usr/bin/env python
'''
passgen.py
Problem: Generate random passwords matching user-defined criteria 
Target Users: public
Target System: Linux
Interface: CLI
Licence: GPL3
Functional Requirments: Choose number and type of characters to generate
    Establish data set of characters to choose from
    Randomly generate characters from available data set
    Display password to user
Maintainer: skribeproductions@gmail.com
'''
VERSION = 0.2

#import modules
import random, string

#define constants

LOWER_SET = list(string.ascii_lowercase)
UPPER_SET = list(string.ascii_uppercase)
NUMBER_SET = list(string.digits)
SPECIAL_SET = list(string.punctuation)


#define variables
password =''
pwDic = LOWER_SET

#Small password function

def smallPassword():
    # This function returns True if the user wants to continue
    # generating a ridiculously small password, otherwise it returns False.
    print('Password is too small.  Do you wish to continue? (yes or no)')
    return input().lower().startswith('y')

# Do you Wanna function

def doYouWanna(type):
    # This function returns true if the use wants a certain character
    # included in their password, otherwise it returns false.
    # options include numbers, capitals and special characters
    print('Do you want to include ' + type + ' in your password? (yes or no)')
    return input().lower().startswith('y')

while True:
    try:
        numchar = int(input('How many characters is the password: '))
        if numchar < 8:
            if smallPassword():
                break
        else:
            break
    except ValueError:
        print('Oops!  That was no valid number.  Try again...')

# set up the password dictionary to generate the password from
if doYouWanna('numbers'):
    pwDic = pwDic + NUMBER_SET

if doYouWanna('upper case letters'):
    pwDic = pwDic + UPPER_SET

if doYouWanna('special characters'):
    pwDic = pwDic + SPECIAL_SET

#generate password
for chars in range(numchar):
    password += random.choice(pwDic)

#output
print(password)
