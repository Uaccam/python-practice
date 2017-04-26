def bubble_sort(array):
	for m in range(len(array)-1, 0, -1):
		for i in range(m):
			if array[i] > array[i+1]:
				array[i], array[i+1] = array[i+1], array[i]

	return array


if __name__ == '__main__':
	assert bubble_sort([7,3,5,1]) == [1,3,5,7]
	assert bubble_sort([9,8,7,6,5,4,3,2,1]) == [1,2,3,4,5,6,7,8,9]
	assert bubble_sort([2,2,3,5,1,1,1,8,6]) == [1,1,1,2,2,3,5,6,8]
	assert bubble_sort([10,15,2,100,55]) == [2,10,15,55,100]