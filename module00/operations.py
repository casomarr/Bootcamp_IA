import sys

if len(sys.argv) != 3:
	print("AssertionError: wrong number of arguments : only 2 expected")
	sys.exit(1)

try: #error if at least one is false
	A = int(sys.argv[1])
	B = int(sys.argv[2])
except ValueError:
	print("AssertionError: only integers expected")
	sys.exit(1)

print("Sum: ", A+B)
print("Difference: ", A-B)
print("Product: ", A*B)
if B == 0:
	print("Quotien: ERROR (division by zero)")
	print("Remainder: ERROR (modulo by zero)")
else:
	print("Quotien: ", A/B)
	print("Remainder: ", A%B)