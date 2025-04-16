from fastapi import FastAPI
# from fastapi.responses import ORJSONResponse
from fastapi.middleware.cors import CORSMiddleware

from todoRouter import router as todo_router
from Chess.router import router as chess_router
from TicTacToe.router import router as ttt_router



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(todo_router, prefix="/todo")
app.include_router(chess_router, prefix="/chess")
app.include_router(ttt_router, prefix="/tictactoe")



