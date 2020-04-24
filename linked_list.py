"""Implementing a Linked List in Python"""

class Node(object):

	def __init__(self, data=None):
		'''Constructor'''
		self.data = data
		self.next = None 

	def getData(self):
		'''Returns data'''
		return self.data

	def setData(self, newdata):
		'''Modify data'''
		self.data = newdata

	def getNext(self):
		'''Get Next node'''
		return self.next

	def setNext(self, nextnode):
		'''Add new node s the next in line'''
		self.next = nextnode

## Creating a linked list manually ##################################################################
print("-\n- Creating a linked list manually:")
node1 = Node("a")
print("\nCreation of Node1")
print("\tNode1 Data: ", node1.getData())
print("\tNode1 Next: ", node1.getNext())

print("\nAddition of Node2")
node2 = Node("b")
node1.setNext(node2)
print("\tNode1 Data: ", node1.getData())
print("\tNode1 Next: ", node1.getNext())
print("\tNode2 Data: ", node2.getData())
print("\tNode2 Next: ", node2.getNext())

print("\nAddition of Node3")
node3 = Node("c")
node2.setNext(node3) 
print("\tNode1 Data: ", node1.getData())
print("\tNode1 Next: ", node1.getNext())
print("\tNode2 Data: ", node2.getData())
print("\tNode2 Next: ", node2.getNext())
print("\tNode3 Data: ", node3.getData())
print("\tNode3 Next: ", node3.getNext())

print("\nGoing form Node2 to shows data from Node3 (node2.getNext().getData())")
print("\tNode3 Data: ", node2.getNext().getData())

## Creating a linked list from a dataset ##################################################################
my_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]

#Crate first Node
head = Node(my_list[0])

#Pointing to the first node
currentNode = head

#Skip the first element of my_list so we can iterate through the rest
iter_my_list = iter(my_list)
next(iter_my_list)

#Create the linked list
for element in iter_my_list:
	#We add a new node
	currentNode.setNext(Node(element))
	#We advance to point to the just created new node
	currentNode = currentNode.getNext()


## Iterate through the linked list #######################################################################
print("\n-- Iterating through a linked list:")
#Point to the begining of the linked list
currentNode = head

print("\nLinked list elements:")
i=0
#Loops while the node does not point to None
while currentNode.getNext() != None:
	#print the data of the current node
	print(f"Data node{i}: ", currentNode.getData())
	#we point to the next node
	currentNode = currentNode.getNext()
	i+=1
print(f"Data node{i}: ", currentNode.getData())

## Check if an element id present in the linked list #####################################################
print("\n-- Checking if an element is in the linked list:")
# element to be found
my_element = "a"
my_element2 = "Z"

#Point to the begining of the linked list
currentNode = head

while currentNode.getNext() != None:
	if currentNode.getData() == my_element:
		print("\nElement found")
		break
	else:
		currentNode = currentNode.getNext()


## Add an element at a given position of the list #####################################################
print("\n-- Insert a new element into the linked list at position 5:")
#element to be placed
new_element = 'ZZZZ'
position = 5
#Point to the begining of the linked list
currentNode = head

#Get to the position before the node we want
counter = 1
while counter < position-1:
	counter+=1
	currentNode = currentNode.getNext()
	


#Temporal Node
tempNode = currentNode.getNext()
#Insert new element
currentNode.setNext(Node(new_element))
#Connect the new element to the rest of the linked list
currentNode.getNext().setNext(tempNode)


#Check the list
currentNode = head
print("\nLinked list elements with new element:")
i = 1
while currentNode.getNext() != None:
	print(f"Data node{i}: ", currentNode.getData())
	currentNode = currentNode.getNext()
	i+=1
print(f"Data node{i}: ", currentNode.getData())

## Delete an element at a given position of the list #####################################################
#*** This cannot get access to the head ***
print("\n-- Delete an element from the linked list at position 5:")
position = 5
#Point to the begining of the list
currentNode=head
#Go to the given position-1
counter=1
while counter < position-1:
	counter+=1
	currentNode = currentNode.getNext()
	
#Skip the unwanted node by pointing to the following one
currentNode.setNext(currentNode.getNext().getNext())

#Check the list
currentNode = head
print("\nLinked list elements an element removed:")
i = 1
while currentNode.getNext() != None:
	print(f"Data node{i}: ", currentNode.getData())
	currentNode = currentNode.getNext()
	i+=1
print(f"Data node{i}: ", currentNode.getData())

## Insert an element at the begining of the list #####################################################
print("\n-- Insert an element at the begining of the list:")
#point to the begining of the list
currentNode = head

#element to be placed
new_element = 'AAAA'
newNode = Node(new_element)

#New Node points to head
newNode.setNext(currentNode)

#set New Node as the new head
head = newNode

#Check the list
currentNode = head
print("\nLinked list elements an element removed:")
i = 1
while currentNode.getNext() != None:
	print(f"Data node{i}: ", currentNode.getData())
	currentNode = currentNode.getNext()
	i+=1
print(f"Data node{i}: ", currentNode.getData())

## Delete the first element (head) of the list #####################################################
print("\n-- Delete the first element (head) of the list:")
#point to the begining of the list
currentNode = head

#set the head of the list as the next element
head = head.getNext()

#Check the list
currentNode = head
print("\nLinked list elements an element removed:")
i = 1
while currentNode.getNext() != None:
	print(f"Data node{i}: ", currentNode.getData())
	currentNode = currentNode.getNext()
	i+=1
print(f"Data node{i}: ", currentNode.getData())

