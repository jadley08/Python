#2d array of 0's and -1's, find shortest path from top left to bottom right without using -1 squares (only 0's)
class Route(object):
	ls = []
	WIDTH = 0
	HEIGHT = 0
	
	def __init__ (self, ls):
		self.ls = ls
		self.HEIGHT = len(ls)
		self.WIDTH = len(ls[0])
		self.ls[self.HEIGHT-1][self.WIDTH-1] = 1

	def print_ls(self):
		"""prints a visual representation of 2d list as matrix

		Nothing -> Nothing"""
		for y in range(self.HEIGHT):
			for x in range(self.WIDTH):
				print(str(self.ls[y][x]), end="\t")
			print("\n")

	def isValidVal(self, x, y):
		"""checks to see if value at current location is okay, True if yes, False if no, also updates it"""
		currVal = self.ls[y][x]
		neighbs = []
		if y > 0 and self.ls[y-1][x] >= 0:
			neighbs.append([x, y-1])
		if y < self.HEIGHT-2 and self.ls[y+1][x] >= 0:
			neighbs.append([x, y+1])
		if x > 0 and self.ls[y][x-1] >= 0:
			neighbs.append([x-1, y])
		if x < self.WIDTH-2 and self.ls[x+1][y] >= 0:
			neighbs.append([x+1, y])
		b = True
		for n in neighbs:
			n_val = self.ls[n[1]][n[0]]
			if n_val == 0:
				b = False
			elif n_val < currVal - 1 or currVal == 0:
				self.ls[y][x] = n_val + 1
				currVal = self.ls[y][x]
				b = False
		return b

	def map_vals(self, x, y):
		"""at each location in 2dlist, value is shortest path from bottom right

		2dList -> 2dList"""
		self.print_ls()
		currVal = self.ls[y][x]
		if self.isValidVal(x, y):
			return
		else:
			#try to go up
			next_val = self.ls[y-1][x]
			if y > 0 and (abs(next_val - currVal) > 1 or next_val == 0 or abs(next_val - currVal) == 0) and (next_val != -11):
				self.map_vals(x, y-1)
			#try to go down
			next_val = self.ls[y+1][x]
			if y < self.HEIGHT-2 and (abs(next_val - currVal) > 1 or next_val == 0 or abs(next_val - currVal) == 0) and (next_val != -11):
				self.map_vals(x, y+1)
			#try to go left
			next_val = self.ls[y][x-1]
			if x > 0 and (abs(next_val - currVal) > 1 or next_val == 0 or abs(next_val - currVal) == 0) and (next_val != -11):
				self.map_vals(x-1, y)
			#try to go right
			next_val = self.ls[y][x+1]
			if x < self.WIDTH-2 and (abs(next_val - currVal) > 1 or next_val == 0 or abs(next_val - currVal) == 0) and (next_val != -11):
				self.map_vals(x+1, y)

	def main(self):
		self.print_ls()
		self.map_vals(self.WIDTH-1, self.HEIGHT-1)
		print("\n\n\n\n\n\n")
		self.print_ls()


route = Route([[0, 0, -11, 0, 0, 0], [0, -11, 0, 0, -11, 0], [0, 0, 0, -11, 0, 0], [0, 0, -11, 0, 0, 0], [0, 0, -11, 0, 0, 0]])
#route = Route([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
route.main()
