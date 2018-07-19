#longest palidrome subsequence

def lps(st):
	"""longest palidrome subsequence"""
	st-rev = []
	for i in range(0, len(st)):
		st-rev[len(st) - i - 1] = st[i]
	return lcs(st, st-rev)

def lcs(st1, st2):
	"""longest common subsequence"""
	m = []
	for i in range(0, len(st1)):
		ls = []
		for j in range(0, len(st2)):
			if i == 0 or j == 0:
				ls.append(0)
			else:
				ls.append(-1)
		m.append(ls)

	for i in range(0, len(st1)):
		 for j in range(0, len(st1)):
			m[j][i] = max(m[j][i-1], m[j-1][i], (delta(st1[i], st2[j]) + m[j-1][i-1]))

	i = len(st1) - 1
	j = len(st2) - 1
	ls = []
	while i >= 0 and j >= 0:
		if st1[i] == st2[j] and m[j][i] == m[j-1][i-1] + 1:
			ls = [st1[i]] + ls
			i = i - 1
			j = j - 1
		elif m[j][i] = m[j][i-1]:
			i = i - 1
		else:
			j = j - 1
	return ls

def delta(c1, c2):
	if c1 == c2:
		return 1
	else:	
		return 0

print(lps("characters"))
