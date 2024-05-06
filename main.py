from random import choice

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
def countGameMoves(board, next_sign, moves_count):
    #TODO if board is a game won board such a board cannot be counted
    game_ended = game_won_by(board)
    if game_ended == 0: 
        return
    elif game_ended == AI_SIGN: return
    elif game_ended == PLAYER_SIGN: return

    print(f'Board: {board}\nMoves: {moves_count}')
    if next_sign == PLAYER_SIGN:
        player_moves = possiblePlayerMoves(board)
        for pos in player_moves:
            board = move(board, PLAYER_SIGN, pos)
            moves_count += 1
            next_sign = AI_SIGN
            gameMoves = countGameMoves(board, next_sign, moves_count)
            print(gameMoves)
            #print(board)
    if next_sign == AI_SIGN:
        ai_moves = best_positions_for_AI(board)
        print(f'AI Moves: {ai_moves}')
        for pos in ai_moves:
            board = move(board, AI_SIGN, pos)
            #print(f'Board @AI: {board}')
            moves_count += 1
            next_sign = PLAYER_SIGN
            gameMoves = countGameMoves(board, next_sign, moves_count)
            print(gameMoves)
    return
    board_list = []
    board_list.append(board)
    move_count = 0
    #print(board_list[-1])
    while True:
        print(f'move count: {move_count}\nBoard List: {board_list[-1]}')
        if next_sign == PLAYER_SIGN:
            for (i, v) in enumerate(board_list[-1]):
                #print(i, v)
                if v == EMPTY_SIGN:
                    #print('am here')
                    board = move(board, PLAYER_SIGN, i)
                    next_sign = AI_SIGN
                    break
        elif next_sign == AI_SIGN: 
            board = ai_move(board)
            next_sign = PLAYER_SIGN

        move_count +=1
        #Check if game has been won or drawn before appending move or game has ended
        board_list.append(board)

        if move_count > 10: break

board = 'X.OOX.X.O'
#board = '.........'
#game_won_by(board)
countGameMoves(board, AI_SIGN, 0)


def game_loop():
    #TODO Check if game has ended before the next move is played
    #TODO Print Utility Values
    #TODO Write you plays first at Random
    board = BOARD
    empty_cell_count = 9
    is_game_ended = False
    while empty_cell_count > 0 and not is_game_ended:
        if empty_cell_count % 2 == 1:
            new_board = ai_move(board)
            print('AI MOVE')
            print ('-----------')
            print_board(new_board)
            print(' ')
        else:
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
            print(' ')
            print('YOUR MOVE')
            print ('-----------')
            print_board(new_board)
            print(' ')
        board = new_board

        game_ended = game_won_by(board)
        print(f'Game Ended: {game_ended}')
        is_game_ended = game_ended != EMPTY_SIGN
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

        empty_cell_count -= 1
    else: 
        print(' ')
        print ('GAME ENDED: No Winner!')
    #TODO Ask to restart GAME

#game_loop()