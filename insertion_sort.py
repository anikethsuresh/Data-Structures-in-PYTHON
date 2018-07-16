def insertion_sort(numbers):
	for i in range(1, len(numbers)):
		current = numbers[i]
		position = i
		while position > 0 and numbers[position-1] > current :
			numbers[position] = numbers[position-1]
			position=position-1
		numbers[position]=current
	print(numbers)



numbers = [9,8,7,6,5]
insertion_sort(numbers)