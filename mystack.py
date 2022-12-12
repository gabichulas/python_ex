import linkedlist as link
import algo1
import array

class LinkedList:
  head = None

class Node:
  value = None
  nextNode = None


def push(S,element):
  link.add(S,element)
  return None

def pop(S):
  if S.head.value != None:
    current = S.head
    S.head = current.nextNode
    return current.value
  else:
    return None
  
