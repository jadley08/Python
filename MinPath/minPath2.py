#would be better to use hashmap(dictionary) than list for visited
#this is doing weird stuff, not assigning ls in Grid init
from queue import PriorityQueue

class Grid(object):
	ls = [[1, 6, 0], [5, 6, 6], [5, 5, 5]]
	WIDTH = 3
	HEIGHT = 3
	pq = PriorityQueue()
	visited = []
	class Coord(object):
		coord = []
		priority = 0
		def __init__(self, c1, c2 = False):
			"""c1 is where we are coming from, c2 is where we are considering going"""
			if c2:
				self.coord = c2
				self.priority = Grid.ls[c1[1]][c1[0]] + Grid.ls[c2[1]][c2[0]]
			else:
				self.coord = c1
				self.priority = Grid.ls[c1[1]][c1[0]]

		def __eq__(self, other):
			return self.coord == other.coord

		def __ne__(self, other):
			return self.coord != other.coord

		def __lt__(self, other):
			return self.priority < other.priority

		def __le__(self, other):
			return self.priority <= other.priority

		def __gt__(self, other):
			return self.priority > other.priority

		def __ge__(self, other):
			return self.priority >= other.priority

		def __repr__(self):
			return "(" + str(self.coord[0]) + ", " + str(self.coord[1]) + ", " + str(self.priority) + ")"

	def __init__(self, l):
#		self.ls = l
#		self.HEIGHT = len(l)
#		self.WIDTH = len(l[0])
		self.visited.append([0,0])
		c = self.Coord([0,0])
		self.pq.put(c)

	def print_grid(self):
		for y in range(self.HEIGHT):
			for x in range(self.WIDTH):
				print(str(self.ls[y][x]), end="\t")
			print("\n")

	def dijkstra(self):
		while not self.pq.empty():
			c = self.pq.get()
			self.ls[c.coord[1]][c.coord[0]] = c.priority
			self.addNeighbors(c.coord)

	def addNeighbors(self, c):
		x = c[0]
		y = c[1]
		if x > 0 and not [x-1, y] in self.visited:
			coord = self.Coord(c, [x-1, y])
			self.pq.put(coord)
			self.visited.append([x-1, y])
		if x < self.WIDTH - 1 and not [x+1, y] in self.visited:
			coord = self.Coord(c, [x+1, y])
			self.pq.put(coord)
			self.visited.append([x+1, y])
		if y > 0 and not [x, y-1] in self.visited:
			coord = self.Coord(c, [x, y-1])
			self.pq.put(coord)
			self.visited.append([x, y-1])
		if y < self.HEIGHT - 1 and not [x, y+1] in self.visited:
			coord = self.Coord(c, [x, y+1])
			self.pq.put(coord)
			self.visited.append([x, y+1])

def main():
	#grid = Grid([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]])
	grid = Grid([])
	grid.print_grid()
	grid.dijkstra()
	print("\n\n")
	grid.print_grid()

main()
