def l_i_s (ls_in):
	"""returns the longest increasing subsequence of the given list
	recursive (slow) brute force algorithm
	List of Numbers -> List of Numbers"""
	return helper(ls_in, [], 0)

def helper(ls_in, ls_out, index):
	if index < len(ls_in):
		if len(ls_out) == 0 or ls_in[index] > ls_out[len(ls_out) - 1]:
			ls_1 = helper(ls_in, ls_out + [ls_in[index]], index+1)
			ls_2 = helper(ls_in, ls_out, index+1)
			if len(ls_1) > len(ls_2):
				return ls_1
			else:
				return ls_2
		else:
			return helper(ls_in, ls_out, index+1)
	else:
		return ls_out

#print(l_i_s([1, 4, 5, 2, 3, 7, 4, 5]))


def better_l_i_s (a):
	"""dp sol'n"""
	score = []
	score.append(a)
	for i in range(0, len(score)):
		score[i] = 0
	parent = []
	parent.append(a)
	for i in range(0, len(parent)):
		parent[i] = 0
	score[0] = 1
	parent[0] = -1
	max_score = 1
	for i in range(1, len(a)):
		max_seen = 1
		par = -1
		for j in range(0, i):
			if a[j] < a[i] and score[j] + 1 > max_seen:
				max_seen = score[j] + 1
				par = j
		parent[i] = par
		score[i] = max_seen
		if max_seen > max_score:
			max_score = max_seen
	return_ls = []
	for i in range(0, max_score):
		return_ls[i] = 0
	ind = len(score) - 1
	while True:
		if score[ind] == max_score:
			break
		ind = ind - 1
	par = ind
	ind = max_score - 1
	while par != -1:
		return_ls[ind] = a[par]
		par = parent[par]
	return return_ls

print(better_l_i_s([1, 4, 5, 2, 3, 7, 4, 5]))
