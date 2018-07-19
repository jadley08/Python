#given two strings, find the longest common substring
s = ['a', 'g', 'a', 'c', 'a', 't']
r = ['g', 'a', 'c', 'g', 't', 'a']
lenS = len(s)
lenR = len(r)
m = []
for y in range(lenR+1):
	mRow = []
	for x in range(lenS+1):
		mRow.append(0)
	m.append(mRow)

def delta(x, y):
	if x == y:
		return 1
	else:
		return 0

for i in range(1, lenR+1):
	for j in range(1, lenS+1):
		m[i][j] = max(m[i-1][j], m[i][j-1], delta(s[j-1], r[i-1]) + m[i-1][j-1])

def matrix_print(arr):
	for row in range(len(arr)):
		for column in range(len(arr[0])):
			print(str(m[row][column]), end="\t")
		print("\n")

matrix_print(m)

def build_lcs(ls, s, r):
	#build_backwards (ez)
	st = ""
	x = lenS
	y = lenR
	while x > 0 and y > 0:
		if s[x-1] == r[y-1] and m[y][x] == m[y-1][x-1] + 1:
			st = s[x-1] + st
			x = x - 1
			y = y - 1
		elif m[y][x] == m[y][x-1]:
			x = x - 1
		else:
			y = y - 1
	return st

print(build_lcs(m, s, r))
