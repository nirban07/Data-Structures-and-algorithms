
from traceback import print_tb


class Node:
	def __init__(self,key) -> None:
		self.val = key
		self.left = None
		self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(6)
leftrun = root
# while(leftrun):
# 	print(leftrun.val)
# 	leftrun = leftrun.left
# rightrun = root
# while(rightrun):
# 	print(rightrun.val)
# 	rightrun = rightrun.right

def traversalInOrder(root):
	if root == None:
		return "None"
	print(root.val)
	traversalInOrder(root.left)
	traversalInOrder(root.right)

# traversalInOrder(root)

def BFS(root):
	arr = []
	queue = []
	currentnode = root
	queue.append(root)

	while(len(queue)>0):
		currentnode = queue.pop(0)
		arr.append(currentnode.val)
		if(currentnode.left):
			queue.append(currentnode.left)
		if(currentnode.right):
			queue.append(currentnode.right)
	return arr
	
# print(BFS(root))


def recursiveBFS(queue,arr):
	if(len(queue)==0):
		return arr
	
	currentnode = queue.pop(0)
	arr.append(currentnode.val)

	if(currentnode.left):
		queue.append(currentnode.left)
	if(currentnode.right):
		queue.append(currentnode.right)
	
	return recursiveBFS(queue,arr)

# print(recursiveBFS([root],[]))

# trweaverse in order
def traverseInOrder(root,arr):
	if(root.left):
		traverseInOrder(root.left,arr)
	arr.append(root.val)
	if(root.right):
		traverseInOrder(root.right,arr)
	return arr
print(traverseInOrder(root,[]))

def traversepreOrder(root,arr):
	arr.append(root.val)
	if(root.left):
		traversepreOrder(root.left,arr)
	if(root.right):
		traversepreOrder(root.right,arr)
	return arr
print(traversepreOrder(root,[]))
def traversePostOrder(root,arr):
	if(root.left):
		traversePostOrder(root.left,arr)
	if(root.right):
		traversePostOrder(root.right,arr)
	arr.append(root.val)
	return arr
print(traversePostOrder(root,[]))

#            1
#       2         3
#     4   6
print(None<1)