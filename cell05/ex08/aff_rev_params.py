#!/usr/bin/python3

import sys

arrLen = len(sys.argv)
if arrLen < 4:
    print("none")
else:
    while arrLen != 1:
        print(sys.argv[arrLen-1])
        arrLen-=1