def test():
    print("Using Checkmate Module,,,,,")
    print("Hello there!")

class chessGame:

    dfb = '''\
........
........
........
........
...K....
........
........
........
\
'''
    def __init__(self, board = dfb) -> None:
        self.board = board
        self.__Boardsta()

        if self.ValidateBoard():
            print("Valid Board Continue The Game...")
        else:
            print("Invalid Board Size It need to be Same Dimention in X,Y")
            exit()

        self.boardSize = len(self.Barr)

    def printboard(self):

        for i in self.Barr:

            for j in i:
                print(j,end='')
            print()

    def ReadPiece(self):

        self.rook = []
        self.bishop = []
        self.queen = []
        self.pawn = []
        self.knight = []
        
        for yCord,yList in enumerate(self.Barr):

            for xCord,bVal in enumerate(yList):

                if bVal == 'K':
                    pass

                elif bVal == 'R':

                    rooktmp = Rook(xCord,yCord,self.boardSize,self.Barr,"white")
                    self.rook.append(rooktmp)

                elif bVal == 'B':

                    bishoptmp = Bishop(xCord,yCord,self.boardSize,self.Barr,"white")
                    self.bishop.append(bishoptmp)
                
                elif bVal == 'Q':

                    queentmp = Queen(xCord,yCord,self.boardSize,self.Barr,"white")
                    self.ueen.append(queentmp)
                
                elif bVal == 'P':
                    pass

                    pawntmp = Pawn(xCord,yCord,self.boardSize,self.Barr,"white")
                    self.pawn.append(pawntmp)

                elif bVal == 'N':

                    knighttmp = Knight(xCord,yCord,self.boardSize,self.Barr,"white")
                    self.knight.append(knighttmp)

                elif bVal == '.':
                    pass

                else:
                    print("There are invalid symble on the board")
                    exit()
        
    def kingCheck(self):
        
        for i in self.rook:

            if "K" in i.move():
                print("Success")
                exit()
            
        for i in self.bishop:

            if "K" in i.move():
                print("Success")
                exit()

        for i in self.queen:

            if "K" in i.move():
                print("Success")
                exit()
        
        # for i in self.pawn:

        #     if "K" in i.move():
        #         print("Success")
        #         exit()

        for i in self.knight:

            if "K" in i.move():
                print("Success")
                exit()
            

    def __Boardsta(self):

        self.Barr = []
        tmp_arr = []

        for i in self.board:
            
            if i == "\n":
                self.Barr.append(tmp_arr)
                tmp_arr = []
            else:
                tmp_arr.append(i)
        
        self.Barr.append(tmp_arr)
    
    def ValidateBoard(self):
        
        for i in range(len(self.Barr)):

            if len(self.Barr[i]) == len(self.Barr):
                continue
            else:
                return False
        return True

class chessPiece:
    
    def __init__(self,xCord,yCord,bSize,barr,color):

        self.xCord = xCord
        self.yCord = yCord
        self.boardSize = bSize
        self.boardArray = barr
        self.color = color
    
    #add ability to check other pawn on the board info
    def cordSeek(self,xCord,yCord):
        return self.boardArray[yCord][xCord]
    
    def PieceInfo(self):
        print("Current Piece Cordinate:",self.xCord,self.yCord)

    def move(self):
        pass

class Pawn(chessPiece):

    def move(self):
        moveSet = []
        if self.color == "Black":
            forward = 1
        else:
            forward = -1
        defaultMoveSet = [[-1,forward],[1,forward]]
        #Move for taking
        for i in range(3):
            tmpX = self.xCord + defaultMoveSet[i][0]
            tmpY = self.yCord + defaultMoveSet[i][1]
            
            #check if the next candidate is in side the board
            if tmpX < self.boardSize or tmpY < self.boardSize or tmpX >= 0 or tmpY >= 0:
                if self.cordSeek(tmpX,tmpY) == 'K': #Opponent's King
                    moveSet.append(self.cordSeek(tmpX,tmpY))
                elif self.cordSeek(tmpX,tmpY) != '.': #With Opponent's color
                    moveSet.append([tmpX,tmpY])
        #Normal move and first move
        startRow = self.boardSize/2 + forward*(2 - self.boardSize/2) - 1
        tmpX = self.xCord
        tmpY = self.yCord + forward
        if tmpX < self.boardSize or tmpY < self.boardSize or tmpX >= 0 or tmpY >= 0:
            if self.cordSeek(tmpX,tmpY) == '.':
                moveSet.append([tmpX,tmpY])
            tmpY = tmpY + forward
            #If in the start position and if noone in the way
            if self.yCord == startRow and self.cordSeek(tmpX,tmpY) == '.':
                moveSet.append([tmpX,tmpY])
        return moveSet

