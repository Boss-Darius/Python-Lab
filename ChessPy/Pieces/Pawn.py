from Pieces import  Piece

class Pawn(Piece.Piece):
    def __init__(self,table,position,color):
        self.color = color
        self.table=table
        self.field = self.table.BoardFields[(7-position[0])*8+position[1]]
        self.table.AddPiece(self)
        self.field.occupied = True
        self.moved=False

    def PossibleMoves(self):

        possibleMoves=[]
        row = self.field.position[0]
        col= self.field.position[1]
        chessboard=self.table.BoardFields
        # the white pawn can only move up
        if self.color == "white":
            #the pawn hasn't been moved, it can move 2 squares instead of one
            if row==1 and self.moved==False and (chessboard[8*(7-row-1)+col].occupied==False and chessboard[8*(7-row-2)+col].occupied==False):
                print(7-row+1,' ',col)
                print(7-row+2,' ',col)
                possibleMoves+=[chr(65+col)+str(row+3)]

            if (row!=7) and (chessboard[8*(7-row-1)+col].occupied==False):
                possibleMoves+=[chr(65+col)+str(row+2)]
        # the blackPawn can only move down
        else:

            if row==6 and self.moved==False:
                possibleMoves+=[chr(65+col)+str(row-1)]
            if row!=0:
                possibleMoves+=[chr(65+col)+str(row)]

        return possibleMoves

    def Move(self,newfield):
        if str(newfield) in self.PossibleMoves():
            self.field.ChangeStatus()
            self.field = newfield
            newfield.ChangeStatus()
        else:
            print("that is not a correct move dor the pawn")

    def __str__(self):
        return "p "


