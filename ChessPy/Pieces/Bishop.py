from Pieces import Piece


class Bishop(Piece.Piece):
    def __init__(self, table, position, color):
        self.color = color
        self.table = table
        self.field = self.table.BoardFields[(7 - position[0]) * 8 + position[1]]
        self.table.AddPiece(self)
        self.field.occupied = True

    def PossibleMoves(self):
        possiblemoves = []

        col = self.field.position[1]
        row = self.field.position[0]
        chessboard = self.table.BoardFields

        # cheking if the bishop can move down

        if row != 0:
            r1 = row - 1
            c1 = col - 1
            # down left
            while r1 >= 0 and c1 >= 0:
                if chessboard[8 * (7 - r1) + c1].occupied == False:
                    # print("camp bun")
                    possiblemoves += [chr(65 + c1) + str(r1 + 1)]
                    c1 -= 1
                    r1 -= 1
                else:
                    if self.CanCapture(r1, c1): possiblemoves += [chr(65 + c1) + str(r1 + 1)]
                    break

            r1 = row - 1
            c1 = col + 1
            # down right
            while r1 >= 0 and c1 <= 7:
                if chessboard[8 * (7 - r1) + c1].occupied == False:
                    # print("camp bun")
                    possiblemoves += [chr(65 + c1) + str(r1 + 1)]
                    c1 += 1
                    r1 -= 1
                else:
                    if self.CanCapture(r1, c1): possiblemoves += [chr(65 + c1) + str(r1 + 1)]
                    break
            # checking if the bishop can move up
            if row != 7:
                r1 = row + 1
                c1 = col - 1
                # up left
                while r1 <= 7 and c1 >= 0:
                    if chessboard[8 * (7 - r1) + c1].occupied == False:
                        # print("camp bun")
                        possiblemoves += [chr(65 + c1) + str(r1 + 1)]
                        c1 -= 1
                        r1 += 1
                    else:
                        if self.CanCapture(r1, c1): possiblemoves += [chr(65 + c1) + str(r1 + 1)]
                        break

                r1 = row + 1
                c1 = col + 1
                # up right
                while r1 <= 7 and c1 <= 7:
                    if chessboard[8 * (7 - r1) + c1].occupied == False:
                        # print("camp bun")
                        possiblemoves += [chr(65 + c1) + str(r1 + 1)]
                        c1 += 1
                        r1 += 1
                    else:
                        if self.CanCapture(r1, c1): possiblemoves += [chr(65 + c1) + str(r1 + 1)]
                        break
            return possiblemoves

    def AttackMoves(self):
        possiblemoves = []

        col = self.field.position[1]
        row = self.field.position[0]
        chessboard = self.table.BoardFields

        # cheking if the bishop can move down

        if row != 0:
            r1 = row - 1
            c1 = col - 1
                # down left
            while r1 >= 0 and c1 >= 0:
                if chessboard[8 * (7 - r1) + c1].occupied == False:
                    # print("camp bun")
                    possiblemoves += [chr(65 + c1) + str(r1 + 1)]
                    c1 -= 1
                    r1 -= 1
                else:
                    possiblemoves += [chr(65 + c1) + str(r1 + 1)]
                    break

            r1 = row - 1
            c1 = col + 1
            # down right
            while r1 >= 0 and c1 <= 7:
                if chessboard[8 * (7 - r1) + c1].occupied == False:
                        # print("camp bun")
                    possiblemoves += [chr(65 + c1) + str(r1 + 1)]
                    c1 += 1
                    r1 -= 1
                else:
                    possiblemoves += [chr(65 + c1) + str(r1 + 1)]
                    break
                # checking if the bishop can move up
            if row != 7:
                r1 = row + 1
                c1 = col - 1
                # up left
                while r1 <= 7 and c1 >= 0:
                    if chessboard[8 * (7 - r1) + c1].occupied == False:
                        # print("camp bun")
                        possiblemoves += [chr(65 + c1) + str(r1 + 1)]
                        c1 -= 1
                        r1 += 1
                    else:
                        possiblemoves += [chr(65 + c1) + str(r1 + 1)]
                        break

                r1 = row + 1
                c1 = col + 1
                # up right
                while r1 <= 7 and c1 <= 7:
                    if chessboard[8 * (7 - r1) + c1].occupied == False:
                         # print("camp bun")
                        possiblemoves += [chr(65 + c1) + str(r1 + 1)]
                        c1 += 1
                        r1 += 1
                    else:
                        possiblemoves += [chr(65 + c1) + str(r1 + 1)]
                        break
            return possiblemoves
    def Move(self, newfield):
        if str(newfield) in self.PossibleMoves():
            if newfield.occupied:
                self.table.RemovePiece(self.table.GetPiece(newfield))
            self.field.ChangeStatus()
            self.field = newfield
            newfield.ChangeStatus()
        else:
            print("That is not a correct move for the bishop")

    def __str__(self):
        if self.color == "white": return "♗"
        return "♝"
