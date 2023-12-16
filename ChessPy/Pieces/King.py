from Pieces import Piece
class King(Piece.Piece):
    def __init__(self,table,position,color):
        self.color = color
        self.table=table
        self.field = self.table.BoardFields[(7-position[0])*8+position[1]]
        self.table.AddPiece(self)
        self.field.occupied = True
        self.moved=False
        self.canCastle=True

    def PossibleMoves(self):
        moves=[]
        row=self.field.position[0]
        col=self.field.position[1]
        chessboard=self.table.BoardFields

        #checking if the king can move down
        if(col!=0):
            # move down
            if chessboard[8*(7-row)+col-1].occupied==False:
                moves += [chr(65 + col - 1) + str(row+1)]
            # move down left
            if(row!=0) and (chessboard[8*(7-(row-1))+col-1].occupied==False):
                moves += [chr(65 + col - 1) + str(row)]
            # move down right
            if (row != 7) and chessboard[8*(7-(row+1))+col-1].occupied==False:
                moves += [chr(65 + col - 1) + str(row+2)]
        #
        # checking if the king can move up
        if (col != 7):
            # move up
            if chessboard[8*(7-row)+col+1].occupied==False:
                moves += [chr(65 + col + 1) + str(row+1)]
            # move up left
            if (row != 0) and (chessboard[8*(7-(row-1))+col+1].occupied==False):
                moves += [chr(65 + col + 1) + str(row)]

            # move up right
            if (row != 7) and chessboard[8*(7-(row+1))+col+1].occupied==False:
                moves += [chr(65 + col+1) + str(row+2)]

        #checking if the king can move to the right
        if (row!=7) and chessboard[8*(7-(row+1))+col].occupied==False: moves+=[chr(65+col)+str(row+2)] #moving right
        #checking if the king can move to the left
        if(row!=0) and chessboard[8*(7-(row-1))+col+1].occupied==False: moves += [chr(65+col)+str(row)] #moving left

        return moves

    def Move(self,newfield):
        if str(newfield) in self.PossibleMoves():
                self.field.ChangeStatus()
                self.field = newfield
                newfield.ChangeStatus()
                self.moved=True
                self.canCastle=False

        else:
            print("That is not a correct move for the king")
    def __str__(self):
        return 'K '

