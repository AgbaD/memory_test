#!/usr/bin/python
# Author:   @BlankGodd_

import sys, time
from random import choice, random

colors = {40:'black', 41:'red', 42:'green', 43:'yellow', 44:'blue', 47:'white'}
base = '\033[{}m'
sols = {"b":"black","bl":"blue","r":"red","g":"green","y":"yellow","w":"white"}

def play(num=10):
    keys = [i for i in colors.keys()]
    game = [choice(keys) for i in range(num)]
    return game        
    
if __name__ == "__main__":
    print("""
        Welcome, to play this game, all you have to do is input a number of
        colors you think you can remember at a go. The default is 10. After this,
        different colors are displayed to you after which you have to enter the 
        colors that were displayed according to the pattern they were displayed.
        You are scored up until you input the wrong color for a position.
        Every other correct color is invalid\n
        To input you answer, type the first letter of the color except for color blue; type 'bl'
        e.g: B for Black, Bl for Blue, W for white, G for Green, Y for Yellow, 
        R for Red\n""")
         
    print("\t"+base.format(91) + "YOUR ANSWERS SHOULD BE TYPED IN A SINGLE COMMA SEPERATED STRING." + base.format(0))
    
    print("""
        You get one point per color 
        All answers must be submitted in order!\n
        Ignore the following prompt to use a default value of 10 or enter your 
        value to display that number of colors. GoodLuck!
    """)
    
    num = 0
    try:
        num = int(input("> "))
    except:
        num = 10
    game = play(num=num)
    answers = [colors[i] for i in game]
    bases = [base.format(j) for j in game]
    for i in bases:
        print(i)
        print('++++++++++++++++++++++++++++++++++++++++++++++')
        time.sleep(0.5)
    print(base.format(0))
    print('\n' * 100)
    print('Your answers should be written in a single comma seperated string.')
    print("Enter your colors")
    user_input = input("> ")
    try:
        users = user_input.split(',')
        users = [i.lower() for i in users]
    except:
        print("InputError")
        print(base.format(0))
        sys.exit(1)
    score = 0
    for i in range(num):
        try:
            if (sols[users[i]] == answers[i]) or (users[i] == answers[i]):
                score += 1  
            else:
                break
        except:
            break
    print("You scored {} out of {}".format(score,num))
    print(answers)    
    print()
