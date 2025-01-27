from time import sleep
from os import system
from random import randint

moves = ['rock', 'scissors', 'paper']

while True:
    system('cls')
    print("Rock, paper, scissors minigame!")
    print("Playing vs computer")
    pick = input('Please select your move ("rock", "scissors", "paper"): ').lower()
    if pick not in moves:
        system('cls')
        print("Wrong selection! Try again.")
        sleep(2)
        continue
    pickIndex = moves.index(pick)
    system('cls')
    print('Computer is thinking...')
    sleep(2)
    robotIndex = randint(0,2)
    winner = None
    
    if pickIndex == robotIndex:
        system('cls')
        print('Tie!')
        sleep(5)
        continue
    elif (pickIndex == 2 and robotIndex != 1):
        winner = 'user'
    elif (pickIndex == 0 and robotIndex != 2):
        winner = 'user'
    elif (pickIndex == 1 and robotIndex != 0):
        winner = 'user'
    else:
        winner = 'computer'
    
    system('cls')
    if winner == 'user':
        print(f"You won, congrats. Computer chose {moves[robotIndex]} while you {moves[pickIndex]}")
    else:
        print(f"Computer won, he chose {moves[robotIndex]} and you chose {moves[pickIndex]}")
    sleep(5)
    
    