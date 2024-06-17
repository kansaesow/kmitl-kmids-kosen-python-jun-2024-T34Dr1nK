#!/usr/bin/python3

import sys

arrLen = len(sys.argv)
if arrLen != 2:
    print("none")
else:
    for i in sys.argv[1]:
        if i == "z":
            print(i,end="")