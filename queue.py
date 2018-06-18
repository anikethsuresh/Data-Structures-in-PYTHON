#Each Element is of class Element
class Element:
	def __init__(self,value):
		self.value=value
		self.connectedTo = None

#Queue holds the elements in its own class
class Queue:
	size=0
	def __init__(self):
		self.first=None
		self.last=None

#Add an element
	def Enqueue(self,queueElement):
		if Queue.size==0:
			self.first=queueElement
			self.last=queueElement
		else:
			self.last.connectedTo=queueElement
			self.last=queueElement
		Queue.size+=1

#Remove an element
	def Dequeue(self):
		if Queue.size==0:
			print("Empty Queue")
			return
		elif Queue.size==1:
			self.first=None
			self.last=None
			Queue.size-=1
		else:
			current=self.first
			self.first = self.first.connectedTo
			current.value = None
			current.connectedTo=None
			del current
			Queue.size-=1

	def printQueue(self):
		current=self.first
		while current!=None:
			print(current.value,"-> ",end="")
			current=current.connectedTo
		print("END")

	def sizeOfQueue(self):
		return Queue.size

	def firstInQueue(self):
		return self.first.value


element1=Element(1)
element2=Element(2)
element3=Element(3)

myQueue = Queue()
myQueue.Enqueue(element1)
myQueue.Enqueue(element2)
myQueue.Enqueue(element3)

myQueue.printQueue()

myQueue.Dequeue()
myQueue.printQueue()
myQueue.Dequeue()
myQueue.printQueue()
myQueue.Dequeue()

myQueue.Dequeue()
