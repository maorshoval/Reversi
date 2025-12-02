
import copy

BOARD_SIZE = 8
#TODO :Create a player class
class Player:
    #TODO: polish the class to later include hurisitic functions
    def __init__(self, symbol):
        self.symbol = symbol


#reversi board class 8x8 board size
class Reversi:
    # TODO: crate initial board setup
    def __init__(self, board=None,current_player='x'):
        if board is None:
            self.player_x = Player('x')
            self.player_o = Player('o')
            self.board = [['_' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
            self.board[3][3] = 'x'#player 1
            self.board[3][4] = 'o'#player 2
            self.board[4][3] = 'o'#player 2
            self.board[4][4] = 'x'#player 1
        else:
            self.board = copy.deepcopy(board)


    #TODO: create a function to print the board
    def print_board(self):
        for row in self.board:
            print(' '.join(row))
        print()

    # TODO: create a transtion function to get all possible moves
    def get_possible_moves(self, player):
        # Placeholder for possible moves logicb
        return []


# TODO: create a function to apply a move and return the new board state
# TODO: create a function to evaluate the board state
# TODO: create the minimax function with alpha-beta pruning
# TODO: create a function to get the best move for the AI
# TODO: create a function to check for game over conditions

if __name__ == "__main__":
    game = Reversi()
    game.print_board()