class Environment():
    def __init__(self):
        self.board = '-'*9
        self.winner = None
        self.ended = False
        self.num_states = 3**(3*3)

    def set_board(self, board):
        self.board = board

    def update_board(self,place,symbol):
        if self.board[place]=='-':
            self.board = self.board[:place] + symbol + self.board[place+1:]
        elif symbol=="x":
            self.winner='o'
            self.ended=True
        else:
            self.winner='x'
            self.ended=True

    def reward(self, sym):
        if self.winner == sym:
            return(1)
        if self.winner == None:
            return(0.3)
        else:
            return(0)

    def is_uniform(self,string):
        if '-' in string:
            return(False)
        for i in string:
            if (not i == string[0]):
                return(False)
        return(True)

    def game_over(self):
        # Horizontals
        if self.is_uniform(self.board[:3]):
            self.winner = self.board[0]
            self.ended = True
        if self.is_uniform(self.board[3:6]):
            self.winner = self.board[3]
            self.ended = True
        if self.is_uniform(self.board[6:9]):
            self.winner = self.board[6]
            self.ended = True

        # Verticals
        for i in range(3):
            if self.is_uniform(self.board[i::3]):
                self.winner = self.board[i]
                self.ended = True

        #Diagonals
        if self.is_uniform(self.board[0::4]):
            self.winner = self.board[0]
            self.ended = True

        if self.is_uniform(self.board[2:8:2]):
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
