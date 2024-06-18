#!/usr/bin/python3

import sys
import checkmate

def main():

    board = """\
...K
....
R...
P...\
"""

    if len(sys.argv) > 1:

        for i in len(sys.argv):

            input_file = open(sys.argv[i],'r')
            content = input_file.read()
            board = content

    chessGame = checkmate.chessGame(board)
    #chessGame.printboard()
    chessGame.ReadPiece()
    chessGame.kingCheck()

if  __name__ == "__main__":
    main()