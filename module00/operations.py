import sys

if len(sys.argv) != 3:
  print("Error: not the right amount of arguments")
  sys.exit(1)
try:
  A = int(sys.argv[1])
  B = int(sys.argv[2])
except ValueError:
  print("Error: argument is not an integer")
  sys.exit(1)

print("Sum:", A+B)
print("Difference:", A-B)
print("Product:", A*B)
if B == 0:
  print("Error: cannot divide or make modulo by 0")
else:
  print("Quotien:", A/B)
  print("Remainder:", A%B)
