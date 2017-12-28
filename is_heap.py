def is_heap(heap_array):
	'''return true if hip_array has heap properties'''
	for i in range(len(heap_array)//2, len(heap_array)):
		j = i
		while j > 1:
			print('i',i,'j',j)
			if heap_array[j//2] < heap_array[j]:
				return False
			j //=2
	return True
