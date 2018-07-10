from queue import Queue,Element

# pass in arguments for the players and teh number of times to pass the "pototo before the music stops"
def hotPotato(names,times):
	myQueue = Queue()
	for name in names:
		myQueue.Enqueue(Element(name))
	myQueue.printQueue()

	
	while myQueue.sizeOfQueue()>1:
		for i in range(times):
			myQueue.Enqueue(myQueue.Dequeue())
		myQueue.Dequeue()
	print("Winner ->", myQueue.firstInQueue())


names = ["Aniketh","Nicole","Suresh","Anthony"]
hotPotato(names, 1000)
