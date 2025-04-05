from abc import ABC, abstractmethod
from typing import List, Tuple

class MoveStrategy(ABC):
    @abstractmethod
    def getValidMoves(self, piece: str, position: Tuple[int, int], board: List[List[str]]) -> List[List[int]]:
        pass

    def _is_valid_position(self, row: int, col: int) -> bool:
        """Check if position is within board boundaries"""
        return 0 <= row < 8 and 0 <= col < 8

    def _can_capture(self, piece: str, target_piece: str) -> bool:
        """Check if piece can capture target piece (different colors)"""
        return target_piece != '' and piece.color != target_piece.color

    def _get_directional_moves(self, piece: str, position: Tuple[int, int], board: List[List[str]], 
                             directions: List[Tuple[int, int]], max_distance: int = 7) -> List[List[int]]:
        """
        Get valid moves in specified directions up to max_distance
        Used by Queen, Rook, and Bishop
        """
        row, col = position
        valid_moves = []
        
        for dx, dy in directions:
            for distance in range(1, max_distance + 1):
                new_row = row + (dx * distance)
                new_col = col + (dy * distance)
                
                if not self._is_valid_position(new_row, new_col):
                    break
                    
                target_square = board[new_row][new_col]
                if target_square == '':
                    valid_moves.append([new_row, new_col])
                else:
                    if self._can_capture(piece, target_square):
                        valid_moves.append([new_row, new_col])
                    break
        # print(valid_moves)
        return valid_moves

class PawnMoveStrategy(MoveStrategy):
    def getValidMoves(self, piece: str, position: Tuple[int, int], board: List[List[str]]) -> List[List[int]]:
        row, col = position
        valid_moves = []
        direction = 1 if piece.color == 'White' else -1
        start_row = 1 if piece.color == 'White' else 6
        
        # Forward moves
        new_row = row + direction
        if self._is_valid_position(new_row, col) and board[new_row][col] == '':
            valid_moves.append([new_row, col])
            # First move can be 2 squares
            if row == start_row and board[row + 2*direction][col] == '':
                valid_moves.append([row + 2*direction, col])
        
        # Diagonal captures
        for col_offset in [-1, 1]:
            new_col = col + col_offset
            new_row = row + direction
            if self._is_valid_position(new_row, new_col):
                target_square = board[new_row][new_col]
                if self._can_capture(piece, target_square):
                    valid_moves.append([new_row, new_col])
        # print(valid_moves)
        return valid_moves

class RookMoveStrategy(MoveStrategy):
    def getValidMoves(self, piece: str, position: Tuple[int, int], board: List[List[str]]) -> List[List[int]]:
        directions = [
            (-1, 0),  # Up
            (1, 0),   # Down
            (0, -1),  # Left
            (0, 1)    # Right
        ]
        return self._get_directional_moves(piece, position, board, directions)

class BishopMoveStrategy(MoveStrategy):
    def getValidMoves(self, piece: str, position: Tuple[int, int], board: List[List[str]]) -> List[List[int]]:
        directions = [
            (-1, -1),  # Up-left
            (-1, 1),   # Up-right
            (1, -1),   # Down-left
            (1, 1)     # Down-right
        ]
        return self._get_directional_moves(piece, position, board, directions)

class KnightMoveStrategy(MoveStrategy):
    def getValidMoves(self, piece: str, position: Tuple[int, int], board: List[List[str]]) -> List[List[int]]:
        row, col = position
        moves = [
            (-2, -1), (-2, 1),  # Up 2, left/right 1
            (2, -1),  (2, 1),   # Down 2, left/right 1
            (-1, -2), (1, -2),  # Left 2, up/down 1
            (-1, 2),  (1, 2)    # Right 2, up/down 1
        ]
        
        valid_moves = []
        for dx, dy in moves:
            new_row, new_col = row + dx, col + dy
            if self._is_valid_position(new_row, new_col):
                target_square = board[new_row][new_col]
                if target_square == '' or self._can_capture(piece, target_square):
                    valid_moves.append([new_row, new_col])
        
        return valid_moves

class KingMoveStrategy(MoveStrategy):
    def getValidMoves(self, piece: str, position: Tuple[int, int], board: List[List[str]]) -> List[List[int]]:
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]
        return self._get_directional_moves(piece, position, board, directions, max_distance=1)

class QueenMoveStrategy(MoveStrategy):
    def getValidMoves(self, piece: str, position: Tuple[int, int], board: List[List[str]]) -> List[List[int]]:
        directions = [
            (-1, -1), (-1, 0), (-1, 1),  # Up-left, Up, Up-right
            (0, -1),           (0, 1),    # Left, Right
            (1, -1),  (1, 0),  (1, 1)     # Down-left, Down, Down-right
        ]
        return self._get_directional_moves(piece, position, board, directions)


class MoveStrategyFactory:
    @staticmethod
    def get_strategy(piece):
        
        if piece.type == 'Pawn':
            return PawnMoveStrategy()
        elif piece.type == 'Rook':
            return RookMoveStrategy()
        elif piece.type == 'Bishop':
            return BishopMoveStrategy()
        elif piece.type == 'Knight':
            return KnightMoveStrategy()
        elif piece.type == 'Queen':
            return QueenMoveStrategy()
        elif piece.type == 'King':
            return KingMoveStrategy()
        else:
            return None
    
