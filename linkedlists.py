class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	# traversal
	def printllist(self):
		temp = self.head
		while(temp):
			print(temp.data)
			temp = temp.next
	
	def pushAtFront(self,data):
		temp = self.head
		self.head = Node(data)
		self.head.next = temp
	
	def pushAtEnd(self,data):
		temp = self.head
		while(temp.next):
			temp =temp.next
		temp.next = Node(data)
	
	def insertAfter(self,pre,data):
		temp = self.head
		while(temp.data != pre):
			temp = temp.next
		afternode = temp.next
		beforenode = temp
		newnode = Node(data)

		beforenode.next = newnode
		newnode.next = afternode
		# print(temp.next = 9)

	def deleteFromStart(self,data):
		temp = self.head
		if(temp.data == data):
			self.head = temp.next
			return 
		prenode = 0
		while(temp.data != data):
			prenode = temp
			temp = temp.next
		# print("this is pre node" ,prenode.data)
		prenode.next = temp.next
		print(prenode.next)
		temp = None
		



llist = LinkedList()
llist.head = Node(1)
# llist.head.next = Node(9)
second = Node(9)
# llist.head.next.next = Node(91)
third = Node(91)
# connecting
llist.head.next = second
second.next = third

# pust at front
llist.pushAtFront(25)

# pushat end
llist.pushAtEnd(30)

llist.insertAfter(1,45)
llist.insertAfter(25,99)

llist.deleteFromStart(30)
# llist.deleteFromStart(30)

# traversal
llist.printllist()


# temp = llist.head
# while temp.data:
# 	print(temp.data)
# 	if(temp.next== None):
# 		break
# 	temp = temp.next