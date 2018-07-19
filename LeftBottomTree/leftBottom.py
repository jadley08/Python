#return the value at the leftmost spot of the bottom layer of a tree
#note could use a linked list instead of a dictionary for m, then either go through and print whole list or just return the one at the end (using DLL)
class Tree(object):
	class Node(object):
		value = 0
		left = None
		right = None
		def __init__(self, value, left=None, right=None):
			self.value = value
			self.left = left
			self.right = right

	root = None
	m = {}
	maxDepth = 0

	def __init__(self, root = None):
		self.root = root

	def find(self):
		self.findHelper(self.root, 0)
		return self.m[self.maxDepth]

	def findHelper(self, n, d):
		if n != None:
			if not d in self.m:
				self.m[d] = n.value
				if d > self.maxDepth:
					self.maxDepth = d
			self.findHelper(n.left, d+1)
			self.findHelper(n.right, d+1)

	def __repr__(self):
		s = ""
		for key in range(self.maxDepth + 1): #for key in self.m:
			s += "Leftmost node at depth=" + str(key) + " has value=" + str(self.m[key]) + "\n"
		return s

	def main(self):
		"""					a
				b					c
			d		e			f		g
						h					i
										j"""
		d = self.Node("d")
		h = self.Node("h")
		f = self.Node("f")
		j = self.Node("j")
		e = self.Node("e", None, h)
		b = self.Node("b", d, e)
		i = self.Node("i", j, None)
		g = self.Node("g", None, i)
		c = self.Node("c", f, g)
		a = self.Node("a", b, c)
		self.root = a
		self.find()
		print(self)

tr = Tree()
tr.main()
