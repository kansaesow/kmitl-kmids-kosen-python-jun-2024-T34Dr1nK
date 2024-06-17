#!/usr/bin/python3

import sys

arrLen = len(sys.argv)
if arrLen < 2:
    print("none")
else:

    print("parameters:",arrLen-1)
    for i in range(arrLen-1):
        print(sys.argv[i+1]+":",len(sys.argv[i+1]))