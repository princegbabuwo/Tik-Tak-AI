from random import choice, randint

combo_indices = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

EMPTY_SIGN = '.'
AI_SIGN = 'X'
PLAYER_SIGN = 'O'
BOARD = '.........'

def print_board(board):
    print(' '.join(board[:3]))
    print(' '.join(board[3:6]))
    print(' '.join(board[6:]))

def print_utilities(utilities):
    print (f'{utilities[0]}, {utilities[1]}, {utilities[2]}')
    print (f'{utilities[3]}, {utilities[4]}, {utilities[5]}')
    print (f'{utilities[6]}, {utilities[7]}, {utilities[8]}')

def init_utility_matrix(board):
    return [0 if cell == EMPTY_SIGN else -1 for cell in board]

def generate_add_score(utilities, board, index):
    def add_score(points):
        for m in index:
            if board[m] == EMPTY_SIGN: 
                utilities[m] += points
    return add_score

def utility_matrix(board):
    utilities = init_utility_matrix(board)
    for [i, j, k] in combo_indices:
        add_score = generate_add_score(utilities, board, [i, j, k])
        triple = [board[i], board[j], board[k]]
        if triple.count(EMPTY_SIGN) == 1:
            if triple.count(AI_SIGN) == 2:
                add_score(1000)        
            elif triple.count(PLAYER_SIGN) == 2:
                add_score(100)
        elif triple.count(EMPTY_SIGN) == 2 and triple.count(AI_SIGN) == 1:
            add_score(10)
        elif triple.count(EMPTY_SIGN) == 3:
            add_score(1)
    return utilities

def move(board, sign, pos):
    if board[pos] == EMPTY_SIGN: 
        return board[:pos] + sign + board[pos+1:]
    return None

def best_moves_from_board(board, sign):
    move_list = []
    utilities = utility_matrix(board)
    max_utility = max(utilities)
    print (f'maximum utility: {max_utility}')
    for i, v in enumerate(board):
        if utilities[i] == max_utility:
            move_list.append(board[:1] + sign + board[i+1:])
    return move_list

def possiblePlayerMoves(board):
    positions = []
    for (i, v) in enumerate(board):
        if v == EMPTY_SIGN: positions.append(i)
    return positions

def best_positions_for_AI(board):
    positions = []
    utilities = utility_matrix(board)
    max_utility = max(utilities)
    #print (f'maximum utility: {max_utility}')

    for (i, v) in enumerate(utilities):
        if utilities[i] == max_utility:
            positions.append(i)
    return positions

def ai_move(board):
    best_positions = best_positions_for_AI(board)
    #print (f'Best Positions: {best_positions}')
    pos = choice(best_positions)
    return move(board, AI_SIGN, pos)

def game_won_by(board):
    draw_count = 0
    for i in combo_indices:
        #i is combo in each combo_indices
        if board[i[0]] == board[i[1]] == board[i[2]] != EMPTY_SIGN:
            return board[i[0]]
        isdraw = board[i[0]] == AI_SIGN and board[i[1]] == PLAYER_SIGN
        isdraw = isdraw or (board[i[0]] == AI_SIGN and board[i[2]] == PLAYER_SIGN)
        isdraw = isdraw or (board[i[0]] == PLAYER_SIGN and board[i[1]] == AI_SIGN)
        isdraw = isdraw or (board[i[1]] == AI_SIGN and board[i[2]] == PLAYER_SIGN)
        isdraw = isdraw or (board[i[0]] == PLAYER_SIGN and board[i[2]] == AI_SIGN)
        isdraw = isdraw or (board[i[1]] == PLAYER_SIGN and board[i[2]] == AI_SIGN)
        #print(f'Case {i}; is_Draw: {isdraw}')
        if isdraw: 
            draw_count += 1
            #print(f'Draw Count: {draw_count}')
    if draw_count >= 8: return 0
    return EMPTY_SIGN

"""
def all_moves_from_board(board, sign):
    move_list = []
    for i, v in enumerate(board):
        if v == EMPTY_SIGN:
            new_board = board[:i] + sign + board[i+1:]
            move_list.append(new_board)
    return move_list


def all_moves_from_board_list(board_list, sign):
    move_list = []
    get_moves = best_moves_from_board if sign == AI_SIGN else all_moves_from_board
    for board in board_list:
        move_list.extend(get_moves(board, sign))
    return move_list

#print(all_moves_from_board(BOARD, AI_SIGN))
#sBOARD = 'x.......x'
#print(ai_move(sBOARD))
"""

