class Human:
  def __init__(self):
    pass

  def set_symbol(self, sym):
    self.sym = sym

  def take_action(self, env):
    while True:
      # break if we make a legal move
      move = input("Enter position i for your next move: ")
      i = int(move) -1
      if env.board[i] == '-':
          env.board = env.board[:i] + self.sym + env.board[i+1:]
          break

  def update_V(self, env):
    pass

  def update_history(self, s):
    pass
