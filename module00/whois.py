import sys

if len(sys.argv) != 2:
  print("Error")
  sys.exit(1)
  
try:
  nb = int(sys.argv[1])
except ValueError:
  print("Error")
  sys.exit(1)
  
if nb == 0:
  print("The number is zero")
elif nb%2 == 0:
  print("The number is even")
else:
  print("The number is odd")

