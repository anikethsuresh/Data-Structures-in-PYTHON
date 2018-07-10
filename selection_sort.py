def selection_sort(items):
	# range from the last index to the first
	for i in range(len(items)-1,0,-1):
		largest = 0
		# iterating upto the second last number in the list
		for j in range(1,i):
			if items[j] > items[largest]:
				largest = j
		if items[largest]> items[i]:
			# swap if larger
			items[i], items[largest] = items[largest], items[i]
	print(items)


items = [9,8,7,6,5,4,3,2,1]
selection_sort(items)
