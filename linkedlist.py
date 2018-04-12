class Node:
	size=0
	def __init__(self,value):
		self.value= value
		self.nextNode = None
		Node.size+=1
class LinkedList:
	head=None
	# Add node to start of LinkedList
	def addNode(self,nodeObj):
		if self.head==None:
			self.head = nodeObj
		else:
			nodeObj.nextNode= self.head
			self.head=nodeObj

	def listAllNodes(self):
		start=self.head
		while self.head!=None:
			print(self.head.value , "-> ", end='')
			self.head=self.head.nextNode
		print("NULL")
		self.head=start

	def sifeOfList(self):
		print("Number of Nodes:",self.head.size)

	# Add node to End of LinkedList
	def addNodeToEnd(self,nodeObj):
		start=self.head
		while self.head.nextNode!=None:
			self.head=self.head.nextNode
		self.head.nextNode=nodeObj
		self.head=start

	#Removing a node from the LinkedList
	def removeNode(self,nodeObj):
		start=self.head
		if self.head==nodeObj: #If the node to be deleted is at the start of the LinkedList
			nextHead=self.head.nextNode
			del self.head
			self.head=nextHead
		else:
			while self.head.nextNode!=nodeObj:
				self.head=self.head.nextNode
			current=self.head
			deleteNode=current.nextNode
			current.nextNode=current.nextNode.nextNode
			del deleteNode
			self.head=start
		self.listAllNodes()


node1=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)
node5=Node(50)
node6=Node(60)
node7=Node(70)
node8=Node(80)

linkedlist = LinkedList()
linkedlist.addNode(node1)
linkedlist.addNode(node2)
linkedlist.addNode(node3)
linkedlist.addNode(node4)
linkedlist.addNode(node5)
linkedlist.addNode(node6)
linkedlist.addNode(node7)
linkedlist.addNode(node8)
linkedlist.listAllNodes()

linkedlist.sifeOfList()


node9=Node(90)
linkedlist.addNodeToEnd(node9)
node10=Node(100)
linkedlist.addNodeToEnd(node10)
linkedlist.sifeOfList()

linkedlist.listAllNodes()

linkedlist.removeNode(node1)
linkedlist.removeNode(node10)
linkedlist.removeNode(node8)
