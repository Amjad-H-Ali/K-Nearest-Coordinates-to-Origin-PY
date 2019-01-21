print("K-Nearest-Coordinates-to-Origin-PY!")

# Swaps elements in array
def swap(array, indx1, indx2):
	temp = array[indx1]

	array[indx1] = array[indx2]

	array[indx2] = temp

# Function that takes in tuple of points and prints the "k" elements that are closest to the origin
def find_nearest(points, k):
	print(points)
	# Call min_heap on parent nodes of k portion of array
	# to sort in min-heap 
	for indx in range(int(k/2) - 1, -1, -1):
		
		max_heap(points, indx, k)

	# TODO
	print(points)
	for indx in range(k, len(points)):

		if(points[0][0]**2 + points[0][1]**2 > points[indx][0]**2 + points[indx][1]**2):
			swap(points, indx, 0)
			max_heap(points, 0, k)
	print(points)		


# Function will take in array of size "k" containing relative distances of coordinates and sort it into a min-heap
def max_heap(array, indx, size):
	
	# Assume largest relative distance belongs to the parent node coordinate
	largest = indx	

	# Define and initialize left and right children nodes
	left = (indx * 2) + 1

	right = left + 1

	''' 
		* If left node relative distance is smaller, reinitalize largest variable
		* Relative Distance Formula:
			Ex: Coordinate (3,6)
				Relative Distance = 3² + 6²

	'''
	if(left < size and array[left][0]**2 + array[left][1]**2 > array[largest][0]**2 + array[largest][1]**2):

		largest = left

	# If right node relative distance is smaller, reinitalize largest variable
	if(right < size and array[right][0]**2 + array[right][1]**2 > array[largest][0]**2 + array[largest][1]**2):	

		largest = right

	# If parent node is not the largest element, swap with largest. Use reccursion to do the above code for the children nodes.
	if(largest != indx):
		swap(array, largest, indx)
		max_heap(array, largest, size)
		



# Tuple representing points on a Cartesian coordinate plane 
coordinates = [(-2, -4), (0, -2), (-1, 0), (3, -5), (-2, -3), (3, 2), (11, 2), (8, 0), (4, 5), (15, 2), (9, -9), (0,0)]

find_nearest(coordinates, 7)