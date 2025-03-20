from typing import Union
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
import os,json,uvicorn

import gameApp



# Run the App using "uvicorn app:app --reload"

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
    game=gameApp.Game()
    # print(game.board, game.currentPlayer)
    return game.board,game.currentPlayer,game_status

# @app.delete("/{item_id}")
# async def delete_item(item_id: int):
#     for each in ToDoList:
#         if(each['id']==item_id):
#             ToDoList.remove(each)
#             with open('data.json','w') as outfile:
#                 json.dump(ToDoList,outfile)
#             return ToDoList
#     return ToDoList
    

@app.post("/")
async def update_board(colIndex,rowIndex):

    return 

if __name__ == "__main__":
    uvicorn.run("api_config:app", host="127.0.0.1", port=5051, reload=True)