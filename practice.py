def find_continuous_section(matrix):
	def is_neighbor_continuous(i, j):
		if (i >= len(matrix) or j >= len(matrix[0]) or i < 0 or j < 0):
			return
		if matrix[i][j] == 0:
			return
		if matrix[i][j] == 1 and (i,j) in visited_coords:
			return
		else:
			visited_coords.add((i,j))
			is_neighbor_continuous.continuous_section += 1
			continuous_section_coords.append((i,j))

		is_neighbor_continuous(i-1, j)
		is_neighbor_continuous(i+1, j)
		is_neighbor_continuous(i, j-1)
		is_neighbor_continuous(i, j+1)

	visited_coords = set()
	max_continuous_section_coords = []
	continuous_section_coords = []
	is_neighbor_continuous.continuous_section = 0
	max_continuous_section = 0

	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j] == 1:
				is_neighbor_continuous(i, j)
				max_continuous_section = max(max_continuous_section, is_neighbor_continuous.continuous_section)
				if len(continuous_section_coords) > len(max_continuous_section_coords):
					max_continuous_section_coords = continuous_section_coords
				continuous_section_coords = []
				is_neighbor_continuous.continuous_section = 0

	return max_continuous_section_coords


matrix = [[0,0,1,1,1,0,0],
		  [0,0,1,0,1,0,0],
		  [0,0,0,0,0,0,0],
		  [0,1,1,1,1,0,0],
		  [0,0,0,1,1,1,0]]
print(find_continuous_section(matrix))

