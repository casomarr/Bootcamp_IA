import numpy as np

a = [3,6,9]
print(a)
#print(a.transpose()) #list has no attribute transpose

b = np.array(a)
print(b)
print(b.T)

b = np.array([a])
print(b)
print(b.T)

a = [[3],
    [6],
    [9]]

b = np.array(a)
print(b)
print(b.T)

b = np.array([a])
print(b)
print(b.T)


# a = [[3,6,9]]
# print(a.transpose()) #list has no attribute transpose

