class Node:						#Node class with 3 attributes:  value,leftChild and rightChild
	def __init__(self,value):
		self.value=value
		self.leftChild=None
		self.rightChild=None

class BinarySearchTree:			#Binary Tree Class holds Node objects
	root=None
	def insert(self,newNode):	#Function to insert a Node into BinartSearchTree
		if self.root==None:		#If empty Tree
			self.root=newNode
		else:		
			current=self.root
			while current!=None:				
				if newNode.value<current.value: #Traverse left tree
					if current.leftChild==None:
						current.leftChild=newNode
						break
					else:
						current=self.traverse("left",current)
				else:							#Traverse right tree
					if current.rightChild==None:
						current.rightChild=newNode
						break
					else:
						current=self.traverse("right",current)

	def traverse(self,direction,nodeToTraverse):
		if direction=="left":
			return nodeToTraverse.leftChild
		elif direction=="right":
			return nodeToTraverse.rightChild

	def getMinNode(self,current):	#Get smallest value in tree
		while(current.leftChild is not None):
			current=current.leftChild
		return current

	def callDelete(self,nodeToBeDeleted): #Calls Delete fucntion
		print("Deleting:",nodeToBeDeleted.value)
		self.delete(nodeToBeDeleted,self.root)
		print("After deletion:")
		self.call_inorder_traversal()

	def delete(self,nodeToBeDeleted,current):
		if nodeToBeDeleted.value>current.value: #Traverse left tree
			current.rightChild= self.delete(nodeToBeDeleted, current.rightChild)
		elif nodeToBeDeleted.value<current.value: #Traverse right tree
			current.leftChild= self.delete(nodeToBeDeleted, current.leftChild)
		else:
			if current.leftChild==None: #Only one child
				temp = current.rightChild
				current.value = None
				return temp
			elif current.rightChild==None:
				temp = current.leftChild
				current.value = None
				return temp
			else:						#The node to be deleted here will have two children
				temp = self.getMinNode(current.rightChild)
				current.value=temp.value
				current.rightChild = self.delete(nodeToBeDeleted, current.rightChild)
		return current


	def call_search(self,nodeToSearch):
		print("Searching for",nodeToSearch)
		answer=self.search(self.root,nodeToSearch)
		if answer :
			print(nodeToSearch,":FOUND")
		else : 
			print(nodeToSearch,":NOT FOUND IN TREE")

	def search(self,root, nodeToSearch):
		if root.value==nodeToSearch:
			return True
		elif nodeToSearch<root.value and root.leftChild!=None:
			self.search(root.leftChild,nodeToSearch)
		elif nodeToSearch>root.value and root.rightChild!=None:
			self.search(root.rightChild,nodeToSearch)


	def call_inorder_traversal(self):
		print("Inorder Traversal:")
		self.inorder_traversal(self.root)
		print("\n")


	def inorder_traversal(self,nodeToTraverse):
		if(nodeToTraverse!=None):
			self.inorder_traversal(nodeToTraverse.leftChild)
			print(nodeToTraverse.value, end=" ")
			self.inorder_traversal(nodeToTraverse.rightChild)


# Create 8 Node objects
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)

# Create a BinarySearchTree object and insert all 8 Nodes
myBinaryTree = BinarySearchTree()
myBinaryTree.insert(node4)
myBinaryTree.insert(node2)
myBinaryTree.insert(node6)
myBinaryTree.insert(node1)
myBinaryTree.insert(node3)
myBinaryTree.insert(node5)
myBinaryTree.insert(node7)
myBinaryTree.insert(node8)

myBinaryTree.call_inorder_traversal()
# Delete node8
myBinaryTree.callDelete(node8)

# Search for a node that is present
myBinaryTree.call_search(4)
# Search for a node that is absent
myBinaryTree.call_search(8)