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
        You are score up until you input the wrong color for a position.\n
        To input you answer, input the first letter of the color except for color blue
        e.g: B for Black, Bl for Blue, W for white, G for Green, Y for Yellow, R for Red
        Your answers should be written in a single comma seperated string.\n
        You get one point per color
        You get two points if you can remember the numbers on the color too. 
        Yo get a prompt for the numbers and you can ignore if you want.\n
        All answers must be submitted in order!\n
        Ignore the following prompt to use a default value of 10 or enter your 
        value to display that number of colors. GoodLuck!
    """)
    
    num = 0
    try:
        num = int(input("> "))
    except:
        pass
    game = []
    if num != 0:
        game = play(num=num)
    else:
        game = play()
    answers = [colors[i] for i in game]
    numbers = []
    bases = [base.format(j) for j in game]
    for i in bases:
        sys.stdout.write(i)
        x = round(random(),2)
        numbers.append(x)
        print(x)
        time.sleep(0.3)
        sys.stdout.flush()
    print(base.format(0))
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
        if sols(users[i]) == answers[i]:
            score += 1  
        else:
            break
    print(base.format(0))
    print("Enter your numbers")
    try:
        user_numbers = input("> ")
    except:
        pass
    if user_numbers:
        print(user_numbers)
        try:
            users = user_numbers.split(',')
            users = [float(i) for i in users]
        except:
            print("InputError")
            print(base.format(0))
            sys.exit(1)
        for i in range(num):
            if users[i] == numbers[i]:
                score += 1  
            else:
                break
    print("You scored {} out of {}".format(score,num))
    
    
