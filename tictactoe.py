import numpy as np
import itertools

def is_uniform(string):
    if '-' in string:
        return(False)
    for i in string:
        if (not i == string[0]):
            return(False)
    return(True)

class Environment():
    def __init__(self):
        self.board = '-'*9
        self.x = 'x'
        self.o = 'o'
        self.winner = None
        self.ended = False
        self.num_states = 3**(3*3)

    def set_board(self, board):
        self.board = board

    def reward(self, sym):
        if self.winner == sym:
            return(1)
        if self.winner == None:
            return(0.3)
        else:
            return(0)

    def game_over(self):
        # Horizontals
        if is_uniform(self.board[:3]):
            self.winner = self.board[0]
            self.ended = True
        if is_uniform(self.board[3:6]):
            self.winner = self.board[3]
            self.ended = True
        if is_uniform(self.board[6:9]):
            self.winner = self.board[6]
            self.ended = True

        # Verticals
        for i in range(3):
            if is_uniform(self.board[i::3]):
                self.winner = self.board[i]
                self.ended = True

        #Diagonals
        if is_uniform(self.board[0::4]):
            self.winner = self.board[0]
            self.ended = True

        if is_uniform(self.board[2:8:2]):
            self.winner = self.board[2]
            self.ended = True

        # Check draw
        if (self.winner == None) and (not ('-' in self.board)):
            self.winner = None
            self.ended = True

    def draw_board(self):
        print(self.board[:3]+'\n'+
              self.board[3:6]+'\n'+
              self.board[6:9]+'\n\n')

class Agent:
    def __init__(self, eps=.1, alpha=.5, optimism=.5):
        self.eps = eps
        self.alpha = alpha
        self.state_history = []
        self.optimism = optimism

    def set_V(self, V):
        self.V = V

    def set_symbol(self, sym):
        self.sym = sym

    def reset_history(self):
        self.state_history = []

    def update_history(self, s):
        self.state_history.append(s)

    def update_V(self, env):
        # Nadat spel voorbij is
        reward = env.reward(self.sym)
        target = reward
        for prev in reversed(self.state_history):
            value = self.V[prev] + self.alpha*(target - self.V[prev])
            self.V[prev] = value
            target = value
        self.reset_history()


    def initialize_V(self):
        V = {}
        states = list(map("".join, itertools.product('-xo', repeat=9)))
        for s in states:
            e = Environment()
            e.set_board(s)
            e.game_over()
            if e.ended == True:
                V[s] = e.reward(self.sym)
            else:
                V[s] = self.optimism
        self.V = V

    def take_action(self, env):
        best_state = None
        best_value = -1
        possible_moves = []
        for i in range(len(env.board)):
            if env.board[i] == '-':
                possible_moves.append(i)
        if possible_moves == []: print('FULL')

        r = np.random.rand()
        if r < (self.eps):
            idx = np.random.choice(len(possible_moves))
            i = possible_moves[idx]
            env.board = env.board[:i] + self.sym + env.board[i+1:]
        else:
            for i in possible_moves:
                next_state = env.board[:i] + self.sym + env.board[i+1:]

                if self.V[next_state] > best_value:
                    best_state = next_state
                    best_value = self.V[next_state]
            env.board = best_state

class Human:
  def __init__(self):
    pass

  def set_symbol(self, sym):
    self.sym = sym

  def take_action(self, env):
    while True:
      # break if we make a legal move
      move = input("Enter position i for your next move")
      i = int(move) -1
      if env.board[i] == '-':
          env.board = env.board[:i] + self.sym + env.board[i+1:]
          break

  def update_V(self, env):
    pass

  def update_history(self, s):
    pass

def play_game(p1,p2,env,draw=False):
    current_player = None
    while not env.ended:
        if current_player == p1:
            current_player = p2
        else:
            current_player = p1

        current_player.take_action(env)
        state = env.board
        p1.update_history(state)
        p2.update_history(state)
        env.game_over()

        if draw:
            env.draw_board()

    p1.update_V(env)
    p2.update_V(env)

p1 = Agent(eps=0, optimism=1.5)
p2 = Agent(eps=0, optimism=1.5)

p1.set_symbol('x')
p2.set_symbol('o')
p1.initialize_V()
p2.initialize_V()

T = 3000
game = 1
for t in range(T):
    draw=False
    if t % 100000 == 0:
        game+=1
        print(t)
        #draw=True
    play_game(p1, p2, Environment(), draw=draw)

human = Human()
human.set_symbol('o')
while True:
    play_game(p1, human, Environment(), draw=2)
    # I made the agent player 1 because I wanted to see if it would
    # select the center as its starting move. If you want the agent
    # to go second you can switch the human and AI.
    answer = input("Play again? [Y/n]: ")
    if answer and answer.lower()[0] == 'n':
        break
