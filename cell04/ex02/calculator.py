#!/usr/bin/python3

inVal1 = int(input("Give me the first number: "))
inVal2 = int(input("Give me the second number: "))
print("Thank you!")

for i in range(4):

    if i == 0:
        print(inVal1,"+",inVal2,"=",inVal1+inVal2)
    elif i == 1:
        print(inVal1,"-",inVal2,"=",inVal1-inVal2)
    elif i == 2:
        print(inVal1,"/",inVal2,"=",inVal1/inVal2)
    elif i == 3:
        print(inVal1,"*",inVal2,"=",inVal1*inVal2)