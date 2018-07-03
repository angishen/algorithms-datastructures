def find_continuous_section(matrix):
	def is_neighbor_one(i, j):
		if i is None or j is None:
			return
		if matrix[i][j] == 0:
			return
		if matrix[i][j] == 1 and (i,j) in visited_cords:
			return
		else:
			visited_coords.add(i,j)
			max_continuous_section += 1
		is_neighbor_one(i-1, j)
		is_neighbor_one(i+1, j)
		is_neighbor_one(i, j-1)
		is_neighbor_one(i, j+1)

	max_continous_section = 0
	visited_coords = set()
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j] == 1:
				is_neighbor_one(i, j)

	

	return max_continous_section

