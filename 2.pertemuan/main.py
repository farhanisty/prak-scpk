import numpy as np

a = np.array([[1,2], [3,4]])
b = np.array([[5,6], [7,8]])
g = np.array([[1,3], [5,6]])

c = a.dot(b)
print(c)

d = c.T

print(d)

e = np.hstack((d, g))

print(e)

print(e[1,0])