class Bishop(chessPiece):

    def move(self):

        moveSet = []
        rotate = [[1, 1], [1, -1], [-1, 1], [-1, -1]]

        for i in range(4):
            tmpX = self.xCord + rotate[i][0]
            tmpY = self.yCord + rotate[i][1]
            while True:

                #check if the next candidate is in side the board
                if tmpX >= self.boardSize or tmpY >= self.boardSize or tmpX < 0 or tmpY < 0:
                    break
                if self.cordSeek(tmpX,tmpY) == '.':
                    moveSet.append([tmpX,tmpY])
                elif self.cordSeek(tmpX,tmpY) == 'K': #Opponent's King
                    moveSet.append(self.cordSeek(tmpX,tmpY))
                else:
                    break

                tmpX = tmpX + rotate[i][0]
                tmpY = tmpY + rotate[i][1]

        return moveSet

class Rook(chessPiece):

    def move(self):
        
        moveSet = []
        rotate = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        for i in range(4):
            tmpX = self.xCord + rotate[i][0]
            tmpY = self.yCord + rotate[i][1]
            while True:

                #check if the next candidate is in side the board
                if tmpX >= self.boardSize or tmpY >= self.boardSize or tmpX < 0 or tmpY < 0:
                    break
                if self.cordSeek(tmpX,tmpY) == '.':
                    moveSet.append([tmpX,tmpY])
                elif self.cordSeek(tmpX,tmpY) == 'K': #Opponent's King
                    moveSet.append(self.cordSeek(tmpX,tmpY))
                else:
                    break

                tmpX = tmpX + rotate[i][0]
                tmpY = tmpY + rotate[i][1]

        return moveSet
    
class Knight(chessPiece):

    def move(self):
        moveSet = []
        defaultMoveSet = [[2,1],[-2,1],[2,-1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]
        for i in range(8):
            tmpX = self.xCord + defaultMoveSet[i][0]
            tmpY = self.yCord + defaultMoveSet[i][1]
            
            #check if the next candidate is in side the board
            if tmpX < self.boardSize or tmpY < self.boardSize or tmpX >= 0 or tmpY >= 0:
                if self.cordSeek(tmpX,tmpY) == '.':
                    moveSet.append([tmpX,tmpY])
                elif self.cordSeek(tmpX,tmpY) == 'K': #Opponent's King
                    moveSet.append(self.cordSeek(tmpX,tmpY))
                else:
                    break
        return moveSet
    
class Queen(chessPiece):

    def move(self):

        moveSet = []
        rotate = [[1, 1], [1, -1], [-1, 1], [-1, -1], [1, 0], [0, 1], [-1, 0], [0, -1]]

        for i in range(8):
            tmpX = self.xCord + rotate[i][0]
            tmpY = self.yCord + rotate[i][1]
            while True:

                #check if the next candidate is in side the board
                if tmpX >= self.boardSize or tmpY >= self.boardSize or tmpX < 0 or tmpY < 0:
                    break
                if self.cordSeek(tmpX,tmpY) == '.':
                    moveSet.append([tmpX,tmpY])
                elif self.cordSeek(tmpX,tmpY) == 'K': #Opponent's King
                    moveSet.append(self.cordSeek(tmpX,tmpY))
                else:
                    break

                tmpX = tmpX + rotate[i][0]
                tmpY = tmpY + rotate[i][1]

        return moveSet