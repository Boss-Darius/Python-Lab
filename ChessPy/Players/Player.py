
from Pieces import King

class Player:
    def __init__(self,table,color):
        self.table=table
        self.color=color
        self.currentPiece=None

    def GetPieces(self):
        if self.color=="white":
            self.pieces=self.table.whitePieces
        else:
            self.pieces=self.table.blackPieces

        for piece in self.pieces:
            if isinstance(piece,King.King):
                self.king=piece

    def SelectPiece(self):
        print("select row for piece: ")
        row=int(input())
        print("select column for piece: ")
        col=int(input())
        while True:
            self.currentPiece=self.table.GetPiece(self.table.BoardFields[8*(7-(row))+col])
            if self.currentPiece is None:
                print("this field has no piece")
            elif self.currentPiece.color!= self.color :
                print("I know it's tempting to control the enemy's pieces but chess won't allow and so neither will I")
            else:
                break
    def Move(self,field):
        self.currentPiece.Move(field)

