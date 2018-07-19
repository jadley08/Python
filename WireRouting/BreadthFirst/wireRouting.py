#2d array of 0's and -1's, find shortest path from top left to bottom right without using -1 squares (only 0's)
import queue

class Route(object):
	ls = []
	WIDTH = 0
	HEIGHT = 0
	q = queue.Queue()

	def __init__ (self, ls):
		self.ls = ls
		self.HEIGHT = len(ls)
		self.WIDTH = len(ls[0])
		self.ls[0][0] = 1
		self.q.put([0,0]) #where we start in the list

	def print_ls(self):
		"""prints a visual representation of 2d list as matrix

		Nothing -> Nothing"""
		for y in range(self.HEIGHT):
			for x in range(self.WIDTH):
				print(str(self.ls[y][x]), end="\t")
			print("\n")

	def map_vals(self):
		"""at each location in 2dlist, value is shortest path from start

		2dList -> 2dList"""
		while not self.q.empty():
			cur_pos = self.q.get()
			cur_x = cur_pos[1]
			cur_y = cur_pos[0]
			cur_val = self.ls[cur_y][cur_x]
			for n in self.neighbors(cur_pos):
				n_x = n[1]
				n_y = n[0]
				self.ls[n_y][n_x] = cur_val + 1
				self.q.put(n)

	def neighbors(self, pos):
		x = pos[1]
		y = pos[0]
		ns = []
		if x > 0 and self.ls[y][x-1] == 0:
			ns.append([y, x-1])	
		if x < self.WIDTH - 1 and self.ls[y][x+1] == 0:
			ns.append([y, x+1])
		if y > 0 and self.ls[y-1][x] == 0:
			ns.append([y-1, x])
		if y < self.HEIGHT - 1 and self.ls[y+1][x] == 0:
			ns.append([y+1, x])
		return ns


	def main(self):
		self.print_ls()
		self.map_vals()
		print("\n\n\n\n\n\n")
		self.print_ls()


route = Route([[0, 0, -1, 0, 0, 0], [0, -1, 0, 0, -1, 0], [0, 0, 0, -1, 0, 0], [0, 0, -1, 0, 0, 0], [0, 0, -1, 0, 0, 0]])
route.main()
print("\n------------------------------------\n")
route = Route([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
route.main()
print("\n\n\n")
