import Agent
import Environment
import Play_Game as PG
import numpy as np



T = 50

p1 = Agent.Agent(input_shape=(3,3,2),N_movements=9,eps=np.arange(1,0,-1./T))
p2 = Agent.Agent(input_shape=(3,3,2),N_movements=9,eps=np.arange(1,0,-1./T))
p1.set_symbol('x')
p2.set_symbol('o')


game = 1
#for t in range(T):
#    draw=False
#    if t % 100000 == 0:
#        game+=1
#        print(t)
        #draw=True
#    PG.play_games(p1, p2, Environment.Environment(),100, Train=True,draw=draw)

p1wins=0
p2wins=0
Nonewins=0
draw=False
n=1000
for i in range(n):
    winner=PG.play_games(p1, p2, Environment.Environment(),1, Train=False,draw=draw)
    if winner==p1.sym: p1wins+=100./n
    elif winner==p2.sym: p2wins+=100./n
    else: Nonewins+=100./n
print('winner\tSymbol\t#occurance')
print('p1\t%s\t%i%s'%(p1.sym,p1wins,'%'))
print('p2\t%s\t%i%s'%(p2.sym,p2wins,'%'))
print('draw\t%s\t%i%s'%('-',Nonewins,'%'))
