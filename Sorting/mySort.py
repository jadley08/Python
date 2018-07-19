#worse radix lol
#O(n*(max number))
def my_sort(original_ls):
	mutated_ls = original_ls[:]
	return_ls = original_ls[:]
	index = 0
	while index < len(return_ls):
		for i in range(len(mutated_ls)):
			if mutated_ls[i] == 0:
				return_ls[index] = original_ls[i]
				index += 1
				if index >= len(mutated_ls):
					break
			mutated_ls[i] = mutated_ls[i] - 1
	return return_ls


ls = [3, 5, 6, 8, 3, 4, 6, 8, 4, 2, 1, 3, 5, 7, 9]
print(ls)
ls2 = my_sort(ls)
print(ls2)
