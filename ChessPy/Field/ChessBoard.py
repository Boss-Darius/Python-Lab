from Field import Field

class Board:
    def __init__(self,whitePieces,blackPieces):
        self.whitePieces=whitePieces
        self.blackPieces=blackPieces
        self.BoardFields=[]

        for i in range(0,8):
            for j in range(0,8):
                self.BoardFields+=[Field.BoardField((7-i,j))]




    def __str__(self):
        stringBoard=""
        for i in range(0,8):
            lineShown=""
            for j in range(0,8):
                for whitepiece in self.whitePieces:
                    if (7-i,j)== whitepiece.field.position: lineShown+=" "+str(whitepiece)+" "
                    else: lineShown+= " "+str(self.BoardFields[8*i+j])+" "
                for blackpiece in self.blackPieces:
                    if (7-i, j) == blackpiece.field.position: lineShown += " "+str(blackpiece)+" "
                    else: lineShown+= " "+str(self.BoardFields[8*i+j])+" "

                #lineShown+=" "+str((i+j)%2)+" "
                #lineShown+= " "+str(self.BoardFields[8*i+j])+" "
            stringBoard+= lineShown +'\n'

        return stringBoard


