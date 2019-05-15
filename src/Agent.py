import numpy as np
import State_converter as sc
import CNN_models as CNN

class Agent:
    def __init__(self,input_shape,N_movements, eps=[.1], alpha=.5):
        self.epsilons=eps
        self.eps =0
        self.alpha = alpha
        self.Action_history = []
        self.state_history = []
        self.targets = []
        self.N_movements=N_movements
        self.input_shape=input_shape
        self.N_actions=0
        self.model=CNN.CNN_BoterKaasEieren(self.N_movements,self.input_shape)

    def set_V(self, V):
        self.model=CNN.load(V)

    def set_symbol(self, sym):
        if (sym=='-'): exit("Error, the symbol '-' is used to display an empty field and can not be used by agents or players.")
        self.sym = sym

    def reset_history(self):
        self.state_history = []
        self.Action_history = []
        self.targets=[]

    def update_history(self, s):
        self.state_history.append(s)

    def update_V(self, env):
        # Nadat spel voorbij is
        values=np.zeros(shape=(len(self.state_history),self.N_movements))
        Inputs=np.zeros(shape=(len(self.state_history),3,3,2))
        count=0
        subcount=0
        for i,state in enumerate(self.state_history):
            if subcount==self.targets[count][1]:
                count+=1
                subcount=0
            target=self.targets[count][0]
            subcount+=1
            values[i]=self.model.predict(sc.convert_to_numbers(state,self.sym).reshape(1,3,3,2))
            values[i,self.Action_history[i]]= values[i,self.Action_history[i]] + self.alpha*(target - values[i,self.Action_history[i]])
            Inputs[i]=sc.convert_to_numbers(state,self.sym)
        CNN.fit_model(self.model,Inputs,values,"Model_"+self.sym+".hdf5")
        self.reset_history()

    def take_action(self, env):
        best_state = None
        best_value = -1
        possible_moves = []
        best_i=0


        for i in range(len(env.board)):
            if env.board[i] == '-':
                possible_moves.append(i)
        if possible_moves == []: print('FULL')

        r = np.random.rand()
        if r < (self.epsilons[self.eps]):
            idx = np.random.choice(len(possible_moves))
            i = possible_moves[idx]
            env.update_board(i,self.sym)
            best_i=i
        else:
            board_state=sc.convert_to_numbers(env.board,self.sym)
            # calcualte value
            value=self.model.predict(board_state.reshape(1,3,3,2))
            best_i=np.argmax(value[0])
            best_value=value[0,best_i]
            env.update_board(best_i,self.sym)
        self.N_actions+=1
        self.Action_history.append(best_i)
