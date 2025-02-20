import sys
from time import sleep
import time

def ft_progress(lst):
	total_elem = len(lst)
	start_time = time.time()
	i = 1
	for elem in lst:
		elapsed_time = time.time() - start_time
		progress = i / total_elem
		bar_length = 42
		bar_filled = int(bar_length * progress)
		bar = '=' * bar_filled + '>' + ' ' * (bar_length - bar_filled)
		percent = progress * 100
		eta = elapsed_time / (i + 1) * (total_elem - i - 1)
		print(f"\rETA: {eta:.2f}s [{percent:6.2f}%][{bar}] {i + 1}/{total_elem} | elapsed time {elapsed_time:.2f}s", end='')
		i = i + 1
		yield elem # creates a generator function : it returns an iterator
	print()


listy = range(1000) #listy is a "range object" that generates numbers from 0 to 999
ret = 0
for elem in ft_progress(listy):
	ret += elem #this line is arbitrary, just to simulate that some work is being done
	sleep(0.01)
print() #prints an empty line
print(ret)