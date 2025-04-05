from abc import ABC, abstractmethod

class ChessPiece(ABC):


    def __init__(self,color,type):
        self.color=color
        self.type=type
    def move(self):
        pass

class King(ChessPiece):

    def __init__(self,color):
        super().__init__(color,'King')
    
class Queen(ChessPiece):

    def __init__(self,color):
        super().__init__(color,'Queen')

class Rook(ChessPiece):

    def __init__(self,color):
        super().__init__(color,'Rook')

class Knight(ChessPiece):

    def __init__(self,color):
        super().__init__(color,'Knight')

class Pawn(ChessPiece):

    def __init__(self,color):
        super().__init__(color,'Pawn')

class Bishop(ChessPiece):

    def __init__(self,color):
        super().__init__(color,'Bishop')


class ChessPieceFactory:
    @staticmethod
    def createPiece(piece_type, color):
        piece_classes = {"Rook": Rook, "Knight": Knight, "Bishop": Bishop, "King": King, "Queen": Queen, "Pawn": Pawn}
        return piece_classes[piece_type](color)


# rook=ChessPieceFactory.createPiece("Rook","White")
# print(rook.color,rook.type)
# rook=Rook('White')
# print(rook.color,rook.type)