#Each Element is of class Element
class Element:                   
	def __init__(self,value):
		self.value=value
		self.elementBelow=None


#Each Element object is added to Stack Object which maintains
class Stack:
	#top and size of the Stack                     
	size=5                       
	numOfElements=0
	top=None

	#Add an element operation
	def push(self,stackElement): 
		if Stack.numOfElements == Stack.size:
			print("Cannot add anymore elements ", "Stack FULL")
			return
		Stack.numOfElements+=1
		if self.top==None:
			self.top=stackElement
			self.top.value=stackElement.value
		else:
			stackElement.elementBelow=self.top
			self.top=stackElement

	#Remove an element operation
	def pop(self):               
		if(Stack.isEmpty(self)):
			print("Cannot perform pop operation ", "Stack EMPTY")
			return
		Stack.numOfElements-=1
		toBePopped = self.top
		self.top = self.top.elementBelow
		print(toBePopped.value,"has been deleted")
		print("Remaining Number of Elements :", Stack.numOfElements)
		del toBePopped


	#Check the top element operation
	def peak(self):              
		if(Stack.isEmpty()):
			print("Stack EMPTY")
			return
		print(self.top.value," is on top of the stack")

	def isFull(self):
		if(Stack.numOfElements==Stack.size):
			return True
		else:
			return False

	def isEmpty(self):
		if(Stack.numOfElements==0):
			return True
		else:
			return False

	def printStack(self):
		rightOnTop = self.top
		while self.top!=None:
			print(self.top.value,"-> ",end="")
			self.top=self.top.elementBelow
		print("END OF STACK")
		self.top = rightOnTop


# Declare Stack variable 
myStack = Stack()

# Create 5 element variables
element1 = Element(1)
element2 = Element(2)
element3 = Element(3)
element4 = Element(4)
element5 = Element(5)

# Push 5 elements onto stack
myStack.push(element1)
myStack.push(element2)
myStack.push(element3)
myStack.push(element4)
myStack.push(element5)

# Extra element to show that stack cannot accept more elements past Stack Size(here, 5)
elementExtra = Element(6)
myStack.push(elementExtra)

myStack.printStack()

myStack.pop()
myStack.pop()
myStack.pop()

myStack.printStack()

myStack.push(element1)
myStack.push(element2)
myStack.push(element3)
print("Stack is FULL:",myStack.isFull())
print("Stack is EMPTY:",myStack.isEmpty())