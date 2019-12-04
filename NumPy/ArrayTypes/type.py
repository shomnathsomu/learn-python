import numpy as np

# All 0s matrix
a = np.zeros((2, 3))
print(a)

# All 1s matrix
b = np.ones((4, 2, 2), dtype='int32')
print(b)

# Any other number
c = np.full((2, 2), 99)
print(c)

# Any other number (full_like)
d = np.full_like(a, 4, dtype='int32')
print(d)

# random decimal number
e = np.random.rand(4, 2)
f = np.random.random_sample(a.shape)
print(f)

# Random Integer Value
g = np.random.randint(5, 11, size=(3, 4))
print(g)

# The identity matrix
j = np.identity(5)
print(j)

# Repeat an array
ra = np.array([[1, 2, 3]])
r1 = np.repeat(ra, 3, axis=0)
print(r1)

# Set an array into an another array
output = np.ones((5, 5))
z = np.zeros((3, 3))
z[1, 1] = 9
output[1:-1, 1:-1] = z
print(output)

# Copying an array
k = np.array([1, 2, 3])
m = k.copy()
m[0] = 100
print(k)
