#!/usr/bin/python3

import sys,re

arrLen = len(sys.argv)
if arrLen < 2:
    print("none")
else:
    for i in range(arrLen-1):
        x = re.findall("ism\Z",sys.argv[i+1])
        if x:
            pass
        else:
            if re.findall("e\Z",sys.argv[i+1]):
                print(str(sys.argv[i+1])[:-1]+"ism")
            else:
                print(str(sys.argv[i+1])+"ism")
