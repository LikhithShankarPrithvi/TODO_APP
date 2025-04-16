from typing import Union
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import APIRouter
import os,json,uvicorn

from TicTacToe.gameApp import Game

class Item(BaseModel):
    col: int
    row: int


# Run the App using "uvicorn app:app --reload"
game=Game()
router = APIRouter()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
]





@router.get("/")
def start_game():
    # print(game.board, game.currentPlayer)
    return game.board,game.currentPlayer,game.status

@router.delete("/")
async def reset_board():
    game.clear_board()
    return game.board,game.currentPlayer,game.status
    

@router.post("/")
async def update_board(item: Item):
    print(item.col,item.row)
    if game.update(game.currentPlayer,item.col,item.row):
        win_status=game.check_win()
        draw_status=game.check_draw()
        if not win_status and not draw_status:
            game.change_player()
        if win_status:
            game.status='Victory'
        if draw_status:
            game.status='Draw'
    return game.board,game.currentPlayer,game.status

if __name__ == "__main__":
    uvicorn.run("api_config:router", host="127.0.0.1", port=5051, reload=True)