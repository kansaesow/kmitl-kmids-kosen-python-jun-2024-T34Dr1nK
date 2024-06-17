#!/usr/bin/python3

import sys

arrLen = len(sys.argv)
if arrLen != 3:
    print("none")
else:
    Narr = []

    for i in range(int(sys.argv[1]),int(sys.argv[2])+1):
        Narr.append(i)
    print(Narr)