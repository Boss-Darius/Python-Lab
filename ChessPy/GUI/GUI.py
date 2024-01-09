import tkinter as tk
import Pieces
from Pieces import King
from Pieces import Pawn
from Pieces import Bishop
from Pieces import Knight
from Pieces import Rook
from Pieces import Queen
import Pieces.Pawn
from Field import ChessBoard
from PIL import ImageTk, Image
from Players import Player, AI
import copy


class GUI:
    # contructor pentru interfata grafica
    # initializeaza fereastra pentru setarea jucatorilor si dupa
    # reseteaza fereastra pentru a incepe jocul de sah
    def __init__(self):
        self.board = ChessBoard.Board()
        self.previousPositions = []
        # adding the players
        self.currentPlayer = None
        self.firstPlayer = None
        self.secondPlayer = None

        self.playAsWhite = True
        self.playWithFriend = False

        self.window = tk.Tk()
        self.window.title("ChessPy")
        self.window.iconbitmap("Images/iconita.ico")
        self.window.geometry("700x700")

        # storing the images in a dictionary
        self.images = {}

        for piece in self.board.whitePieces:
            piece_image = Image.open(piece.Image())
            piece_image1 = piece_image.resize((80, 80), Image.LANCZOS)
            piece_image2 = ImageTk.PhotoImage(piece_image1)
            self.images[str(piece)] = piece_image2

        for piece in self.board.blackPieces:
            piece_image = Image.open(piece.Image())
            piece_image = piece_image.resize((80, 80), Image.LANCZOS)
            piece_image = ImageTk.PhotoImage(piece_image)
            self.images[str(piece)] = piece_image
        # adding the background
        bg = tk.PhotoImage(file="Images/Tabla.png")

        self.canvas = tk.Canvas(self.window, width=700, height=700)
        self.canvas.pack(fill="both", expand=True)

        self.canvas.create_image(0, 0, image=bg, anchor="nw")
        self.canvas.create_text(350, 125, text="Welcome to ChessPy", font=("Helvetica", 50), fill="red")

        self.canvas.create_text(350, 250, text="Seteazati numele", font=("Helvetica", 30), fill="red")

        self.entry1 = tk.Entry(self.window)

        self.canvas.create_window(300, 300, anchor="nw", window=self.entry1)

        self.canvas.create_text(350, 550, text="Numele Adversarului", font=("Helvetica", 30), fill="red")

        self.entry2 = tk.Entry(self.window)

        self.canvas.create_window(300, 600, anchor="nw", window=self.entry2)

        self.canvas.create_text(350, 200, text="Joaca ca:", font=("Helvetica", 30), fill="red")

        self.canvas.create_text(100, 220, text="Albul", font=("Helvetica", 30), fill="white")
        self.canvas.create_text(600, 220, text="Negrul", font=("Helvetica", 30), fill="black")
        self.canvas.create_text(350, 400, text="Joaca impotriva :", font=("Helvica", 30), fill="red")
        # creating buttons

        # creating the image for the button

        imagine1 = Image.open("Images/rege alb2.png")

        imagineRedimensionata1 = imagine1.resize((75, 75), Image.LANCZOS)

        conversie1 = ImageTk.PhotoImage(imagineRedimensionata1)

        # adding the button

        selectWhiteButton = tk.Button(self.window, image=conversie1, command=self.WhiteKingButton)

        self.canvas.create_window(65, 270, anchor="nw", window=selectWhiteButton)

        # creating the image for the button

        imagine2 = Image.open("Images/rege negru2.png")

        imagineRedimensionata2 = imagine2.resize((75, 75), Image.LANCZOS)

        conversie2 = ImageTk.PhotoImage(imagineRedimensionata2)

        # adding the button

        selectBlackButton = tk.Button(self.window, image=conversie2, command=self.BlackKingButton)

        self.canvas.create_window(575, 270, anchor="nw", window=selectBlackButton)

        # adding button for choosing enemy player:

        enemyPlayerButton = tk.Button(self.window, text="Altui jucator", height=5, width=10, background="yellow",
                                      command=self.PlayWithFriend)
        self.canvas.create_window(65, 500, anchor="nw", window=enemyPlayerButton)

        # adding button for choosing ai
        AIPlayerButton = tk.Button(self.window, text="Unui AI", height=5, width=10, background="yellow",
                                   command=self.PlayWithAI)
        self.canvas.create_window(575, 500, anchor="nw", window=AIPlayerButton)

        gameButton = tk.Button(self.window, text="Incepe jocul", height=5, width=10, background="black",
                               foreground="white", command=self.CreateGame)
        self.canvas.create_window(550, 600, anchor="nw", window=gameButton)

        self.window.mainloop()

    # schimba jucatorul curent
    def SwitchPlayer(self):
        if self.currentPlayer == self.firstPlayer:
            self.currentPlayer = self.secondPlayer
        else:
            self.currentPlayer = self.firstPlayer

        print(self.currentPlayer.name + " este acum la mutare")

    # verifica ce jucator are albul si ce jucator are negrul
    # si initializeaza jocul de sah

    def CreateGame(self):
        if self.playAsWhite:

            self.firstPlayer = Player.Player(self.board, "white")
            self.currentPlayer = self.firstPlayer

            name = self.entry1.get()

            if name == "":
                print("vei juca ca albul")
                self.firstPlayer.SetName("Albul")
            else:
                self.firstPlayer.SetName(name)
                print(name + " ! vei juca ca albul")

            if self.playWithFriend:
                self.secondPlayer = Player.Player(self.board, "black")

                name = self.entry2.get()
                if name == "":
                    print("Jicatorul doi va juca ca negrul")
                    self.secondPlayer.SetName("Negrul")
                else:
                    self.secondPlayer.SetName(name)
                    print(name + " ! vei juca ca negrul")

            else:
                self.secondPlayer = AI.AI(self.board, "black")
                name = self.entry2.get()

                if name != "": self.secondPlayer.SetName(name)

                print(self.secondPlayer.name + " va juca ca negrul")
        # ai ales sa joci ca negru
        else:
            self.firstPlayer = Player.Player(self.board, "black")

            name = self.entry1.get()

            if name == "":
                print("vei juca ca negrul")
                self.firstPlayer.SetName("Negrul")
            else:
                self.firstPlayer.SetName(name)
                print(name + " ! vei juca ca negrul")

            if self.playWithFriend:
                self.secondPlayer = Player.Player(self.board, "white")
                self.currentPlayer = self.secondPlayer
                name = self.entry2.get()
                if name == "":
                    print("Jucatorul doi va juca ca albulul")
                    self.secondPlayer.SetName("Albul")
                else:
                    self.secondPlayer.SetName(name)
                    print(name + " ! vei juca ca albul")

            else:
                self.secondPlayer = AI.AI(self.board, "white")
                self.currentPlayer = self.secondPlayer
                name = self.entry2.get()

                if name != "": self.secondPlayer.SetName(name)

                print(self.secondPlayer.name + " va juca ca albul")

        print(self.currentPlayer.name + " joaca primul")

        self.ResetWindow()
        print("ia sa vedem ce piese avem")

    # seteaza flag-ul pentru ca utilizatorul sa joace cu albul
    def WhiteKingButton(self):
        print("vei juca ca albul")
        self.playAsWhite = True

    # seteaza flag-ul pentru ca utilizatorul sa joace cu negrul
    def BlackKingButton(self):
        print("vei juca ca negrul")
        self.playAsWhite = False

    # seteaza flag-ul pentru ca utilizatorul sa joace cu un bot
    def PlayWithAI(self):
        print("vei juca cu un AI")
        self.playWithFriend = False

    # seteaza flag-ul pentru ca utilizatorul sa joace cu alt utilizator
    def PlayWithFriend(self):
        print("Vei juca cu un prieten (sper ca tie prieten)")
        self.playWithFriend = True

    # sterge fereastra de initializare a jocului si o creeaza pe cea pentru joc
    def ResetWindow(self):
        self.canvas.delete("all")

        imagine1 = Image.open("Images/rege alb2.png")

        imagineRedimensionata1 = imagine1.resize((75, 75), Image.LANCZOS)

        self.whiteKing = ImageTk.PhotoImage(imagineRedimensionata1)
        self.blackKing = ImageTk.PhotoImage(Image.open("Images/rege negru2.png").resize((75, 75), Image.LANCZOS))
        self.whiteQueen = ImageTk.PhotoImage(Image.open("Images/regina alba2.png").resize((75, 75), Image.LANCZOS))

        self.DisplayBoard()

        self.state = "select-piece"
        # self.canvas.create_image(0, 0, image=bg, anchor="nw")

    # creeaza grid-ul pentru tabla de sah
    def DisplayBoard(self):
        for row in range(8):
            for col in range(8):
                color = "#FFF2BD" if (row + col) % 2 == 0 else "#744C29"
                x1, y1 = col * 87.5, row * 87.5
                x2, y2 = x1 + 87.5, y1 + 87.5

                self.canvas.create_rectangle([x1, y1], [x2, y2], outline="black", width=1, fill=color,
                                             tags=f"square_{row}_{col}")

                self.canvas.tag_bind(f"square_{row}_{col}", "<Button-1>",
                                     lambda event, r=row, c=col: self.ClickField(r, c))

        self.DisplayPieces()

    # preia piesa de pe camplul respectiv sau muta piesa jucatorului curent pe campul respectiv
    def ClickField(self, row, col):

        self.currentPlayer.GetPieces()
        print(self.currentPlayer.name + " este la mutare! si are piesele")

        for piece in self.currentPlayer.pieces:
            posibilities = [str(field) for field in piece.FilterMoves()]
            print(str(piece) + " " + str(piece.field), ' ', posibilities)
        print("starea este : ", self.state)
        print(row, ' ', col, ' ', str(self.board.GetPiece(self.board.BoardFields[8 * ((row)) + col])), " ",
              self.board.BoardFields[8 * ((row)) + col].occupied)
        # Daca muta AI-ul nu mai e nevoie sa selectez piesa sau campul
        if isinstance(self.currentPlayer, AI.AI):
            self.MoveForPlayer()
        # In schimb pentru jucator am nevoie
        else:
            if self.state == "select-piece":
                print("N-ai ales piesa inca")
                result = self.currentPlayer.SelectPiece(row, col)
                if result == True:
                    self.state = "select-field"
                else:
                    self.state = "select-piece"

                print("starea este : ", self.state)
            #
            elif self.state == "select-field":

                print("field at (", row, " ", col, ")")
                if self.board.BoardFields[8 * (row) + col] in self.currentPlayer.currentPiece.FilterMoves():
                    print("poti muta acolo " + str(self.board.BoardFields[8 * (row) + col]))

                    # setam field-ul jucatorului curent
                    self.currentPlayer.field = self.board.BoardFields[8 * (row) + col]
                    self.MoveForPlayer()
                    print("starea este : ", self.state)
                #
                else:
                    print("nu poti muta acolo")
                    print("Campul este ", str(self.board.BoardFields[8 * ((row)) + col]))
                    self.state = "select-field"
                    print("starea este : ", self.state)

    # selecteaza piesa pentru jucatorul curent sau captureaza piesa adversa
    def ClickPiece(self, row, col):
        print(self.currentPlayer.name + " este la mutare! si are piesele")

        self.currentPlayer.GetPieces()
        print("starea este : ", self.state)
        print(row, " ", col)
        # Handle the click event for the piece at the specified row and column
        print(
            f"Piece({str(self.board.GetPiece(self.board.BoardFields[8 * ((row)) + col]))}) clicked at row {7 - row}, column {col}")
        print("Campul este ", str(self.board.BoardFields[8 * ((row)) + col]))
        # Daca muta AI-ul nu mai am nevoie de selectarea pieselor
        if isinstance(self.currentPlayer, AI.AI):
            self.MoveForPlayer()
        # Dar pentru un jucator da
        else:
            if self.state == "select-piece":
                print("n-am piesa selectata. O alegem acum")
                result = self.currentPlayer.SelectPiece(7 - row, col)
                print(f"{result} {self.currentPlayer.name} a ales : ", self.currentPlayer.currentPiece)
                #
                if result == True:
                    self.state = "select-field"

                else:
                    print("Campul este ", str(self.board.BoardFields[8 * ((row)) + col]))
                    self.state = "select-piece"
                #
                print("starea este : ", self.state)
            elif self.state == "select-field":
                print("Am ales deja piesa. O mut peste piesa asta")
                if self.board.BoardFields[8 * (row) + col] in self.currentPlayer.currentPiece.FilterMoves():
                    print("pot muta piesa acolo" + str(self.board.BoardFields[8 * (7 - row) + col]))
                    self.currentPlayer.field = self.board.BoardFields[8 * (row) + col]
                    # setam field-ul jucatorului curent
                    self.MoveForPlayer()
                    print("starea este : ", self.state)
                else:
                    print("nu poti muta acolo")
                    print("Campul este ", str(self.board.BoardFields[8 * ((row)) + col]))
                    self.state = "select-field"
                    print("starea este : ", self.state)
            #         self.state="select-field"
            #     # self.currentPlayer.field=self.board.BoardFields[8*(row)+col]

    # afiseaza piesele de sah pe campurile pe care se afla
    def DisplayPieces(self):
        square_size = 87.5
        for row in range(8):
            for col in range(8):
                square_center_x = col * square_size + square_size // 2
                square_center_y = row * square_size + square_size // 2

                piece = self.board.GetPiece(self.board.BoardFields[8 * row + col])

                if piece:
                    piece_image = self.images[str(piece)]
                    piece_tag = f"piece_{row}_{col}"
                    self.canvas.create_image(square_center_x, square_center_y, image=piece_image, anchor="c",
                                             tags=piece_tag)
                    self.canvas.tag_bind(piece_tag, "<Button-1>", lambda event, r=row, c=col: self.ClickPiece(r, c))

    # verifica daca jucatorul curent este AI sau utilizator
    # efectueaza mutarea pentru jucator
    def MoveForPlayer(self):
        print("am intrat in move Player")
        if isinstance(self.currentPlayer, AI.AI):
            # AI-ul va muta

            self.currentPlayer.Move()
        else:
            # muta jucatorul
            # self.currentPlayer.field = self.board.BoardFields[8 * (row) + col]
            # mutam piesa
            self.currentPlayer.currentPiece.Move(self.currentPlayer.field,
                                                 self.currentPlayer.currentPiece.FilterMoves())
        # checking if the player has promoted a pawn

        if isinstance(self.currentPlayer.currentPiece, Pieces.Pawn.Pawn):
            if self.currentPlayer.currentPiece.promoted:
                self.CreateSelectionForPromotion()

        self.previousPositions += [str(self.board)]
        self.SwitchPlayer()

        self.ResetWindow()

        self.currentPlayer.GetPieces()
        # afisam mutarea si scimbam jucatorul
        print("Verific daca jucatorul e in remiza")
        if self.ThreeHoldRule():
            self.canvas.create_text(300, 350,
                                    text="Remiza: 3 pozitii identice",
                                    font=("Helvetica", 30), fill="red")
            self.state = "game-ended"
        if self.board.noCaptureCount == 50:
            self.canvas.create_text(300, 350,
                                    text="Remiza: 50 de mutari fara capturi",
                                    font=("Helvetica", 30), fill="red")
            self.state = "game-ended"
        if self.currentPlayer.StaleMated():
            print("Juvatorul e in remiza")
            self.canvas.create_text(300, 350,
                                    text="Pat :/",
                                    font=("Helvetica", 30), fill="red")
            self.state = "game-ended"
        if self.currentPlayer.CheckMated():
            # utilizatorul pierde
            if self.currentPlayer == self.firstPlayer:
                self.canvas.create_text(300, 350,
                                        text=self.secondPlayer.name + " a casitigat! " + self.firstPlayer.name + " a pierdut. :(",
                                        font=("Helvetica", 20), fill="red")
                self.state = "game-ended"
            else:
                self.canvas.create_text(300, 350,
                                        text=self.firstPlayer.name + " a casitigat! " + self.secondPlayer.name + " a pierdut. :(",
                                        font=("Helvetica", 20), fill="red")
            self.state = "game-ended"

        else:
            # Resetam campul Enpassant pentru pionul care putea fi capturat astfel
            # dar pe care adversarul nu l-a luat asa
            for piece in self.currentPlayer.pieces:
                if isinstance(piece, Pieces.Pawn.Pawn) and piece.Enpassant:
                    piece.Enpassant = False
                    break
            self.state = "select-piece"
            # print("starea este : ", self.state)

    # creaza fereastra pentru promovarea pionului
    def CreateSelectionForPromotion(self):
        print("Promovam pionul lui " + self.currentPlayer.name)
        print(self.currentPlayer.currentPiece, " ", self.currentPlayer.currentPiece.field)
        self.selectionMenu = tk.Toplevel(self.window)
        self.selectionMenu.title("Pawn Promotion")
        self.selectionMenu.iconbitmap("Images/iconita.ico")

        label = tk.Label(self.selectionMenu, text="Promote this bastard to:")
        label.pack(pady=10)

        self.selectionMenu.grab_set()

        # adding the buttons:
        if self.currentPlayer.color == "white":

            button_images = ["♕", "♖", "♗", "♘"]

        else:
            button_images = ["♛", "♜", "♝", "♞"]
        for i, image in enumerate(button_images, start=1):
            button = tk.Button(self.selectionMenu, image=self.images[image], command=lambda t=i: self.Promotion(t))
            button.pack()

        self.window.wait_window(self.selectionMenu)

    # promoveaza pionul in piesa aleasa de jucator prin apasarea butonului din fereastra de selectie
    def Promotion(self, piece):
        field = self.currentPlayer.currentPiece.field
        print("Alegem noua piesa pentru: " + self.currentPlayer.name)
        print(self.currentPlayer.currentPiece, " ", self.currentPlayer.currentPiece.field)
        if piece == 1: Pieces.Queen.Queen(self.board, self.currentPlayer.currentPiece.field.position,
                                          self.currentPlayer.color)
        if piece == 2: Pieces.Rook.Rook(self.board, self.currentPlayer.currentPiece.field.position,
                                        self.currentPlayer.color)
        if piece == 3: Pieces.Bishop.Bishop(self.board, self.currentPlayer.currentPiece.field.position,
                                            self.currentPlayer.color)
        if piece == 4: Pieces.Knight.Knight(self.board, self.currentPlayer.currentPiece.field.position,
                                            self.currentPlayer.color)

        # print("campul e acum ocupat? ",field.occupied)
        self.board.RemovePiece(self.currentPlayer.currentPiece)
        # print("campul e acum ocupat2? ",field.occupied)
        field.ChangeStatus()
        self.selectionMenu.destroy()

    # verifica daca nu s-au repetat 3 pozitii pana in momentul curent
    def ThreeHoldRule(self):
        # print("regula de 3 mutari")
        # print(self.previousPositions)
        for position in self.previousPositions:
            # print(position)
            # print(self.previousPositions.count(position))
            if self.previousPositions.count(position) == 3:
                return True
        return False
