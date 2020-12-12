# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 21:36:29 2020

@author: Tsiolkovsky
"""

# The initial state of the board is defined (empty):

state = ["-","-","-","-","-","-","-","-","-"]

# A function is defined to draw the state:

def draw(x):

    print("\n{0}{1}{2}\n{3}{4}{5}\n{6}{7}{8}".format(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8]))


# The initial state is drawn:
    
draw(state)

# The first turn is given to player 1:

player = 1

# The game begins:

flag = True

while flag:
    
    # Depending on the player playing this turn, one symbol or another will be drawn:
    
    if player==1:
        symbol="x"
    else:
        symbol="o"
    
    # The player is asked where he wants to move and his answer is checked to 
    # be an interger:
    
    while True:
        try:
            square = int(input("Choose a square to move: "))
            break
        except ValueError:
            print("                      \n                             Invalid character")
            draw(state)
    
    # First it is checked if the user has entered a valid index for a square,
    # and then: If the square is not occupied, the state of the board is 
    # modified with the new move and the turn is given to the other player. 
    # If the square is occupied, an error message is displayed and the current 
    # player's turn is kept:
    
    if square<1 or square>9:
            print("                      \n                             Invalid character")            
    elif state[int(square)-1]=="-":
        state[int(square)-1]=symbol
        player*=-1
    else:
        print("                             That square is already occupied")
    
    # The board is drawn:
    
    draw(state)
       
    # We check if someone has won the game
    
    j=0
    
    while j<7:                   
        if state[j]==state[j+1]==state[j+2]!="-":
            print("                             {0} wins".format(state[j]))
            flag = False
        j+=3
    j=0
    while j<3:        
        if state[j]==state[j+3]==state[j+6]!="-":
            print("                             {0} wins".format(state[j]))
            flag = False
        j+=1
    if state[0]==state[4]==state[8]!="-":
        print("                             {0} wins".format(state[0]))
        flag = False
    if state[2]==state[4]==state[6]!="-":
        print("                             {0} wins".format(state[2]))
        flag = False
                
    # We check if a tie has been made:
    
    if flag:
        occupied_squares = 0
        for square in state:        
            if square!="-":
                occupied_squares+=1
        if occupied_squares==9:
            flag=False
            print("                             Draw")
            
            
            
