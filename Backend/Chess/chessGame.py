from Chess.chessBoard import ChessBoard
from Chess.chessStrategy import MoveStrategyFactory
from Chess.chessPieces import *

class Chess:
    

    def __init__(self):
        self.board=ChessBoard()
        self.board.newBoard()
        self.player1='Player1'
        self.player2='Player2'
        self.currentPlayer=self.player1
        self.status="progress"
    
    def get_valid_moves(self,position):
        piece=self.board.get_piece(position)
        if not piece:
            return []
        strategy = MoveStrategyFactory.get_strategy(piece)
        return strategy.getValidMoves(piece, position, self.board.board)
        
    def move_piece(self, old_position, new_position):
        
        piece=self.board.get_piece(old_position)
        if not piece:
            return []
        valid_moves = self.get_valid_moves(old_position)
        print(new_position,valid_moves)
        if list(new_position) in valid_moves:
            print('Updating')
            return self.board.update_position(piece, old_position,new_position)

    def changePlayer(self):
        if self.currentPlayer==self.player1:
            self.currentPlayer=self.player2
        else:
            self.currentPlayer=self.player1


    
    def print_board(self):
        # Print column labels
        self.board.print_board()
