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

	def map_vals(self, x, y):
		"""at each location in 2dlist, value is shortest path from bottom right

		2dList -> 2dList"""
		#self.print_ls()
		#print()
		currVal = self.ls[y][x]
		n_vals = []
		if y > 0:
			n_vals.append(self.ls[y-1][x])
		if y < self.HEIGHT-1:
			n_vals.append(self.ls[y+1][x])
		if x > 0:
			n_vals.append(self.ls[y][x-1])
		if x < self.WIDTH-1:
			n_vals.append(self.ls[y][x+1])
		for val in n_vals:
			if val > 0 and (currVal - val > 1): #only reset currVal if the neighboring val isn't 0 or an obstacle and it is 2 or more smaller than us
				self.ls[y][x] = val+1
				currVal = val+1
			elif currVal == 0 and val > 0: #if our currVal is 0, we need to just set it to something
				self.ls[y][x] = val+1
				currVal = val+1
		#try to go up
		if y > 0:
			next_val = self.ls[y-1][x]
		if y > 0 and (abs(next_val - currVal) > 1 or next_val == 0) and (next_val != -11):
			self.map_vals(x, y-1)
		#try to go down
		if y < self.HEIGHT-1:
			next_val = self.ls[y+1][x]
		if y < self.HEIGHT-1 and (abs(next_val - currVal) > 1 or next_val == 0) and (next_val != -11):
			self.map_vals(x, y+1)
		#try to go left
		if x > 0:
			next_val = self.ls[y][x-1]
		if x > 0 and (abs(next_val - currVal) > 1 or next_val == 0) and (next_val != -11):
			self.map_vals(x-1, y)
		#try to go right
		if x < self.WIDTH-1:
			next_val = self.ls[y][x+1]
		if x < self.WIDTH-1 and (abs(next_val - currVal) > 1 or next_val == 0) and (next_val != -11):
			self.map_vals(x+1, y)

	def main(self):
		self.print_ls()
		self.map_vals(self.WIDTH-1, self.HEIGHT-1)
		print("\n\n\n\n\n\n")
		self.print_ls()


route = Route([[0, 0, -11, 0, 0, 0], [0, -11, 0, 0, -11, 0], [0, 0, 0, -11, 0, 0], [0, 0, -11, 0, 0, 0], [0, 0, -11, 0, 0, 0]])
route.main()
print("\n\n\n")
route = Route([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
route.main()
print("\n\n\n")

