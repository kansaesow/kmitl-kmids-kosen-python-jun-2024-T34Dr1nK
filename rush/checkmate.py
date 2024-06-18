def test():
    print("Using Checkmate Module,,,,,")

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
                    for i in rook1.move():
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
    
    def cordSeek(self,xCord,yCord):
        return self.boardArray[yCord][xCord]

    def move(self):
        pass

class Pawn(chessPiece):

    def move(self):
        return super().move()
    
    def Eatmove(self):
        return super().move()

class Bishop(chessPiece):

    def move(self):



        return super().move()

class Rook(chessPiece):

    def move(self):

        moveSet = []

        for i in range(4):

            #check the moveable for rook at the right size
            if i == 0:
                tmpX = self.xCord+1
                while tmpX < self.boardSize:

                    if self.cordSeek(tmpX,self.yCord) == '.':

                        moveSet.append([tmpX,self.yCord])
                        tmpX += 1

                    elif self.cordSeek(tmpX,self.yCord) == 'K':

                        moveSet.append(self.cordSeek(tmpX,self.yCord))
                        tmpX = 9
                        
                    else:
                        tmpX = 9

            #We move to the bottom of rook
            elif i == 1:
                tmpY = self.yCord+1
                while tmpY < self.boardSize:

                    if self.cordSeek(self.xCord,tmpY) == '.':

                        moveSet.append([self.xCord,tmpY])
                        tmpX += 1

                    elif self.cordSeek(self.xCord,tmpY) == 'K':

                        moveSet.append(self.cordSeek(self.xCord,tmpY))
                        tmpY = 9
                        
                    else:
                        tmpY = 9

            #check the moveable for rook at the left size
            elif i == 2:
                tmpX = self.xCord-1
                while tmpX > 0:

                    if self.cordSeek(tmpX,self.yCord) == '.':

                        moveSet.append([tmpX,self.yCord])
                        tmpX -= 1

                    elif self.cordSeek(tmpX,self.yCord) == 'K':

                        moveSet.append(self.cordSeek(tmpX,self.yCord))
                        tmpX = -1
                        
                    else:
                        tmpX = 1

            #We move to the upper of rook
            elif i == 3:
                tmpY = self.yCord-1
                while tmpY > 0:

                    if self.cordSeek(self.xCord,tmpY) == '.':

                        moveSet.append([self.xCord,tmpY])
                        tmpX -= 1

                    elif self.cordSeek(self.xCord,tmpY) == 'K':

                        moveSet.append(self.cordSeek(self.xCord,tmpY))
                        tmpY = -1
                        
                    else:
                        tmpY = -1


        return moveSet
    
class Horse(chessPiece):

    def move(self):
        return super().move()
    
class Queen(chessPiece):

    def move(self):
        return super().move()