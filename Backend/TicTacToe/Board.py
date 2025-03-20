class Board:

    def __init__(self):
        self.board=[[" " for i in range(3)]for j in range(3)]


    def clear(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j]=" "