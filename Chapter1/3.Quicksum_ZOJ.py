# Task: the sum of the products of each character's position in the packet times the character's value
# Letters have a value equal to their position in the alphabet
# Only uppercase letters and spaces, e.g ' ' = 0, 'A' = 1, 'Z' = 26

# Input: one or more packets followed by a line containing only # that signals the end of the input 
# Each packet is on a line by itself, does not begin or end with a space, and contains from 1 to 255 characters

# Output: for each packet, output its quicksum on a separate line in the output

from sys import stdin

def value(char):
    if char == ' ':
        return 0
    else:
        return (ord(char)-ord('A')+1)

quicksum = 0
position = 1
uLimit = 255
line = stdin.read(255)

while(line != '#\n'):
    for i in line:
        if i == '\n':
            break
        else:
            quicksum += position * value(i)
            position += 1
    print(quicksum)
    quicksum = 0
    position = 1
    line = stdin.read()
