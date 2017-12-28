
def is_heap(array):
	
	'''return true if hip_array has heap properties'''
	for i in range(1,(len(array)//2)+1):
		if (2*i)+1 < len(array):
			if array[i] < array[2*i] or array[i] < array[(2*i) +1]:
				return False
		elif array[i] < array[2*i]:
			return False
		print('i',i,'i*2',2*i,'i*2+1')
		
	return True
