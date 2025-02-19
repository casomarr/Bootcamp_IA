import sys

if len(sys.argv) < 2:
	sys.exit(1)
if len(sys.argv) > 2:
	print("AssertionError: more than one argument are provided")
	sys.exit(1)

try:
	number = int(sys.argv[1])
except ValueError:
	print("AssertionError: argument is not an integer")
	sys.exit(1)

if number == 0:
	print("I'm Zero.")
elif number%2 == 0:
	print("I'm Even.")
else:
	print("I'm Odd.")