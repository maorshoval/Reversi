
import copy

BOARD_SIZE = 8
DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1),
             (0, -1),          (0, 1),
             (1, -1), (1, 0), (1, 1)]
#TODO :Create a player class
class Player:
    #TODO: polish the class to later include hurisitic functions
    def __init__(self, symbol):
        self.symbol = symbol


#reversi board class 8x8 board size
    def is_valid_move(board, row, col, player):
        opponent = 'o' if player.symbol == 'x' else 'x'

        for direction in DIRECTIONS:
            x, y = row + direction[0], col + direction[1]
            has_opponent_between = False

            while 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE:
                if board[x][y] == opponent:
                    has_opponent_between = True
                elif board[x][y] == player.symbol:
                    if has_opponent_between:
                        return True
                    else:
                        break
                else:
                    break

                x += direction[0]
                y += direction[1]

        return False


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


        # TODO: create Actions (possible moves)

    def get_all_possible_states(self, board, player):
        pass

    # TODO: create a transtion model to get new state from current state and action
    def get_new_state(self, board, action, player):
        new_board = copy.deepcopy(board)
        x, y = action
        new_board[x][y] = player.symbol
        return


    #TODO: create a function to check if a move is valid

    # TODO: create a transtion function to get all possible moves
    # def get_possible_moves(self, board,player):
    #     possible_moves =[]#list of tuples (row, col)
    #
    #     for row in range(BOARD_SIZE):
    #         for col in range(BOARD_SIZE):
    #             if board[row][col] == '_':
    #                 if player.is_valid_move(board, row, col, player):
    #                     possible_moves.append((row, col))



    #TODO: state space function to get all possible states from current


    #TODO: create terminal state (game over) function
    def is_terminal_state(self, board):
        pass

    #TODO : create utility function to evaluate board state
    def evaluate_board(self, board):
        pass




if __name__ == "__main__":
    game = Reversi()
    game.print_board()
