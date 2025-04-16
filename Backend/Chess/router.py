from typing import Union
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi import APIRouter
from pydantic import BaseModel
import os,json,uvicorn

from Chess.chessGame import Chess


# Run the App using "uvicorn app:app --reload"
game=Chess()
router = APIRouter()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
]




class PositionRequest(BaseModel):
    position: tuple[int, int]

class MoveRequest(BaseModel):
    old_position: tuple[int, int]
    new_position: tuple[int, int]


@router.post("/get_possible_moves")
async def get_possible_moves(request: PositionRequest):
    """API to return possible moves for a selected chess piece."""
    position = request.position
    possible_moves = game.get_valid_moves(position)

    if possible_moves is None:
        raise HTTPException(status_code=400, detail="Invalid position or no piece at given position")

    return {"position": position, "possible_moves": possible_moves}

@router.post("/move_piece")
async def move_piece(request: MoveRequest):
    """API to move a chess piece."""
    killStatus = game.move_piece(request.old_position, request.new_position)
    game.changePlayer()
    # if not success:
    #     raise HTTPException(status_code=400, detail=message)
    board=game.board.get_board_state()
    return {"killStatus": killStatus,"board":board,"player":game.currentPlayer}


@router.get("/")
def start_game():
    # return 1
    # game.board.newBoard()
    return game.board.get_board_state(),game.currentPlayer,game.status

@router.get("/new_game")
def new_game():
    game.board.newBoard()
    return game.board.get_board_state(),game.currentPlayer,game.status

# @router.delete("/")
# async def reset_board():
#     game.clear_board()
#     return game.board,game.currentPlayer,game.status
    

# @router.post("/")
# async def update_board(item: Item):
#     print(item.col,item.row)
#     if game.update(game.currentPlayer,item.col,item.row):
#         win_status=game.check_win()
#         draw_status=game.check_draw()
#         if not win_status and not draw_status:
#             game.change_player()
#         if win_status:
#             game.status='Victory'
#         if draw_status:
#             game.status='Draw'
#     return game.board,game.currentPlayer,game.status

if __name__ == "__main__":
    uvicorn.run("chessAppController:router", host="127.0.0.1", port=8000, reload=True)