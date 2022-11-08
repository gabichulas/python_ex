from algo1 import *
from mylib import *

class LinkedList:
  head = None

class Node:
  value = None
  nextNode = None

def add(l,element):
  node = Node()
  current = l.head
  node.value = element
  l.head = node
  node.nextNode = current

def search(l,element):
  current = l.head
  pos = 0
  while current != None:
    if current.value == element:
      return pos
    pos += 1
    current = current.nextNode
  return None

def length(L):
  current = L.head
  len = 0
  while current != None:
    len += 1
    current = current.nextNode
  return len

def insert(l,element,position):
    current = l.head
    if position > length(l) or position < 0:
        return None
    elif position == 0:
        add(l, element)
        l.head.nextNode = current
        return 0

    else:
        for i in range(1, position + 1):
            if (i == position):
                node = Node()
                node.value = element
                node.nextNode = current.nextNode
                current.nextNode = node
                position = i
            current = current.nextNode
        return position

def delete(l,element):
  current = l.head
  pos = search(l,element)
  if pos != None:
    if current.value == element:
      l.head = current.nextNode
      return pos
    while current != None:
      if current.nextNode.value == element:
        current.nextNode = current.nextNode.nextNode
        return pos
      current = current.nextNode    
  else:
    return None

def access(l,position):
  current = l.head
  if position >= 0 and position < length(l):
    for i in range(0,position+1):
      valor = current.value
      current = current.nextNode
    return valor
  elif position == 0:
      return current.value   
  else:
    return None
  
def update(l,element,position):
  current = l.head
  if position >= 0 and position < length(l):  
    for i in range(0,position):
      current = current.nextNode
    current.value = element
    return position
  else:
    return None

def revert(L):
	newL = LinkedList()
	len = length(L)
	current = L.head

	for i in range(len):
		len -= 1
		add(newL, current.value)
		current = current.nextNode
	return newL