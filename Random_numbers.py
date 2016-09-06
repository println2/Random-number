import time

def random():
	return int(time.time())

"""
formula = a(first number in range)+random number using time % number of terms in your range
"""
def print_random(name):
	print random()
	number = 7+random()%8
	return name+" "+str(number)

number = print_random('rahul')
print number