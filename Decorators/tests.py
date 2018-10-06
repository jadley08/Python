import decorators
import math

@decorators.timer
def waste_some_time(num_times):
	res = 0
	for _ in range(num_times):
		res += sum([i*2 for i in range(10000)])
	return res

math.factorial = decorators.debug(math.factorial)
def approximate_e(terms=18):
	return sum(1 / math.factorial(n) for n in range(terms))
