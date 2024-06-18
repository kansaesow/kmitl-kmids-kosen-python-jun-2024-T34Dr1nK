#!/usr/bin/python3

import checkmate

def main():

    checkmate.test()

    board = """\
RK..
....
..P.
....\
"""

    chessGame = checkmate.chessGame(board)
    chessGame.printboard()
    chessGame.Kcheck()

if  __name__ == "__main__":
    main()