from typing import Union
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
import os,json,uvicorn

import gameApp

class Item(BaseModel):
    col: int
    row: int


# Run the App using "uvicorn app:app --reload"
game=gameApp.Game()
app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
]



app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def start_game():
    # print(game.board, game.currentPlayer)
    return game.board,game.currentPlayer,game.status

@app.delete("/")
async def reset_board():
    game.clear_board()
    return game.board,game.currentPlayer,game.status
    

@app.post("/")
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
    uvicorn.run("api_config:app", host="127.0.0.1", port=5051, reload=True)