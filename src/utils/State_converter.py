import numpy as np

def convert_to_numbers(state,OwnSym):
    newstate=np.zeros(shape=(3,3,2))
    for i,symbol in enumerate(state):
        if symbol=='-':
            newstate[int(i/3),i%3]=[0,1]
        elif symbol==OwnSym:
            newstate[int(i/3),i%3]=[1,0]
        else:
            newstate[int(i/3),i%3]=[-1,0]
    return newstate

def convert_to_string(state,OwnSym):
    newstate=""
    if OwnSym=='x':
        OtherSym='o'
    else:
        OtherSym='x'
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j][0]==0:
                newstate+='-'
            if state[i][j][0]==1:
                newstate+=OwnSym
            if state[i][j][0]==0:
                newstate+=OtherSym
    return newstate