#This function counts the game moves using Breath First Search 
#and inaccordance with the rules programmed for the AI player.
def countGameMoves(board, next_sign, counts):
    game_ended = game_won_by(board)
    if game_ended == 0:
        counts['draws'] += 1
        return 0, counts
    elif game_ended == AI_SIGN: 
        counts['ai'] += 1
        return 1, counts
    elif game_ended == PLAYER_SIGN:
        counts['human'] += 1
        return 2, counts

    if next_sign == PLAYER_SIGN:
        player_moves = possiblePlayerMoves(board)
        for pos in player_moves:
            new_board = move(board, PLAYER_SIGN, pos)
            next_sign = AI_SIGN
            state, counts_ = countGameMoves(new_board, next_sign, counts)
            if state > -1: continue

    elif next_sign == AI_SIGN:
        ai_moves = best_positions_for_AI(board)
        for pos in ai_moves:
            new_board = move(board, AI_SIGN, pos)
            next_sign = PLAYER_SIGN
            state, counts_ = countGameMoves(new_board, next_sign, counts) 
            if state > -1: continue
            
    return -1, counts

def game_loop():
    #TODO Write who plays first at Random
    board = BOARD
    empty_cell_count = 9
    is_game_ended = False
    next_player = choice([AI_SIGN, PLAYER_SIGN])


    while True: #empty_cell_count > 0 and not is_game_ended:
        if next_player == AI_SIGN:
            new_board = ai_move(board)
            next_player = PLAYER_SIGN
            print('AI TURN')
            print ('-----------')
            print_board(new_board)
            print(' ')
        elif next_player == PLAYER_SIGN:
            print('YOUR TURN')
            print ('-----------')
            board_nums = '123456789'
            stage_space = ''
            for i in enumerate(board):
                if i[1] == '.':
                    stage_space = f'{stage_space}{board_nums[i[0]]}'
                else: 
                    stage_space = f'{stage_space}{i[1]}'
            print_board(stage_space)
            pos = int(input(f'Your Turn({PLAYER_SIGN}): Enter Board Number to play: '))
            #TODO limit pos to between 1 & 9
            new_board = move(board, PLAYER_SIGN, pos-1)
            if new_board == None:
                print(' ')
                print ('Invalid Move! PLAY AGAIN!')
                continue
            next_player = AI_SIGN
            print(' ')
            print('YOUR MOVE')
            print ('-----------')
            print_board(new_board)
            print(' ')
        board = new_board

        game_ended = game_won_by(board)
        if game_ended == 0:
            print(' ')
            print ('GAME ENDED AS DRAW: No Winner!')
            break
        if game_ended == AI_SIGN: 
            print(' ')
            print ('GAME ENDED: Game Won by AI!')
            break
        elif game_ended == PLAYER_SIGN:
            print(' ')
            print ('GAME ENDED: Game Won by YOU!')
            break
    #TODO Ask to restart GAME


def gameCounts():
    board = '.........'
    first_player = PLAYER_SIGN
    counts = {
        'ai': 0,
        'human': 0,
        'draws': 0,
    }
    state1, counts1 = countGameMoves(board, first_player, counts)
    counts1['games'] = counts1['ai'] + counts1['human'] + counts1['draws']

    board = '.........'
    first_player = AI_SIGN
    counts = {
        'ai': 0,
        'human': 0,
        'draws': 0,
    }
    state2, counts2 = countGameMoves(board, first_player, counts)
    counts2['games'] = counts2['ai'] + counts2['human'] + counts2['draws']

    counts_ = {
        'games': counts1['games'] + counts2['games'],
        'ai': counts1['ai'] + counts2['ai'],
        'human': counts1['human'] + counts2['human'],
        'draws': counts1['draws'] + counts2['draws']
    }
    print(f'Human player first: {counts1}')
    print(f'AI player first: {counts2}')
    print(f'Total counts: {counts_}')

#gameCounts()
game_loop()