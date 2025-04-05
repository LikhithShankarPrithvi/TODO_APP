from chessPieces import ChessPieceFactory


class ChessBoard:

    def __init__(self):
        self.board=[['' for i in range(8)] for j in range(8)]

    def newBoard(self):
        #empty mid board
        for i in range(2,6):
            for j in range(8):
                self.board[i][j]=''
        # pawn_setup
        for i in range(8):
            self.board[1][i]= ChessPieceFactory.createPiece("Pawn","White")
            self.board[6][i]= ChessPieceFactory.createPiece("Pawn","Black")

        #Rook Setup
        self.board[0][0]=ChessPieceFactory.createPiece("Rook","White")
        self.board[0][-1]=ChessPieceFactory.createPiece("Rook","White")
        self.board[-1][0]=ChessPieceFactory.createPiece("Rook","Black")
        self.board[-1][-1]=ChessPieceFactory.createPiece("Rook","Black")

        #Knight Setup
        self.board[0][1]=ChessPieceFactory.createPiece("Knight","White")
        self.board[0][-2]=ChessPieceFactory.createPiece("Knight","White")
        self.board[-1][1]=ChessPieceFactory.createPiece("Knight","Black")
        self.board[-1][-2]=ChessPieceFactory.createPiece("Knight","Black")

        # Bishop Setup
        self.board[0][2]=ChessPieceFactory.createPiece("Bishop","White")
        self.board[0][-3]=ChessPieceFactory.createPiece("Bishop","White")
        self.board[-1][2]=ChessPieceFactory.createPiece("Bishop","Black")
        self.board[-1][-3]=ChessPieceFactory.createPiece("Bishop","Black")

        #Queen Setup
        self.board[0][3]=ChessPieceFactory.createPiece("Queen","White")
        self.board[-1][3]=ChessPieceFactory.createPiece("Queen","Black")

        #King Setup
        self.board[0][4]=ChessPieceFactory.createPiece("King","White")
        self.board[-1][4]=ChessPieceFactory.createPiece("King","Black")



    def print_board(self):
        for row in range(8):
            for col in range(8):
                piece=self.board[row][col]
                # print(piece)
                if piece!="":
                    print(piece.color,row,col,end=" ")
            print(".")
    def get_piece(self,position):
        row,col=position
        if self.board[row][col]!='':
            return self.board[row][col]
        return None
    def update_position(self,piece,old_position,new_position):
        row,col=new_position
        newCell=self.board[row][col]

        self.board[row][col]=piece
        oldRow,oldCol=old_position
        self.board[oldRow][oldCol]=''
        if newCell!='':
            return newCell
        return None
    
    def serialize_piece(self,piece):
        if piece=='':
            return None
        # print(piece)
        return {
            "type": piece.type,     # "Pawn", "Rook", etc.
            "color": piece.color    # "White" or "Black"
        }

    def get_board_state(self):
        return [
            [self.serialize_piece(cell) for cell in row]
            for row in self.board
        ]


# board=ChessBoard()
# board.newBoard()
# print(board.get_board_state())