import algo1
import array
import linkedlist as link


class PriorityQueue:
  head=None
class PriorityNode:
  value=None
  nextNode=None
  priority=None



def enqueue_priority(Q,element,priority):
	current = Q.head
	newNode = PriorityNode()
	newNode.value = element
	newNode.priority = priority
	position = 0

	if current == None:
		Q.head = newNode
		return position
	else:
		if current.priority <= priority:
			newNode.nextNode = current
			Q.head = newNode
			return position
		
		while current.nextNode != None:
			position += 1
			if current.nextNode.priority >= priority:
				current = current.nextNode
			else:
				newNode.nextNode = current.nextNode
				current.nextNode = newNode
				return position
		
		current.nextNode = newNode
		position += 1
		return position



def dequeue_priority(Q):
	current = Q.head
	if current == None: return
	maxPriority = current.priority
	prevPriorityNode = current

	while current.nextNode != None:
		if maxPriority < current.nextNode.priority:
			maxPriority = current.nextNode.priority
			prevPriorityNode = current
		current = current.nextNode
	
	if maxPriority == Q.head.priority: 
		maxPriorityValue = Q.head.value
		Q.head = Q.head.nextNode
	else:
		maxPriorityValue = prevPriorityNode.nextNode.value
		prevPriorityNode.nextNode = prevPriorityNode.nextNode.nextNode
	return maxPriorityValue
    