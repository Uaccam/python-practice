def insertion_sort(array):
	for i in range(1, len(array)):
		key = array[i]
		j = i
		while j > 0 and array[j-1] > key:
			array[j] = array[j-1]
			j -= 1
		array[j] = key
	return array


if __name__ == '__main__':
	assert insertion_sort([2,5,1,3,9,4]) == [1,2,3,4,5,9]
	assert insertion_sort([78, 42, 101, 800, 5]) == [5,42,78,101,800]
	assert insertion_sort([0,0,1,1,0,0,2,1,0]) == [0,0,0,0,0,1,1,1,2]