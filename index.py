print("K-Nearest-Coordinates-to-Origin-PY!")

# Function that takes in tuple of points and prints the "k" elements that are closest to the origin
def find_nearest(points, k):
	
	# Call min_heap on parent nodes of k portion of array
	# to sort in min-heap 
	for indx in range(int(k/2) - 1, -1, -1):
		
		min_heap(points, indx, k)




# Function will take in array of size "k" containing relative distances of coordinates and sort it into a min-heap
def min_heap(array, indx, size):
	
	# Assume smallest relative distance belongs to the parent node coordinate
	smallest = indx	

	# Define and initialize left and right children nodes
	left = (indx * 2) + 1

	right = left + 1

	''' 
		* If left node relative distance is smaller, reinitalize smallest variable
		* Relative Distance Formula:
			Ex: Coordinate (3,6)
				Relative Distance = 3² + 6²

	'''
	if(array[left] < size and array[left][0]**2 + array[left][1]**2 < array[smallest][0]**2 + array[smallest][1]**2):

		smallest = left

	# If right node relative distance is smaller, reinitalize smallest variable
	if(array[right] < size and array[right][0]**2 + array[right][1]**2 < array[smallest][0]**2 + array[smallest][1]**2):	

		smallest = right

		



# Tuple representing points on a Cartesian coordinate plane 
coordinates = [(-2, -4), (0, -2), (-1, 0), (3, -5), (-2, -3), (3, 2)]

find_nearest(coordinates, 3)