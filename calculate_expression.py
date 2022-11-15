import linkedlist as link
from algo1 import *
from mylib import *

def isPermutation(S,T):
    currentS = S.head
    currentT = T.head
    aux = None
    cont = 0
    areEqual = link.areEqual(S,T)
    if areEqual == False:    
        while currentS != None:
            aux = link.search(S,currentT.element)
            if aux != None:
                cont += 1
            currentS = currentS.nextNode
            currentT = currentT.nextNode
        if aux == link.length(S): return True 
        else: return False
    else:
        return False
