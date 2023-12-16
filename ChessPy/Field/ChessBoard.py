from Field import Field

class Board:
    def __init__(self,whitePieces,blackPieces):
        self.whitePieces=whitePieces
        self.blackPieces=blackPieces
        self.BoardFields=[]

        for i in range(0,8):
            for j in range(0,8):
                self.BoardFields+=[Field.BoardField((7-i,j))]

    def AddPiece(self,piece):
        if piece.color=="white":
            self.whitePieces+=[piece]
        else:
            self.blackPieces+=[piece]

    #functie de debug
    #verific daca se modifica pozitia pieselor albe pe tabla
    def CheckWhitePiecesFields(self):
        print(self.whitePieces)
        for i in range(0,len(self.whitePieces)):
            print(self.whitePieces[i],' ',self.whitePieces[i].field.occupied)
    #functie de debug
    #verific ca nu cumva o piesa sa mentina un camp ocupat dupa ce a parasit acel camp
    def OccupiedField(self):
        fieldstring=""
        for i in range(0,8):
            for j in range(0,8):
                if self.BoardFields[(7-i)*8 + j].occupied==True:
                    fieldstring+=str(self.BoardFields[(7-i)*8 + j])+" "

        return fieldstring

    def __str__(self):
        stringBoard=""
        whitepiecespositions=[]
        blackpiecespositions=[]
        for i in range(0,8):
            lineShown=""
            for j in range(0,8):
                for whitepiece in self.whitePieces:
                    if (7-i,j)== whitepiece.field.position:
                        lineShown+=" "+str(whitepiece)+" "
                        whitepiecespositions+=[whitepiece.field.position]
                for blackpiece in self.blackPieces:
                    if (7-i, j) == blackpiece.field.position:
                        lineShown += " "+str(blackpiece)+" "
                        blackpiecespositions+=[blackpiece.field.position]

                if ((7-i,j) not in whitepiecespositions) and ((7-i,j) not in blackpiecespositions) :
                    lineShown+= " "+str(self.BoardFields[8*i+j])+" "
            stringBoard+= lineShown +'\n'
        return stringBoard


