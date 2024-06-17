#!/usr/bin/python3

import sys,re

if len(sys.argv) != 2 :
    print("none")
else:
    inVal = str(input("What was the parameter? "))

    if inVal == sys.argv[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")