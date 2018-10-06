import functools
import time

def timer(func):
	@functools.wraps(func)
	def wrapper_timer(*args, **kwargs):
		start_time = time.perf_counter()
		value = func(*args, **kwargs)
		end_time = time.perf_counter()
		run_time = end_time - start_time
		print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
		return value
	return wrapper_timer

@timer
def waste_some_time(num_times):
	res = 0
	for _ in range(num_times):
		res += sum([i**2 for i in range(10000)])
	return res
