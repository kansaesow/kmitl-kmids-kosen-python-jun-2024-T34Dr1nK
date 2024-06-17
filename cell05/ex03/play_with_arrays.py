#!/usr/bin/python3

arr = [2, 8, 9, 48, 8, 22, -12, 2]
Narr = []

for i in arr:
    if i > 5:
        Narr.append(i+2)

print("Original array: ", arr)
print("New array: ", set(Narr))