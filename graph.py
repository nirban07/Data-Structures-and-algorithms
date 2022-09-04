class Graph:
	def __init__(self) -> None:
		self.numberofnodes = 0
		self.adjacentList = {}
	def addVertex(self,node):
		self.adjacentList.update({node:[]})
		self.numberofnodes+=1
	def addEdge(self,node1,node2):
		self.adjacentList[node1].append(node2)
		self.adjacentList[node2].append(node1)

grph = Graph()
grph.addVertex(2)
grph.addVertex(4)
print(grph.adjacentList)