#!/usr/bin/python3

print("Enter the first number:")
inVal1 = int(input())
print("Enter the second number:")
inVal2 = int(input()) 

TxT = inVal1 * inVal2

if TxT > 0:
    print("This number is positive.")
elif TxT == 0:
    print("This number is both positive and negative.")
else:
    print("This number is negative.")