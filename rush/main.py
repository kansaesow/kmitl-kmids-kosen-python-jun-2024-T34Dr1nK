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

        input_file = open(sys.argv[1],'r')
        content = input_file.read()
        board = content

    chessGame = checkmate.chessGame(board)
    #chessGame.printboard()
    chessGame.ReadPiece()
    chessGame.kingCheck()

if  __name__ == "__main__":
    main()