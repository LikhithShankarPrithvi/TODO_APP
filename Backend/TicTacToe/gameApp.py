# from typing import Union
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi import FastAPI
# from pydantic import BaseModel
# import os,json,uvicorn


class Game:


    def __init__(self):
        self.board=[[" " for i in range(3)]for j in range(3)]
        self.player1='Player1'
        self.player2='Player2'
        self.currentPlayer=self.player1
        self.status="progress"

    def clear_board(self):
        self.board=[[" " for i in range(3)]for j in range(3)]
        self.player1='Player1'
        self.player2='Player2'
        self.currentPlayer=self.player1
        self.status="progress"

    def change_player(self):
        if self.currentPlayer==self.player1:
            self.currentPlayer=self.player2
        elif self.currentPlayer==self.player2:
            self.currentPlayer=self.player1
    
    def update(self,player,rowIndex,colIndex):
        x=rowIndex
        y=colIndex
        if self.board[x][y]!=" ":
            return False


        if player==self.player1:
            self.board[x][y]='X'
        elif player==self.player2:
            self.board[x][y]='O'
        return True
    def check_draw(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j]==" ":
                    return False
        if self.status=='progress':
            return True
        return False
    def check_win(self):
        for i in range(3):
            if self.board[i][0]==self.board[i][1]==self.board[i][2]:
                if self.board[i][0]=='X' or self.board[i][0]=='O':
                    return True
            elif self.board[0][i]==self.board[1][i]==self.board[2][i]:
                if self.board[0][i]=='X' or self.board[0][i]=='O':
                    return True
        if self.board[1][1]==self.board[0][0]==self.board[2][2]:
            if self.board[1][1]=='X' or self.board[1][1]=='O':
                    return True

        if self.board[1][1]==self.board[0][2]==self.board[2][0]:
            if self.board[1][1]=='X' or self.board[1][1]=='O':
                    return True
        return False


    def print_board(self):
        for i in range(3):
            print(self.board[i])


    def start(self):
        while True:
            self.print_board()
            print(self.currentPlayer,"select a block")
            print("each block has designations as 1,2,3,4,5,6,7,8,9")
            position=int(input())


            while not self.update(self.currentPlayer,position):
                print("invalid Move")
                position=int(input())

            if self.check_win():
                print(self.board)
                print(self.currentPlayer, "You Won !!!")
                break


            if self.currentPlayer==self.player1:
                self.currentPlayer=self.player2
            elif self.currentPlayer==self.player2:
                self.currentPlayer=self.player1



# app = FastAPI()

# origins = [
#     "http://localhost.tiangolo.com",
#     "https://localhost.tiangolo.com",
#     "http://localhost",
#     "http://localhost:3000",
# ]



# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# @app.get("/")
# def start_game():
#     game=Game()
#     print(game.board, game.currentPlayer)
#     return 1

# game = Game()
# # game.print_board()
# game.start()


# if __name__ == "__main__":
#     uvicorn.run("gameApp:app", host="127.0.0.1", port=5051, reload=True)