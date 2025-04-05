from abc import ABC, abstractmethod

class MoveStrategy(ABC):

    def getValidMoves(self,piece,board):
        pass

class PawnMoveStrategy(MoveStrategy):

    def getValidMoves(self, piece, position, board):
        row, col = position
        validMoves = []
        piece_color = piece[0]  # 'W' or 'B'
        
        # Set direction based on piece color
        direction = -1 if piece_color == 'W' else 1
        start_row = 6 if piece_color == 'W' else 1
        
        # Forward move
        if 0 <= row + direction < 8:
            if board[row + direction][col] == '':
                validMoves.append([row + direction, col])
                # First move can be 2 squares
                if row == start_row and board[row + 2*direction][col] == '':
                    validMoves.append([row + 2*direction, col])
        
        # Diagonal captures
        for col_offset in [-1, 1]:
            new_col = col + col_offset
            new_row = row + direction
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                if board[new_row][new_col] != '':  # Square is occupied
                    target_piece = board[new_row][new_col]
                    if target_piece[0] != piece_color:  # Opposite color piece
                        validMoves.append([new_row, new_col])
        
        return validMoves

class RookMoveStrategy(MoveStrategy):

    def getValidMoves(self, piece, position, board):
        row, col = position
        validMoves = []
        piece_color = piece[0]
        
        # Horizontal moves (left)
        for newCol in range(col-1, -1, -1):
            if board[row][newCol] == '':
                validMoves.append([row, newCol])
            else:
                target_piece = board[row][newCol]
                if target_piece[0] != piece_color:  # Opposite color piece
                    validMoves.append([row, newCol])
                break
        
        # Horizontal moves (right)
        for newCol in range(col+1, 8):
            if board[row][newCol] == '':
                validMoves.append([row, newCol])
            else:
                target_piece = board[row][newCol]
                if target_piece[0] != piece_color:
                    validMoves.append([row, newCol])
                break
        
        # Vertical moves (up)
        for newRow in range(row-1, -1, -1):
            if board[newRow][col] == '':
                validMoves.append([newRow, col])
            else:
                target_piece = board[newRow][col]
                if target_piece[0] != piece_color:
                    validMoves.append([newRow, col])
                break
        
        # Vertical moves (down)
        for newRow in range(row+1, 8):
            if board[newRow][col] == '':
                validMoves.append([newRow, col])
            else:
                target_piece = board[newRow][col]
                if target_piece[0] != piece_color:
                    validMoves.append([newRow, col])
                break
        
        return validMoves

class BishopMoveStrategy(MoveStrategy):

    def getValidMoves(self, piece, position, board):
        row, col = position
        validMoves = []
        piece_color = piece[0]  # 'W' or 'B'
        
        # Diagonal moves in all 4 directions
        # Up-Right diagonal
        for i in range(1, 8):
            if row-i < 0 or col+i >= 8: break
            if board[row-i][col+i] == '':
                validMoves.append([row-i, col+i])
            else:
                target_piece = board[row-i][col+i]
                if target_piece[0] != piece_color:  # Different color = valid capture
                    validMoves.append([row-i, col+i])
                break
                
        # Up-Left diagonal
        for i in range(1, 8):
            if row-i < 0 or col-i < 0: break
            if board[row-i][col-i] == '':
                validMoves.append([row-i, col-i])
            else:
                target_piece = board[row-i][col-i]
                if target_piece[0] != piece_color:
                    validMoves.append([row-i, col-i])
                break
                
        # Down-Right diagonal
        for i in range(1, 8):
            if row+i >= 8 or col+i >= 8: break
            if board[row+i][col+i] == '':
                validMoves.append([row+i, col+i])
            else:
                target_piece = board[row+i][col+i]
                if target_piece[0] != piece_color:
                    validMoves.append([row+i, col+i])
                break
                
        # Down-Left diagonal
        for i in range(1, 8):
            if row+i >= 8 or col-i < 0: break
            if board[row+i][col-i] == '':
                validMoves.append([row+i, col-i])
            else:
                target_piece = board[row+i][col-i]
                if target_piece[0] != piece_color:
                    validMoves.append([row+i, col-i])
                break
                
        return validMoves

