#!/usr/bin/python3

print("Enter a number less than 25")

inVal = int(input())

if inVal < 26:
    for i in range(inVal,26):
        print("Inside the loop, my variable is",i)
else:
    print("Error")