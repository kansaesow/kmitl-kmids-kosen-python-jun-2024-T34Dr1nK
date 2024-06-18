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

        if self.__ValidateBoard():
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

    def Kcheck(self):
        
        for yCord,yList in enumerate(self.Barr):

            for xCord,bVal in enumerate(yList):

                if bVal == 'K':
                    print("King at x,y: ",xCord,yCord)

                elif bVal == 'R':

                    print("Rook at x,y: ",xCord,yCord)
                    rook1 = Rook(xCord,yCord,self.boardSize,self.Barr)
                    print("This is Rook movable set :")
                    # for i in rook1.move():
                    #     print(i)

                    print(rook1.move())
                        
                elif bVal == 'B':

                    print("Bishop at x,y: ",xCord,yCord)
                    bishop1 = Bishop(xCord,yCord,self.boardSize,self.Barr)
                    print("This is Bishop movable set :")
                    for i in bishop1.move():
                        print(i)
                
                elif bVal == 'Q':

                    print("Queen at x,y: ",xCord,yCord)
                    queen1 = Queen(xCord,yCord,self.boardSize,self.Barr)
                    print("This is Queen movable set :")
                    for i in queen1.move():
                        print(i)
                
                elif bVal == 'P':

                    print(" at x,y: ",xCord,yCord)
                    pawn1 = Pawn(xCord,yCord,self.boardSize,self.Barr)
                    print("This is Pawn movable set :")
                    for i in pawn1.move():
                        print(i)

                elif bVal == 'K':

                    print(" at x,y: ",xCord,yCord)
                    knight1 = Knight(xCord,yCord,self.boardSize,self.Barr)
                    print("This is Knight movable set :")
                    for i in knight1.move():
                        print(i)

                elif bVal != '.':
                    print(bVal,"x,y:",xCord,yCord)

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
    
    def __ValidateBoard(self):
        
        for i in range(len(self.Barr)):

            if len(self.Barr[i]) == len(self.Barr):
                continue
            else:
                return False
        return True

class chessPiece:
    
    def __init__(self,xCord,yCord,bSize,barr):

        self.xCord = xCord
        self.yCord = yCord
        self.boardSize = bSize
        self.boardArray = barr
    
    #add ability to check other pawn on the board info
    def cordSeek(self,xCord,yCord):
        return self.boardArray[yCord][xCord]

    def move(self):
        pass

class Pawn(chessPiece):

    def move(self):

        moveSet = []

        return super().move()

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
        return super().move()
    
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