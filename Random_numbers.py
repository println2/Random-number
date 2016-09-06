import time

def random():
	return int(time.time())

"""
formula = a(first numbre in range)+random number using time % number of terms in your range
"""
def print_random():
	print random()
	number = 6+random()%10
	print number

print_random()