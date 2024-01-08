def partition(array, low, high):
	pivot = array[high]
	print(high)
	print(pivot)
	i = low - 1
	print('i : ',i)
	for j in range(low, high):
		if array[j] <= pivot:
			i = i + 1
			print('i= ',i)
			(array[i], array[j]) = (array[j], array[i])
			print(array)
	print('high : ',high)
	print(array[i+1],array[high])
	(array[i + 1], array[high]) = (array[high], array[i + 1])
	print(array[i+1],array[high])
	print(array)
	return i + 1
def quickSort(array, low, high):
	if low < high:
		pi = partition(array, low, high)
		print('pi : ',pi)
		print('low',low)
		quickSort(array, low, pi - 1)
		print('2:',array)
		quickSort(array, pi + 1, high)
data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)
size = len(data)
quickSort(data, 0, size - 1)
print('Sorted Array in Ascending Order:')
print(data)
