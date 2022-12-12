import array
import myqueue
import mystack
import mypriorityqueue
import linkedlist
from algo1 import *
from mylib import *

###########################################

class BinaryTree:
  root=None

class BinaryTreeNode:
  key=None
  value=None
  leftnode=None
  rightnode=None
  parent=None

###########################################
### Ej. 1 ###
###########################################

def search(B, element):
	node = searchNodeR(B.root, element)
	if node == None: return
	else: return node.key

def searchNodeR(node, element):
	if node == None: return

	if node.value == element:
		return node
	
	right = searchNodeR(node.rightnode, element)
	if right != None: 
		return right
	
	left = searchNodeR(node.leftnode, element)
	if left != None: 
		return left

def searchNode(B, element):
	return searchNodeR(B.root, element)

####################################################

def insert(B, element, key):
	newNode = BinaryTreeNode()
	newNode.key = key
	newNode.value = element

	if(B.root == None):
		B.root = newNode
		return key
	return insertR(newNode, B.root)

def insertR(newNode, currentNode):
	if newNode.key > currentNode.key:
		if currentNode.rightnode == None:
			newNode.parent = currentNode
			currentNode.rightnode = newNode
			return newNode.key
		else:
			right = insertR(newNode, currentNode.rightnode)
			if right != None: 
				return right
	else:
		if currentNode.leftnode == None:
			newNode.parent = currentNode
			currentNode.leftnode = newNode
			return newNode.key
		else:
			left = insertR(newNode, currentNode.leftnode)
			if left != None: 
				return left

################################################

def delete(B, element):
	node = searchNode(B, element)
	if node == None: return
	else: return deleteCurrentCase(B, node)

def deleteCurrentCase(B, node):
	if node.rightnode == None:
		if node.leftnode == None:
			if node.parent.leftnode != None and node.parent.leftnode == node:
				node.parent.leftnode = None
				return node.key
			elif node.parent.rightnode != None and node.parent.rightnode == node:
				node.parent.rightnode = None
				return node.key
		if node.parent.leftnode != None and node.parent.leftnode == node:
			node.parent.leftnode = node.leftnode
			return node.key
		elif node.parent.rightnode != None and node.parent.rightnode == node:
			node.parent.rightnode = node.leftnode
			return node.key

	else:
		if node.leftnode == None:
			if node.parent.leftnode == node:
				node.parent.leftnode = node.rightnode
				return node.key
			elif node.parent.rightnode == node:
				node.parent.rightnode = node.rightnode
				return node.key
		else:
			change = bigger(node.leftnode)

			node.value = change.value
			oldKey = node.key
			node.key = change.key

			if change.parent.leftnode == change:
					change.parent.leftnode = None
			elif change.parent.rightnode == change:
					change.parent.rightnode = None
			
			return oldKey

#Como usaremos solo una opción, definimos solo la funcion para encontrar el nodo mas grande

def bigger(node):
	if node.rightnode != None:
		current = bigger(node.rightnode)
		if current != None:
			return current
	else: return node

######################################

def deleteKey(B, key):
	node = searchKeyR(B.root, key)
	if node == None: return
	else: return deleteCurrentCase(B, node)

# Función recursiva de searchKey
def searchKeyR(node, key):
	if node == None: return

	if node.key == key:
		return node
	
	right = searchKeyR(node.rightnode, key)
	if right != None: 
		return right
	
	left = searchKeyR(node.leftnode, key)
	if left != None: 
		return left
    
############################################

def access(B, key):
	node = searchKeyR(B.root, key)
	if node == None: return
	else: return node.value

############################################

def update(B, element, key):
	node = searchKeyR(B.root, key)
	if node == None: return
	else:
		node.value = element
		return node.key

###########################################
### Ej. 2 ###
###########################################

def traverseInOrder(B):
	L=linkedlist.LinkedList()
	traverseInOrderR(B.root, L)
	return linkedlist.revert(L)

def traverseInOrderR(node, L):
	if node != None:
		traverseInOrderR(node.leftnode, L)
		linkedlist.add(L, node.value)
		traverseInOrderR(node.rightnode, L)

###########################################

def traverseInPostOrder(B):
	L = linkedlist.LinkedList()
	traverseInPostOrderR(B.root, L)
	return linkedlist.revert(L)

def traverseInPostOrderR(node, L):
	if node != None:
		traverseInPostOrderR(node.leftnode, L)
		traverseInPostOrderR(node.rightnode, L)
		linkedlist.add(L, node.value)

##########################################

def traverseInPreOrder(B):
  L = linkedlist.LinkedList()
  traverseInPreOrderR(B.root, L)
  return linkedlist.revert(L)

def traverseInPreOrderR(node, L):
	if node != None:
		linkedlist.add(L, node.value)
		traverseInPreOrderR(node.leftnode, L)
		traverseInPreOrderR(node.rightnode, L)

#############################################

def traverseBreadFirst(B):
  queue = linkedlist.LinkedList()
  valuesQueue = linkedlist.LinkedList()
  myqueue.enqueue(queue, B.root)
  while queue.head != None:
    node = myqueue.dequeue(queue)
    myqueue.enqueue(valuesQueue, node.value)

    if node.leftnode != None:
      myqueue.enqueue(queue, node.leftnode)
    if node.rightnode != None:
      myqueue.enqueue(queue, node.rightnode)
  return linkedlist.revert(valuesQueue)

#################################################

def mod(n):
  if n > 0:
    return n
  elif n == 0:
    return 0
  else:
    return n*-1

def isBalanced(B):
  leftTree = BinaryTree()
  rightTree = BinaryTree()
  
  leftTree.root = B.root.leftnode
  rightTree.root = B.root.rightnode
  
  leftTreeHeight = height(leftTree)
  rightTreeHeight = height(rightTree)
  
  if mod(leftTreeHeight - rightTreeHeight) == 0 or mod(leftTreeHeight - rightTreeHeight) == 1: return True
  else: return False


def heightR(head):
  heigth = 0
  if head.leftnode == None and head.rightnode==None:
    return 0
  else:
    firstOption = -1
    secondOption = -1
    if head.leftnode != None:
      firstOption = heightR(head.leftnode)
    if head.rightnode != None:
      secondOption = heightR(head.rightnode)
    return 1+max(firstOption,secondOption)
      
  
def height(B):
  return (heightR(B.root))


def isSubtree(B,S):
  h1 = height(B)
  h2 = height(S)
  if h1 > h2:
    newRoot = searchKeyR(S.root,S.root.key)
    B.root = newRoot
    list1 = traverseInOrder(B)
    list2 = traverseInOrder(S)
    if linkedlist.areEqual(list1,list2):
      return True
    else:
      return False
  else:
    return "Error, el primer arbol debe ser mas grande que el segundo."

def checkBST(B):
	if(B.root == None):
		return False
	return isBST(B.root)

def isBST(node):   
	if(node.leftnode != None):
		if(node.key <= node.leftnode.key):
			return False
		isBST(node.leftnode)
	if(node.rightnode != None):
		if(node.key >= node.rightnode.key):
			return False
		isBST(node.rightnode)
	return True