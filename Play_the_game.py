import Human
import Agent
import numpy as np
import Play_Game as PG
import Environment

human = Human.Human()
human.set_symbol('o')
p1 = Agent.Agent(input_shape=(3,3,2),N_movements=9,eps=[0])
p1.set_V('Model_x.hdf5')
p1.set_symbol('x')
while True:
    winner=PG.play_games(p1, human, Environment.Environment(),N=1,Train=False, draw=2)
    # I made the agent player 1 because I wanted to see if it would
    # select the center as its starting move. If you want the agent
    # to go second you can switch the human and AI.
    if winner=='x':
        print('You have lost, better luck next time!')
    elif winner=='o':
        print('Concratulations, you have won!')
    else:
        print('Its a draw.')
    answer = input("Play again? [Y/n]: ")
    if answer and answer.lower()[0] == 'n':
        break
