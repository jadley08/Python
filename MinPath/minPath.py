#2d array of vals, find shortest path from top left to bottom right
#use dijkstra algorithm

class Route(object):
	ls = []
	WIDTH = 0
	HEIGHT = 0
	visited = []#list of coords ([y,x]) only that have already been calculated (in the cloud)

	def __init__ (self, ls):
		self.ls = ls
		self.HEIGHT = len(ls)
		self.WIDTH = len(ls[0])
		self.visited.append([0,0])

	def print_ls(self):
		"""prints a visual representation of 2d list as matrix

		Nothing -> Nothing"""
		for y in range(self.HEIGHT):
			for x in range(self.WIDTH):
				print(str(self.ls[y][x]), end="\t")
			print("\n")

	def dijkstra(self):
		"""blah"""
		#go over all neighbors and find min of them + their extension of the cloud
		#add that to the cloud with updated val
		while len(self.visited) != self.WIDTH * self.HEIGHT:
			self.print_ls()
			print()
			potentials = []
			for v in self.visited:
				potentials = potentials + self.neighbors(v)
			if len(potentials) > 0:
				minimum_val = potentials[0][1]
				minimum_pos = potentials[0][0]
				for p in potentials:
					if p[1] < minimum_val:
						minimum_val = p[1]
						minimum_pos = p[0]
				self.ls[minimum_pos[0]][minimum_pos[1]] = minimum_val
				self.visited.append(minimum_pos)

	def neighbors(self, pos):
		"""returns list of neighbors(coord and val to be)"""
		x = pos[1]
		y = pos[0]
		ns = []
		if x > 0 and not [[y, x-1]] in self.visited:
			ns.append([[y, x-1], self.ls[y][x] + self.ls[y][x-1]])
		if x < self.WIDTH - 1 and not [[y, x+1]] in self.visited:
			ns.append([[y, x+1], self.ls[y][x] + self.ls[y][x+1]])
		if y > 0 and not [[y-1, x]] in self.visited:
			ns.append([[y-1, x], self.ls[y][x] + self.ls[y-1][x]])
		if y < self.HEIGHT - 1 and not [[y+1, x]] in self.visited:
			ns.append([[y+1, x], self.ls[y][x] + self.ls[y+1][x]])
		return ns


	def main(self):
		self.print_ls()
		self.dijkstra()
		print("\n\n\n\n\n\n")
		self.print_ls()


route = Route([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]])
route.main()
print("\n------------------------------------\n")
#route = Route([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
#route.main()
#print("\n\n\n")
