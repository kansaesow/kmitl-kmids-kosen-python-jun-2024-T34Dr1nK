#!/usr/bin/python3

import sys,re

if len(sys.argv) != 3 :
    print("none")
else:
    Scan =len(re.findall(sys.argv[1],sys.argv[2]))

    if Scan:
        print(Scan)
    else:
        print("none")