import random, numpy as np

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
AI_SIGN = 'x'
PLAYER_SIGN = 'O'
BOARD = '.........'
#print(combo_indices)

def print_board(board):
    #print (board)
    print(' '.join(board[:3]))
    print(' '.join(board[3:6]))
    print(' '.join(board[6:]))
#print_board('X...O...X')

#ReWrite
def move(board, sign, pos):
    pos -= 1
    #print(f'am inside board; pos: {pos}')
    if board[pos] == EMPTY_SIGN: 
        #print(f'am inside board if;')
        #print('to return: ' + board[:pos] + sign + board[pos+1:])
        return board[:pos] + sign + board[pos+1:]
    return None

#ReWrite
def ai_move(board):
    while True:
        pos = random.randint(1, 9)
        if board[pos-1] == EMPTY_SIGN:
            mv = move(board, AI_SIGN, pos)
            if mv == None: continue
            else: 
                return mv
                break
        

    

def all_moves_from_board(board, sign):
    move_list = []
    for i, v in enumerate(board):
        if v == EMPTY_SIGN:
            new_board = board[:i] + sign + board

def game_won_by(board):
    for i in combo_indices:
        #print (f'index: {i}')
        if board[i[0]] == board[i[1]] == board[i[2]] != EMPTY_SIGN:
            return board[i[0]]
    return EMPTY_SIGN


def game_loop():
    board = BOARD
    #print (board)
    empty_cell_count = 9
    is_game_ended = False
    while empty_cell_count > 0 and not is_game_ended:
        if empty_cell_count % 2 == 1: 
            new_board = ai_move(board)
            #print(f'Board @AI: {board}')
            #print(f'New Board @AI: {new_board}')
            print('AI MOVE')
            print ('-----------')
            print_board(new_board)
            #print ('.........')
            print(' ')
        else:
            board_nums = '123456789'
            stage_space = ''
            for i in enumerate(board):
                if i[1] == '.':
                    stage_space = f'{stage_space}{board_nums[i[0]]}'
                else: 
                    stage_space = f'{stage_space}{i[1]}'
                    #print(f'i={i[1]}')
                #print(i)
            print_board(stage_space)
            pos = int(input(f'Your Turn({PLAYER_SIGN}): Enter Board Number to play: '))
            #TODO limit pos to between 1 & 9
            new_board = move(board, PLAYER_SIGN, pos)
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
        is_game_ended = game_ended != EMPTY_SIGN
        #print (f'game_ended: {game_ended}; is_game_ended: {is_game_ended}')
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

        


#print_board(ai_move(BOARD))

game_loop()