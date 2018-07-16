def mergesort(unorderedList):
    if len(unorderedList) > 1: # Base case
        middle = len(unorderedList) // 2 # continuously split until base case
        leftPart = unorderedList[:middle]
        rightPart = unorderedList[middle:]
        # recursively call the mergesort function on either half
        mergesort(leftPart)
        mergesort(rightPart)
        indexForLeft = indexForRight = 0
        mainIndex = 0
        rightFlag = True
        leftFlag = True
        while mainIndex!=len(unorderedList) and rightFlag and leftFlag:
        	# sort the left half
        	if leftPart[indexForLeft] <= rightPart[indexForRight] :
        		unorderedList[mainIndex] = leftPart[indexForLeft]
        		indexForLeft +=1
        	# sort the right half	
        	else:
        		unorderedList[mainIndex] = rightPart[indexForRight]
        		indexForRight +=1
        	# incase the end of the halves are reached
        	if indexForLeft == len(leftPart):
        		leftFlag = False
        	if indexForRight == len(rightPart):
        		rightFlag = False
        	mainIndex +=1
         # this is to add the remaining numbers in the right half
        if rightFlag:
        	while mainIndex!=len(unorderedList):
        		unorderedList[mainIndex] = rightPart[indexForRight]
        		indexForRight +=1
        		mainIndex+=1
        # this is to add the remaining numbers in the left half
        if leftFlag:
        	while mainIndex!=len(unorderedList):
        		unorderedList[mainIndex] = leftPart[indexForLeft]
        		indexForLeft +=1
        		mainIndex+=1

numbers = [9,5,1,4,6,3,2,45,6,76,54,3,44,67,87,5,6,5,4,3,3,4]
mergesort(numbers)
print(numbers)