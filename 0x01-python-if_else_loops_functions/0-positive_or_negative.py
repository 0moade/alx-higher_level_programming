#!/usr/bin/python3
import random
number = random.randint(-10, 10)
for i in number:
	if number > 0:
		print("The {:d} is positive".format(number))
	elif number == 0:
		print("The {:d} is zero".format(number))
	elif number < 0:
		print("The {:d} is negative".format(number))
