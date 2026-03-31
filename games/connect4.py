import numpy as np
class Connect4:
    def __init__(self,array,rows,columns):
        self.rows=7
        self.columns=7
        self.array=np.zeros((rows,columns))
    def Valid_Move(self,x,y,s):
        if self.array[x][y-1]=="X" or self.array[x][y-1]=="O":
            self.array[x][y-1]=s
            return true
        else:
            return false
    



