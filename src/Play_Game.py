import Environment
def play_games(p1,p2,env,N,Train,draw=False):
    for game in range(N):
        env=Environment.Environment()
        current_player = None
        while not env.ended:
            if current_player == p1:
                current_player = p2
            else:
                current_player = p1

            state = env.board
            current_player.update_history(state)
            current_player.take_action(env)
            #other_player.update_history(state)
            env.game_over()

            if draw:
                env.draw_board()

        if Train:
            p1.targets.append([env.reward(p1.sym),p1.N_actions])
            p1.N_actions=0
            p2.targets.append([env.reward(p2.sym),p2.N_actions])
            p2.N_actions=0
    if Train:
        if p2.eps<len(p2.epsilons):
            p2.eps+=1
        if p1.eps<len(p1.epsilons):
            p1.eps+=1
    if Train:
        p1.update_V(env)
        p2.update_V(env)
    return env.winner
