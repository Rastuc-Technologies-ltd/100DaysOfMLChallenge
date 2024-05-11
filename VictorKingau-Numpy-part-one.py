import numpy as np

#QUESTION 1

def make_np_array(list):
	'''
	Creates a 1D numpy array 
	takes a list as anargument
	'''
	array = np.array(list)
	return array

arr = make_np_array([1,2,3,4,5])
print(arr)

# QUESTION 2

def random_array2D(lowerLimit,upperLimit,shape):
	'''
	creates a 2D numpy array of randon integers
	arg shape -> tuple
	'''
	import random
	tmpList = []
	inList = []
	row = 0
	while row < shape[0]:
		for i in range(shape[1]):
			inList.append(random.randint(lowerLimit, upperLimit))
		
		tmpList.append(inList)
		inList = []
		row += 1

	array = np.array(tmpList)
	return array

#array2D = random_array2D(1,6, (3,4))

# alternative solution

def random_arrayV2(lowerLimit,upperLimit, shape):
	return np.random.randint(lowerLimit, upperLimit, size = (shape))


#array2D = random_arrayV2(1,6,(3,4))
#print(array2D)

#QUESTION 3

def ones_3D_Array(shape):
	'''
	creates a 3D numpy array of ones 
	takes args as tuple of 3 elements
	'''
	array = np.ones(shape, dtype = np.int16)
	return array

array3D = ones_3D_Array((2,3,4))
#print(array3D)