class KnightMoveStrategy(MoveStrategy):

    def getValidMoves(self, piece, position, board):
        row, col = position
        validMoves = []
        piece_color = piece[0]
        
        # All possible L-shaped moves
        moves = [
            [-2,-1], [-2,1],  # Up 2, left/right 1
            [2,-1],  [2,1],   # Down 2, left/right 1
            [-1,-2], [1,-2],  # Left 2, up/down 1
            [-1,2],  [1,2]    # Right 2, up/down 1
        ]
        
        for move in moves:
            newRow = row + move[0]
            newCol = col + move[1]
            if 0 <= newRow < 8 and 0 <= newCol < 8:
                if board[newRow][newCol] == '':
                    validMoves.append([newRow, newCol])
                else:
                    target_piece = board[newRow][newCol]
                    if target_piece[0] != piece_color:
                        validMoves.append([newRow, newCol])
                
        return validMoves

class KingMoveStrategy(MoveStrategy):

    def getValidMoves(self, piece, position, board):
        row, col = position
        validMoves = []
        piece_color = piece[0]
        
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if i == 0 and j == 0: continue
                newRow = row + i
                newCol = col + j
                if 0 <= newRow < 8 and 0 <= newCol < 8:
                    if board[newRow][newCol] == '':
                        validMoves.append([newRow, newCol])
                    else:
                        target_piece = board[newRow][newCol]
                        if target_piece[0] != piece_color:
                            validMoves.append([newRow, newCol])
                    
        return validMoves

class QueenMoveStrategy(MoveStrategy):

    def getValidMoves(self, piece, position, board):
        row, col = position
        validMoves = []
        piece_color = piece[0]
        
        # Horizontal moves (left)
        for newCol in range(col-1, -1, -1):
            if board[row][newCol] == '':
                validMoves.append([row, newCol])
            else:
                target_piece = board[row][newCol]
                if target_piece[0] != piece_color:
                    validMoves.append([row, newCol])
                break
                
        # Horizontal moves (right)
        for newCol in range(col+1, 8):
            if board[row][newCol] == '':
                validMoves.append([row, newCol])
            else:
                target_piece = board[row][newCol]
                if target_piece[0] != piece_color:
                    validMoves.append([row, newCol])
                break
                
        # Vertical moves (up)
        for newRow in range(row-1, -1, -1):
            if board[newRow][col] == '':
                validMoves.append([newRow, col])
            else:
                target_piece = board[newRow][col]
                if target_piece[0] != piece_color:
                    validMoves.append([newRow, col])
                break
                
        # Vertical moves (down)
        for newRow in range(row+1, 8):
            if board[newRow][col] == '':
                validMoves.append([newRow, col])
            else:
                target_piece = board[newRow][col]
                if target_piece[0] != piece_color:
                    validMoves.append([newRow, col])
                break
                
        # Diagonal moves (reusing Bishop logic)
        for i in range(1, 8):
            # Up-Right
            if row-i < 0 or col+i >= 8: break
            if board[row-i][col+i] == '':
                validMoves.append([row-i, col+i])
            else:
                target_piece = board[row-i][col+i]
                if target_piece[0] != piece_color:
                    validMoves.append([row-i, col+i])
                break
                
        for i in range(1, 8):
            # Up-Left
            if row-i < 0 or col-i < 0: break
            if board[row-i][col-i] == '':
                validMoves.append([row-i, col-i])
            else:
                target_piece = board[row-i][col-i]
                if target_piece[0] != piece_color:
                    validMoves.append([row-i, col-i])
                break
                
        for i in range(1, 8):
            # Down-Right
            if row+i >= 8 or col+i >= 8: break
            if board[row+i][col+i] == '':
                validMoves.append([row+i, col+i])
            else:
                target_piece = board[row+i][col+i]
                if target_piece[0] != piece_color:
                    validMoves.append([row+i, col+i])
                break
                
        for i in range(1, 8):
            # Down-Left
            if row+i >= 8 or col-i < 0: break
            if board[row+i][col-i] == '':
                validMoves.append([row+i, col-i])
            else:
                target_piece = board[row+i][col-i]
                if target_piece[0] != piece_color:
                    validMoves.append([row+i, col-i])
                break
                
        return validMoves
