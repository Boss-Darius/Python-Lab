from Pieces import King


class Player:
    def __init__(self, table, color):
        self.table = table
        self.color = color
        self.currentPiece = None
        self.field = None
        self.king = None
        self.pieces=[]
        print("Set your name : ")
        name = input()
        self.name = name

    def GetPieces(self):
        if self.color == "white":
            self.pieces = self.table.whitePieces
        else:
            self.pieces = self.table.blackPieces

        for piece in self.pieces:
            if isinstance(piece, King.King):
                self.king = piece

    def SelectPiece(self):
        print("select row for piece: ")
        row = int(input())
        print("select column for piece: ")
        col = int(input())
        while True:
            if (0 <= row and row <= 7) and (0 <= col and col <= 7):
                self.currentPiece = self.table.GetPiece(self.table.BoardFields[8 * (7 - (row)) + col])
                if self.currentPiece is None:
                    print("this field has no piece")
                elif self.currentPiece.color != self.color:
                    print("I know it's tempting to control the enemy's pieces but chess won't allow and neither will I")
                elif self.currentPiece.color==self.color and len(self.currentPiece.FilterMoves())==0:
                    print("This piece can't be moved")
                else:
                    break
            print("select a valid row for piece: ")
            row = int(input())
            print("select a valid column for piece: ")
            col = int(input())

    def SelectField(self):
        print("select the row for the field : ")
        row = int(input())

        while not (0 <= row and row <= 7):
            print("select a valid row for the field dude...")
            row = int(input())

        print("select the column for the field : ")
        col = int(input())

        while not (0 <= col and col <= 7):
            print("select a valid rcolumn for the field dude...")
            col = int(input())

        self.field = self.table.BoardFields[8 * (7 - (row)) + col]

    def Move(self):
        print("Selecteaza piesa")
        self.SelectPiece()
        print("Selecteaza campul")
        self.SelectField()
        while True:
            if self.field in self.currentPiece.FilterMoves():
                break
            else:
                print("Selecteaza campul")
                self.SelectField()

        self.currentPiece.Move(self.field, self.currentPiece.FilterMoves())

    def GetMoves(self):
        moves = []
        for piece in self.pieces:
            moves += piece.FilterMoves()

        return moves

    def CheckMated(self):
        return (self.king.InCheck()) and (len(self.GetMoves()) == 0)

    def StaleMated(self):
        return (not self.king.InCheck()) and (len(self.GetMoves()) == 0)
