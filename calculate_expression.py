import linkedlist as link
from algo1 import *
from mylib import *

def calculate_expression(L,position):
    operator = ""
    firstPart = ""
    secondPart = ""
    j = 0
    value = link.access(L,position)

    if value != None:
        for h in range(len(value)):
            if value[h] == "+":
                operator = value[h]
            elif value[h] == "-":
                operator = value[h]
            elif value[h] == "/":
                operator = value[h]
            elif value[h] == "*":
                operator = value[h]

        while (value[j] != operator):
            firstPart = firstPart + value[j]
            j += 1

        for i in range(j+1,len(value)):
            secondPart = secondPart + value[i]
        
        firstPart = int(firstPart)
        secondPart = int(secondPart)

        if operator == "+":
            return firstPart+secondPart
        elif operator == "-":
            return firstPart-secondPart
        elif operator == "*":
            return firstPart*secondPart
        elif operator == "/":
            return trunc(firstPart/secondPart)
    else:
        return None

